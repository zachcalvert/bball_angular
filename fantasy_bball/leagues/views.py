import json
from datetime import date, timedelta

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

from leagues.models import League, Team
from players.models import Player, Quote
from schedule.models import Season, Game, StatLine, Matchup


class BDLView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(BDLView, self).get_context_data(*args, **kwargs)
        quote = Quote.objects.order_by('?').first()
        context["quote"] = quote
        return context


class HomePageView(BDLView):
    template = "site_base.html"

    def top_performers(self, day):
        games = Game.objects.filter(date=day)
        statlines = list(StatLine.objects.filter(game__in=games))
        statlines.sort(key=lambda x: x.game_score, reverse=True)
        return statlines[:4] # grab the 4 best performances

    def goat_performances(self):
        season = Season.objects.last()
        games = Game.objects.filter(season=season, date__lt=date.today())
        statlines = list(StatLine.objects.filter(game__in=games))
        statlines.sort(key=lambda x: x.game_score, reverse=True)
        return statlines[:20]

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        yesterday = date.today() - timedelta(days=1)
        yesterdays_best = self.top_performers(yesterday)
        if not yesterdays_best:
            yesterday = date.today() - timedelta(days=2)
            yesterdays_best = self.top_performers(yesterday)


        context["leagues"] = League.objects.filter(is_public=True) 
        context["yesterday"] = yesterday.strftime("%A, %B %-d")
        context["yesterdays_best"] = yesterdays_best
        context["season_best"] = self.goat_performances()
        return context


class LeagueView(BDLView):
    template_name = "league.html"

    def get_context_data(self, *args, **kwargs):
        context = super(LeagueView, self).get_context_data(*args, **kwargs)
        league = League.objects.get(id=kwargs['league_id'])
        league_data = league.to_data()

        context["league_data"] = league_data
        return context


class TeamView(BDLView):
    template_name = "team.html"

    def get_context_data(self, *args, **kwargs):
        context = super(TeamView, self).get_context_data(*args, **kwargs)
        team = Team.objects.get(id=kwargs['team_id'])
        team_data = team.to_data(player_data=True)

        context["team_data"] = team_data
        return context

# class LeaguesView(JSONView):

# 	def get(self, request):
# 		data = [league.to_data() for league in League.objects.filter(is_public=True)]
# 		return data


# class LeagueView(JSONView):

# 	def get(self, request, league_id):
# 		data = League.objects.get(id=league_id).to_data()
# 		return data


# class FreeAgentsView(JSONView):

#     def get(self, request, league_id):
#         players = [p for p in Player.objects.all() if p.is_available(league_id=league_id)]
#         data = [
#             player.to_data() for player in players
#         ]
#         return data


# class MatchupsView(JSONView):

#     def get(self, request, league_id):
#         data = {}
#         today = date.today()
#         current_matchups = Matchup.objects.filter(league_id=league_id, start_date__lte=today, end_date__gte=today)

#         data['current'] = [
#             matchup.to_data() for matchup in current_matchups
#         ]
#         data['all'] = [
#             matchup.to_data() for matchup in Matchup.objects.filter(league_id=league_id).order_by('start_date')
#         ]
#         return data


# class TeamView(JSONView):

# 	def get(self, request, team_id):
# 		team = Team.objects.get(id=team_id)
# 		return team.to_data(player_data=True)

