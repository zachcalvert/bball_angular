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
		from leagues.models import Matchup
		return Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self))).order_by('week')

	@cached_property
	def current_matchup(self):
		from leagues.models import Matchup
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


class Matchup(models.Model):
    league = models.ForeignKey(League, related_name='league')
    home_team = models.ForeignKey(Team, related_name='home')
    away_team = models.ForeignKey(Team, related_name='away')
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    week = models.IntegerField(default=22)
    finalized = models.BooleanField(default=False)
    home_points = models.FloatField(default=0.0)
    away_points = models.FloatField(default=0.0)
    result = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return "matchup between: {0} and {1} starting {2}".format(self.home_team, self.away_team, self.start_date)

    def to_data(self):
        return {
            "league_id": self.league_id,
            "home": {
                "id": self.home_team.id,
                "name": self.home_team.name,
                "points": self.home_points,
                "players": self.home_data()
                },
            "away": {
                "id": self.away_team.id,
                "name": self.away_team.name,
                "points": self.away_points,
                "players": self.away_data()
                },
            "week": self.week,
            "start_date": self.start_date, 
            "end_date": self.end_date,

        }
        if self.finalized:
            data["result"] = self.result

    @cached_property
    def home_statlines(self):
    	from schedule.models import StatLine
        return StatLine.objects.filter(player__in=self.home_team.players.all(), 
            game__date__gte=self.start_date, game__date__lte=self.end_date)

    @cached_property
    def away_statlines(self):
    	from schedule.models import StatLine
        return StatLine.objects.filter(player__in=self.away_team.players.all(), 
            game__date__gte=self.start_date, game__date__lte=self.end_date)

    def home_data(self):
        data = {}
        for player in self.home_team.players.all():
            player_total = sum(sl.game_score for sl in self.home_statlines.filter(player=player))
            data[player.id] = [player.name, player_total]

        return data

    def away_data(self):
        data = {}
        for player in self.away_team.players.all():
            player_total = sum(sl.game_score for sl in self.away_statlines.filter(player=player))
            data[player.id] = [player.name, player_total]

        return data

    def update_score(self):
        self.home_points = sum(sl.game_score for sl in self.home_statlines)
        self.away_points = sum(sl.game_score for sl in self.away_statlines)

        if self.end_date <= date.today():
            self.finalized = True
            if self.home_points > self.away_points:
                self.home_team.wins += 1
                self.away_team.losses += 1
            elif self.home_points < self.away_points:
                self.home_team.losses += 1    
                self.away_team.wins += 1
            else:
                self.home_team.ties += 1
                self.away_team.ties += 1

            self.away_team.save()
            self.home_team.save()

            print('saved {0} with new record {1}'.format(self.home_team, self.home_team.record))

        self.save()


class Draft(models.Model):
	league = models.ForeignKey(League)

	def snake(self, num_teams):
	    while True:
	        for i in xrange(1,num_teams+1):
	            yield i
	        for i in xrange(num_teams,0,-1):
	            yield i

	def set_order(self):
		self.picks.all().delete()
		snake = self.snake(self.league.teams.count())
		draft_order = [snake.next() for _ in xrange(self.league.teams.count()*self.league.roster_size)]

		draft_round = 0
		for count, i in enumerate(draft_order, start=1): 
			if self.picks.count() % self.league.teams.count() == 0:
				draft_round += 1
			team = Team.objects.get(league=self.league, place=i)
			pick = DraftPick.objects.create(draft=self, team=team, number=count, draft_round=draft_round)

	def to_data(self):
		i = 1
		data = []
		while i <= self.league.roster_size:
			data.append([{
				"pick": pick.number, 
				"player": {
					"id": pick.player.id,
					"name": pick.player.short_name,
					"nba_team": pick.player.nba_team,
					"position": pick.player.position
				},
				"team": { 
					"id": pick.team.id,
					"name": pick.team.name
				}, 
				"round": pick.draft_round 
			} for pick in self.picks.filter(draft_round=i)])
			i += 1

		return data
		

class DraftPick(models.Model):
	draft = models.ForeignKey(Draft, related_name='picks')
	number = models.IntegerField(default=1)
	team = models.ForeignKey(Team)
	player = models.ForeignKey('players.Player', null=True, blank=True)
	draft_round = models.IntegerField(default=1)

	class Meta:
		ordering = ['number']

