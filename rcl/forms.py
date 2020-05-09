from django import forms


class NewScorecardForm(forms.Form):
    runs_team_1=forms.IntegerField()
    overs_team_1=forms.FloatField()
    wickets_team_1=forms.IntegerField()
    runs_team_2=forms.IntegerField()
    overs_team_2=forms.FloatField()
    wickets_team_2=forms.IntegerField()
