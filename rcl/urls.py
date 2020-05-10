from django.urls import path
from . import views


app_name = 'rcl'
urlpatterns =[
    path('/index', views.index, name='index'),
    path('admin/',views.admin,name='admin'),
    path('logoutAdmin/',views.logoutAdmin,name='logoutAdmin'),
    path('results/',views.results,name='results'),
    path('add_team_score/',views.add_team_score,name='add_team_score'),
    path('matches/',views.matches,name='matches'),
    path('points_view/',views.points_view,name='points'),
    path('Fixture_view/',views.Fixture_view,name='Fixture'),
    path('Teams_view/',views.Teams_view,name='Teams'),
    path('Abouts_view/',views.Abouts_view,name='About'),

]
