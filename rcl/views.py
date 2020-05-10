from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import NewScorecardForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'rcl/index.html')

def admin(request):

        if request.method=='POST':
            username= request.POST.get('username')
            password= request.POST.get('pwd')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                teams_set=Teams.objects.all()
                return render(request,'rcl/results.html',{'teams_set': teams_set})

        return render(request, 'rcl/login.html')

def logoutAdmin(request):
    logout(request)
    return render(request,'rcl/index.html')


def results(request):
    teams_set=Teams.objects.all()
    return render(request,'rcl/results.html',{'teams_set': teams_set})

def add_team_score(request):

    # SCORECARD TABLE SAVING BEGINS HERE #

        runs_team_1=request.POST["runs"]
        overs_team_1=request.POST["overs"]
        wickets_team_1=request.POST["wickets"]
        runs_team_2=request.POST["runs1"]
        overs_team_2=request.POST["overs1"]
        wickets_team_2=request.POST["wickets1"]
        team_data= Scorecard(team_name_1=Teams.objects.get(teamName=request.POST["drop1"]),runs_team_1=runs_team_1,overs_team_1=overs_team_1,wickets_team_1=wickets_team_1, team_name_2=Teams.objects.get(teamName=request.POST["drop2"]),runs_team_2=runs_team_2,overs_team_2=overs_team_2,wickets_team_2=wickets_team_2)
        team_data.save()

    # POINTS TABLE SAVING BEGINS HERE

        nrr=(int(team_data.runs_team_1)/float(team_data.overs_team_1))-(int(team_data.runs_team_2)/float(team_data.overs_team_2))
        nrr1=(int(team_data.runs_team_2)/float(team_data.overs_team_2))-(int(team_data.runs_team_1)/float(team_data.overs_team_1))

        
        team1 = Points.objects.get(team_name=team_data.team_name_1) #null
        if(team1.played != 0):
                
                if(team_data.runs_team_1>team_data.runs_team_2):
                        Points.objects.filter(team_name=team_data.team_name_1).update(played=team1.played+1,won=team1.won+1,lost=team1.lost,points=team1.points+2,net_runrate=(team1.net_runrate+nrr)/2)
                else:
                        Points.objects.filter(team_name=team_data.team_name_1).update(played=team1.played+1,won=team1.won,lost=team1.lost+1,points=team1.points,net_runrate=(team1.net_runrate+nrr)/2)

        else:
                if(team_data.runs_team_1>team_data.runs_team_2):
                    team_points=Points(team_name=team_data.team_name_1,played=1,won=1,lost=0,tie=0,points=2,net_runrate=nrr)
                    team_points.save()
                else:
                    team_points=Points(team_name=team_data.team_name_1,played=1,won=0,lost=1,tie=0,points=0,net_runrate=nrr)
                    team_points.save()

        team2 = Points.objects.get(team_name=team_data.team_name_2)
        if(team2.played != 0):

                if(team_data.runs_team_1>team_data.runs_team_2):
                        Points.objects.filter(team_name=team_data.team_name_2).update(played=team2.played+1,won=team2.won,lost=team2.lost+1,points=team2.points,net_runrate=(team2.net_runrate+nrr1)/2)
                else:
                        Points.objects.filter(team_name=team_data.team_name_2).update(played=team2.played+1,won=team2.won+1,lost=team2.lost,points=team2.points+2,net_runrate=(team2.net_runrate+nrr1)/2)

        else:
                if(team_data.runs_team_1>team_data.runs_team_2):
                    team_points1=Points(team_name=team_data.team_name_2,played=1,won=0,lost=1,tie=0,points=0,net_runrate=nrr1)
                    team_points1.save()
                else:
                    team_points1=Points(team_name=team_data.team_name_2,played=1,won=1,lost=0,tie=0,points=2,net_runrate=nrr1)
                    team_points1.save()


        messages.success(request,'Scorecard Submitted Successfully !')
        return render(request,'rcl/results.html')

def matches(request):
    score_set=Scorecard.objects.all()
    return render(request,'rcl/matches.html',{'score_set':score_set})

def points_view(request):
    team_info=Points.objects.all().order_by('-points', '-net_runrate')
    return render(request,'rcl/points.html',{'team_info':team_info})

def Fixture_view(request):
    team_info1=Fixture.objects.all().order_by('id')
    return render(request,'rcl/fixtures.html',{'team_info1':team_info1})

def Teams_view(request):
    player_info=Teams.objects.all().order_by('teamName')
    return render(request,'rcl/teams.html',{'player_info':player_info})

def Abouts_view(request):
    return render(request,'rcl/about.html')
