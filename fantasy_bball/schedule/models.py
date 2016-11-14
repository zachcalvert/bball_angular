from __future__ import unicode_literals, division

from django.db import models

from players.models import NBA_TEAMS, Player


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
    statlines = models.ManyToManyField('players.Player', through="StatLine")

    @property
    def result(self):
        return ("{0} {1}-{2} {3}".format(self.away_team, self.away_points, self.home_points, self.home_team))

    def __unicode__(self):
        return "{0}: {1} @ {2}".format(self.date, self.away_team, self.home_team)


class StatLine(models.Model):
    game = models.ForeignKey(Game, db_index=True)
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
    added_to_player = models.BooleanField(default=False)

    def __unicode__(self):
        return "{0} - {1}".format(self.player, self.game)

    def to_data(self):
        return {
            "game": self.game.result,
            "player": self.player.to_data(),
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
            "pts": self.pts
        }

    @property
    def game_score(self):
        """
        Out of 10. Combines stat totals relative to shot efficiency and turnovers.
        This is not PER or anything like that, this is an evaluation purely from a 
        fantasy basketball perspective.
        """
        base = 5.0

        base += self.fgm *.235 # 43% shooter comes out even
        base -= self.fga * .1

        base += self.ftm * .13 # 77% free throw shooter comes out even
        base -= self.fta * .1

        base += self.threesm * .2

        base += self.trbs * .13
        base += self.asts * .16
        base += self.stls * .3
        base += self.blks * .3
        base -= self.tos * .2

        base += (self.pts / 10) *.3 # for every 10 pts, +0.3

        # if base > 10: # hasn't even happened in 2016
        #     base = 10

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
