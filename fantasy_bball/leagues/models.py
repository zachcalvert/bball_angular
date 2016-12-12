from __future__ import unicode_literals, division

from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.functional import cached_property


class League(models.Model):
	name = models.CharField(max_length=30)
	manager = models.ForeignKey(User)
	is_dynasty = models.BooleanField(default=False)
	is_public = models.BooleanField(default=True)
	max_teams = models.IntegerField(default=12)

	def __unicode__(self):
		return self.name

	@cached_property
	def free_agents(self):
		from players.models import Player
		return [p.id for p in Player.objects.all() if p.is_available(self.pk)]

	def get_teams(self):
		return [team.to_data() for team in Team.objects.filter(league=self)]

	def make_random_team(self, name="temp name", num_players=14, owner=None):
		from players.models import Player
		team = Team.objects.create(name=name, league=self, owner=None)
		i = 0
		players = [p for p in Player.objects.all() if p.is_available(league_id=self.pk)]
		pl = sorted(players, key=lambda t: t.recent_form)
		pl.reverse()

		for p in pl[i::10]:
			team.players.add(p)
			print('added {} to {}'.format(p, team))

			i += 1
			if i >= num_players:
				break

	def to_data(self):
		data = {
			'id': self.id,
			'name': self.name,
			'is_public': self.is_public,
			'dynasty': self.is_dynasty,
			'manager': self.manager.username,
			'teams': [team.to_data() for team in self.teams.all()]
		}

		return data


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

	@property
	def matchups(self):
		from schedule.models import Matchup
		return Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self))).order_by('week')

	@cached_property
	def current_matchup(self):
		from schedule.models import Matchup
		matchups = Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self))) 
		return matchups.filter(Q(start_date__lte=date.today()) & (Q(end_date__gte=date.today()))).first()

	@cached_property
	def current_opponent(self):
		if self.current_matchup.home_team == self:
			return self.current_matchup.away_team
		else:
			return self.current_matchup.home_team.name

	def clean(self):
		if self.pk:
			for player in self.players.all():
				if Team.objects.filter(league=self.league).exclude(id=self.pk).filter(players__name=player.name):
					raise IntegrityError('%s is already on a team in this league: %s' % (player.name, self.name))

	def get_players(self):
		from players.models import Player
		return [player.to_data() for player in Player.objects.filter(pk__in=self.players.all())]

	def to_data(self, player_data=False):
		current_matchup = self.current_matchup
		data = {
			'id': self.id,
			'league_id': self.league.id,
			'name': self.name,
			'record': self.record,
			'current_matchup': self.current_matchup,
			'current_opponent': self.current_opponent
		}

		if player_data:
			data['players'] = [player.to_data() for player in self.players.all()]

		return data
