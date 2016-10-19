from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class League(models.Model):
	name = models.CharField(max_length=30)
	manager = models.ForeignKey(User)
	is_dynasty = models.BooleanField(default=False)
	is_public = models.BooleanField(default=True)
	max_teams = models.IntegerField(default=12)

	def __unicode__(self):
		return self.name

	def get_teams(self):
		return [team.to_data() for team in Team.objects.filter(league=self)]


class Team(models.Model):
	league = models.ForeignKey(League, related_name='teams')
	name = models.CharField(max_length=30, default='Team')
	owner = models.ForeignKey(User, null=True, related_name='teams')
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	ties = models.IntegerField(default=0)
	players = models.ManyToManyField('players.Player', blank=True, related_name='teams')

	class Meta:
		ordering = ['-wins', 'losses']

	def __unicode__(self):
		return self.name

	@property
	def record(self):
		return "{0}-{1}-{2}".format(self.wins, self.losses, self.ties)

	def clean(self):
		for player in self.players.all():
			if Team.objects.filter(league=self.league).exclude(id=self.pk).filter(players__name=player.name):
				raise IntegrityError('%s is already on a team in this league: %s' % (player.name, self.name))

	def to_data(self):
		data = {
			'id': self.id,
			'league': {
				'id': self.league.id,
				'name': self.league.name,
			},
			'name': self.name,
			'record': self.record,
			'players': [{
				'id': player.id,
				'name': player.name,
				'position': player.position,
				'team': player.nba_team,
			} for player in self.players.all()]
		}
		if self.owner:
			data.update({'owner': self.owner.username})

		return data
