from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.query import QuerySet

from applications.leagues.models import League


POSITIONS = (
	('PG', 'Point Guard'),
	('SG', 'Shooting Guard'),
	('SF', 'Small Forward'),
	('PF', 'Power Forward'),
	('C', 'Center'),
)

NBA_TEAMS = (
    ('ATL', 'Atlanta Hawks'),('BRK', 'Brooklyn Nets'),('BOS', 'Boston Celtics'),
    ('CHO', 'Charlotte Hornets'),('CHI', 'Chicago Bulls'),('CLE', 'Cleveland Cavaliers'),
    ('DAL', 'Dallas Mavericks'),('DEN', 'Denver Nuggets'),('DET', 'Detroit Pistons'),
    ('GSW', 'Golden State Warriors'),('HOU', 'Houston Rockets'),('IND', 'Indiana Pacers'),
    ('LAC', 'Los Angeles Clippers'),('LAL', 'Los Angeles Lakers'),('MEM', 'Memphis Grizzlies'),
    ('MIA', 'Miami Heat'),('MIN', 'Minnesota Timberwolves'),('MIL', 'Milwaukee Bucks'),
    ('NOP', 'New Orleans Pelicans'),('NYK', 'New York Knicks'),('OKC', 'Oklahoma City Thunder'),
    ('ORL', 'Orlando Magic'),('PHI', 'Philadelphia 76ers'),('PHO', 'Phoenix Suns'),
    ('POR', 'Portland TrailBlazers'),('SAS', 'San Antonio Spurs'),('SAC', 'Sacramento Kings'),
    ('TOR', 'Toronto Raptors'),('UTA', 'Utah Jazz'),('WAS', 'Washington Wizards'),
    ('FA', 'Free Agent'),
)


class Player(models.Model):
	"""
	A simple model describing an NBA player that may be on one Team per League.
	"""
	# attributes
	name = models.CharField(max_length=35)
	position = models.CharField(u'Position', choices=POSITIONS, default='PG', max_length=15)
	nba_team = models.CharField(u'NBA Team', choices=NBA_TEAMS, default='FA', max_length=25)

	# roto_id = models.IntegerField(default=0)
	# recent_notes = models.CharField(max_length=2000, default='No recent notes.')

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

	def is_available(self, league_id):
		league = League.objects.get(id=league_id)
		for team in league.teams.all():
			if self in team.players.all():
				return False
		return True

		