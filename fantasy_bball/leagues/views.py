import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from leagues.models import League, Team
from players.models import Player


class JSONHttpResponse(HttpResponse):
    def __init__(self, content=None, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        content = json.dumps(content, cls=DjangoJSONEncoder)
        super(JSONHttpResponse, self).__init__(content, *args, **kwargs)


class JSONView(View):

    def dispatch(self, request, *args, **kwargs):
        data = super(JSONView, self).dispatch(request, *args, **kwargs)

        if isinstance(data, HttpResponse):
            return data
        else:
            return JSONHttpResponse(data)


class LeaguesView(JSONView):

	def get(self, request):
		data = [league.to_data() for league in League.objects.filter(is_public=True)]
		return data


class LeagueView(JSONView):

	def get(self, request, league_id):
		data = League.objects.get(id=league_id).to_data()
		return data


class FreeAgentsView(JSONView):

    def get(self, request, league_id):
        players = [p for p in Player.objects.all() if p.is_available(league_id=league_id)]
        data = [
            player.to_data() for player in players
        ]

        return data


class TeamView(JSONView):

	def get(self, request, team_id):
		team = Team.objects.get(id=team_id)
		return team.to_data(player_data=True)

