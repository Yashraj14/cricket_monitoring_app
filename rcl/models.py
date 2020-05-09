from django.db import models

# Create your models here.
class Teams(models.Model):
    team_flag=models.ImageField(blank=True,null=True)
    teamName=models.CharField(max_length=50, primary_key=True,default='hello')
    user_img=models.ImageField(blank=True,null=True)
    user_desc=models.CharField(max_length=150,null=True)


    def __str__(self):
        return self.teamName

    class Meta:
        verbose_name_plural = "teams"

class Fixture(models.Model):
    team_1_flag=models.ImageField(blank=True,null=True)
    team_1=models.ForeignKey(Teams, on_delete=models.CASCADE,max_length=50,related_name='team1',db_column='team_1',default='team')
    team_2_flag=models.ImageField(blank=True,null=True)
    team_2=models.ForeignKey(Teams, on_delete=models.CASCADE,max_length=50,related_name='team2',db_column='team_2',default='team')
    venue=models.CharField(max_length=10,default='Cape Town')

    def __str__(self):
        template = '{0.team_1_flag} {0.team_1} {0.team_2_flag} {0.team_2} {0.venue}'
        return template.format(self)

    class Meta:
        verbose_name_plural = "Fixtures"



class Admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Scorecard(models.Model):
    team_name_1 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name='home', db_column='team_name_1',default='hello')
    runs_team_1=models.IntegerField(null=True)
    overs_team_1=models.FloatField(null=True)
    wickets_team_1=models.IntegerField(null=True)
    team_name_2 = models.ForeignKey(Teams, on_delete=models.CASCADE,related_name='away', db_column='team_name_2',default='hello')
    runs_team_2=models.IntegerField(null=True)
    overs_team_2=models.FloatField(null=True)
    wickets_team_2=models.IntegerField(null=True)


    def __str__(self):
        template = '{0.team_name_1} {0.runs_team_1} {0.overs_team_1} {0.wickets_team_1} {0.team_name_2} {0.runs_team_2} {0.overs_team_2} {0.wickets_team_2}'
        return template.format(self)
    class Meta:
        verbose_name_plural = "Scorecard"
        db_table = 'Scorecard'

class Points(models.Model):
    team_img=models.ImageField(blank=True,null=True)
    team_name= models.ForeignKey(Teams,on_delete=models.CASCADE,db_column='team_name',default='team')
    played=models.IntegerField(default=0)
    won=models.IntegerField(default=0)
    lost=models.IntegerField(default=0)
    tie=models.IntegerField(default=0)
    points=models.IntegerField(default=0)
    net_runrate=models.FloatField(default=0.00)

    def __str__(self):
        template = '{0.team_name} {0.played} {0.won} {0.lost} {0.tie} {0.points} {0.net_runrate} '
        return template.format(self)

    class Meta:
        verbose_name_plural="Points_table"
        db_table="Points"
