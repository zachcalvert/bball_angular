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
	roster_size = models.IntegerField(default=14)

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
		pl = sorted(players, key=lambda t: t.season_form)
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
	place = models.IntegerField(default=1)

	class Meta:
		ordering = ['-wins', 'losses']

	def __unicode__(self):
		return self.name

	@cached_property
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

	def average_weekly_score(self):
		scores = []
		eligible = self.matchups.filter(finalized=True)
		for e in eligible:
			if e.home_team == self:
				scores.append(e.home_points)
			else:
				scores.append(e.away_points)

		return round(sum(scores)/eligible.count(), 2)

	def to_data(self, player_data=False):
		data = {
			'id': self.id,
			'league_id': self.league.id,
			'name': self.name,
			'record': self.record,
			'current_matchup': self.current_matchup,
			'current_opponent': self.current_opponent,
			'average_weekly_score': self.average_weekly_score()
		}

		if player_data:
			data['players'] = [player.to_data() for player in self.players.all()]

		return data


class Draft(models.Model):
	league = models.ForeignKey(League)

	def snake(self, num_teams):
		# teams is list of team
	    while True:
	        for i in xrange(1,num_teams+1):
	            yield i
	        for i in xrange(num_teams,0,-1):
	            yield i

	def set_order(self):
		self.picks.all().delete()
		snake = self.snake(self.league.teams.count())
		draft_order = [snake.next() for _ in xrange(self.league.teams.count()*self.league.roster_size)]

		for count, i in enumerate(draft_order): 
			team = Team.objects.get(league=self.league, place=i)
			pick = DraftPick.objects.create(draft=self, team=team, number=count)


class DraftPick(models.Model):
	draft = models.ForeignKey(Draft, related_name='picks')
	number = models.IntegerField(default=1)
	team = models.ForeignKey(Team)
	player = models.ForeignKey('players.Player', null=True, blank=True)

	class Meta:
		ordering = ['number']
