from django import forms

class LeagueForm(forms.Form):
    name = forms.CharField()
    num_teams = forms.IntegerField()
    roster_size = forms.IntegerField()
    