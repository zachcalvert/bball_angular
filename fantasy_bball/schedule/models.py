from __future__ import unicode_literals, division

from django.db import models

from leagues.models import League, Team
from leagues.utils import random_item
from players.models import NBA_TEAMS, Player
from schedule.texts.stats import points, assists, rebounds, blocks, steals


NBA_SEASONS = (
	('2014-15', '2014-15'),
	('2015-16', '2015-16'),
	('2016-17', '2016-17'),
)


class Season(models.Model):
    year = models.CharField(u'Season', choices=NBA_SEASONS, default='2015-16', max_length=10)

    def __unicode__(self):
        return "{}".format(self.year)


class Game(models.Model):
    season = models.ForeignKey(Season)
    date = models.DateField(auto_now=False)
    tipoff = models.CharField(max_length=8, null=True, blank=True)
    home_team = models.CharField(u'Home Team', max_length=25, choices=NBA_TEAMS)
    away_team = models.CharField(u'Away Team', max_length=25, choices=NBA_TEAMS)
    home_points = models.IntegerField(null=True)
    away_points = models.IntegerField(null=True)
    boxscore_link = models.URLField(max_length=255, null=True, blank=True)
    statlines = models.ForeignKey('StatLine', null=True, blank=True, related_name='game_stats')

    @property
    def result(self):
        return ("{0} {1}-{2} {3}".format(self.away_team, self.away_points, self.home_points, self.home_team))

    def __unicode__(self):
        return "{0}: {1} @ {2}".format(self.date, self.away_team, self.home_team)

    @property
    def full_home_name(self):
        return dict(NBA_TEAMS).get(self.home_team)

    @property
    def full_away_name(self):
        return dict(NBA_TEAMS).get(self.away_team)

    @property
    def home_statlines(self):
        return self.sls.filter(player__nba_team=self.home_team)

    @property
    def away_statlines(self):
        return self.sls.filter(player__nba_team=self.away_team)


class StatLine(models.Model):
    game = models.ForeignKey(Game, db_index=True, related_name='sls')
    player = models.ForeignKey(Player, db_index=True)
    mp = models.CharField(max_length=5, null=True, blank=True)
    fgm = models.IntegerField(default=0)
    fga = models.IntegerField(default=0)
    ftm = models.IntegerField(default=0)
    fta = models.IntegerField(default=0)
    threesm = models.IntegerField(default=0)
    threesa = models.IntegerField(default=0)
    orbs = models.IntegerField(default=0)
    drbs = models.IntegerField(default=0)
    trbs = models.IntegerField(default=0)
    asts = models.IntegerField(default=0)
    stls = models.IntegerField(default=0)
    blks = models.IntegerField(default=0)
    tos = models.IntegerField(default=0)
    pfs = models.IntegerField(default=0)
    pts = models.IntegerField(default=0)
    dank = models.BooleanField(default=False)
    added_to_player = models.BooleanField(default=False)

    def to_data(self):
        return {
            "id": self.id,
            "game_result": self.game.result,
            "game_name": self.short_format,
            "player": self.player.to_data(quick_stats=False),
            "game_score": self.game_score,
            "mp": self.mp,
            "fgm": self.fgm,
            "fga": self.fga,
            "ftm": self.ftm,
            "fta": self.fta,
            "threesm": self.threesm,
            "threesa": self.threesa,
            "rebs": self.trbs,
            "asts": self.asts,
            "stls": self.stls,
            "blks": self.blks,
            "tos": self.tos,
            "pts": self.pts,
            "game": self.game
        }

    @property
    def game_score(self):
        """
        Out of 10. Combines stat totals relative to shot efficiency and turnovers.
        This is not PER or anything like that, this is an evaluation purely from a 
        fantasy basketball perspective.
        """
        base = 4.0
        base += self.fgm *.22 # 45% shooter comes out even
        base -= self.fga * .1
        base += self.ftm * .13 # 77% free throw shooter comes out even
        base -= self.fta * .1
        base += self.threesm * .2

        base += self.trbs * .13
        base += self.asts * .16
        base += self.stls * .285
        base += self.blks * .27
        base -= self.tos * .2
        base += (self.pts / 10) *.3 # for every 10 pts, +0.3

        if base > 11: # we need to know when players have a game this good
            self.dank=True
            self.save()

        if base > 10:
            base = 10.0

        return round(base, 2)

    @property
    def short_format(self):
        """
        Concise representation of the game this took place in, relative to this statline's player's team
        """
        away = False
        if self.game.away_team == self.player.nba_team:
            opp = self.game.home_team
            away = True
        else:
            opp = "@{}".format(self.game.away_team)

        date = self.game.date.strftime('%-m/%-d')
        return "{0} {1}".format(opp, date)

    def to_text(self):
        points_verb = random_item(points.verbs)
        rebounds_verb = random_item(rebounds.verbs)
        return "{0} {1} {2} points against the {3} and {4} {5} rebounds.".format(self.player.name, points_verb, self.pts, self.game.full_home_name, rebounds_verb, self.trbs)

class Matchup(models.Model):
    league = models.ForeignKey(League)
    home_team = models.ForeignKey(Team, related_name='home_team')
    away_team = models.ForeignKey(Team, related_name='away_team')
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    week = models.IntegerField(default=22)
    finalized = models.BooleanField(default=False)
    result = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return "matchup between: {0} and {1} starting {2}".format(self.home_team, self.away_team, self.start_date)

    def to_data(self):
        return {
            "league_id": self.league_id,
            "home_id": self.home_team.id,
            "home_team": self.home_team.name,
            "away_id": self.away_team.id,
            "away_team": self.away_team.name,
            "week": self.week,
            "start_date": self.start_date, 
            "end_date": self.end_date

        }
        if self.finalized:
            data["result"] = self.result

    # @property
    # def home_totals(self):
    #     home_stats = teams.utils.calculate_team_totals(self.home_team, start_day=self.start_date, end_day=self.end_date)
    #     home_totals = home_stats.pop('totals')
    #     return home_totals

    # @property
    # def away_totals(self):
    #     away_stats = teams.utils.calculate_team_totals(self.away_team, start_day=self.start_date, end_day=self.end_date)
    #     away_totals = away_stats.pop('totals')
    #     return away_totals
