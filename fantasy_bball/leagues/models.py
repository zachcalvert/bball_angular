from __future__ import unicode_literals, division

from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.functional import cached_property

STATS = (
	('pts', 'points'),
	('rebs', 'rebounds'),
	('asts', 'assists'),
	('stls', 'steals'),
	('blks', 'blocks'),
	('threesm', 'threesm'),
)


class League(models.Model):
	name = models.CharField(max_length=30)
	manager = models.ForeignKey(User)
	is_dynasty = models.BooleanField(default=False)
	is_public = models.BooleanField(default=True)
	max_teams = models.IntegerField(default=12)
	roster_size = models.IntegerField(default=12)

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
			'teams': [team.to_data(team_stats=True) for team in self.teams.all()]
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
	# needed_position = models.CharField(u'Position', choices='players.models.POSITIONS', default='PG', max_length=15)	

	class Meta:
		ordering = ['-wins', 'losses']

	def __unicode__(self):
		return self.name

	@property
	def record(self):
		return "{0}-{1}-{2}".format(self.wins, self.losses, self.ties)

	@property
	def needed_stat(self):
		pts = 15 - sum(player.stats["averages"]["pts"] for player in self.players.all())/self.players.count()
		rebs = 6 - sum(player.stats["averages"]["rebs"] for player in self.players.all())/self.players.count()
		asts = 3.5 - sum(player.stats["averages"]["asts"] for player in self.players.all())/self.players.count()
		stls = 1.1 - sum(player.stats["averages"]["stls"] for player in self.players.all())/self.players.count()
		blks = 1.1 - sum(player.stats["averages"]["blks"] for player in self.players.all())/self.players.count()
		threesm = 1.6 - sum(player.stats["averages"]["threesm"] for player in self.players.all())/self.players.count()

		x = ["pts", "rebs", "asts", "stls", "blks", "threesm"]
		avgs = [pts, rebs, asts, stls, blks, threesm]
		i = avgs.index(max(avgs))
		return x[i]

	@property
	def matchups(self):
		from leagues.models import Matchup
		return Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self))).order_by('week')

	@property
	def current_matchup(self):
		return self.matchups.filter(Q(start_date__lte=date.today()) & (Q(end_date__gte=date.today()))).first()

	@property
	def current_opponent(self):
		if self.current_matchup.home_team == self:
			return self.current_matchup.away_team
		else:
			return self.current_matchup.home_team.name

	@property
	def previous_matchup(self):
		return self.matchups.filter(week=self.current_matchup.week-1).first()

	@property
	def previous_opponent(self):
		if self.previous_matchup.home_team == self:
			return self.previous_matchup.away_team
		else:
			return self.previous_matchup.home_team.name

	def clean(self):
		if self.pk:
			for player in self.players.all():
				if Team.objects.filter(league=self.league).exclude(id=self.pk).filter(players__name=player.name):
					raise IntegrityError('%s is already on a team in this league: %s' % (player.name, self.name))

	@cached_property
	def season_totals(self):
		pts = 0
		asts = 0
		rebs = 0
		stls = 0
		blks = 0
		tos = 0
		fgm = 0
		fga = 0
		ftm = 0
		fta = 0
		threesm = 0
		threesa = 0

		for matchup in self.matchups:
			if matchup.home_team == self:
				pts += matchup.home_pts
				asts += matchup.home_asts
				rebs += matchup.home_rebs
				stls += matchup.home_stls
				blks += matchup.home_blks
				fgm += matchup.home_fgm
				fga += matchup.home_fga
				ftm += matchup.home_ftm
				fta += matchup.home_fta
				threesm += matchup.home_threesm
			else:
				pts += matchup.away_pts
				asts += matchup.away_asts
				rebs += matchup.away_rebs
				stls += matchup.away_stls
				blks += matchup.away_blks
				fgm += matchup.away_fgm
				fga += matchup.away_fga
				ftm += matchup.away_ftm
				fta += matchup.away_fta
				threesm += matchup.away_threesm

		return {
			"pts": pts,
			"asts": asts,
			"rebs": rebs,
			"stls": stls,
			"blks": blks,
			"tos": tos,
			"fgm": fgm,
			"fga": fga,
			"ftm": fta,
			"threesm": threesm,
			"fgpct": "{0:.1f}%".format(fgm/fga * 100),
			"ftpct":"{0:.1f}%".format(ftm/fta * 100)
		}

	def average_weekly_score(self):
		scores = []
		eligible = self.matchups.filter(finalized=True)
		for e in eligible:
			if e.home_team == self:
				scores.append(e.home_points)
			else:
				scores.append(e.away_points)

		return round(sum(scores)/eligible.count(), 2)

	def to_data(self, player_data=False, team_stats=False):
		data = {
			'id': self.id,
			'league_id': self.league.id,
			'name': self.name,
			'record': self.record,
			'current_matchup': self.current_matchup,
			'current_opponent': self.current_opponent,
			'previous_matchup': self.previous_matchup,
			'previous_opponent': self.previous_opponent,
			'average_weekly_score': self.average_weekly_score()
		}

		if player_data:
			data['players'] = [player.to_data() for player in self.players.all()]
		if team_stats:
			data['season_totals'] = self.season_totals

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
    
    home_fgm = models.IntegerField(default=0)
    home_fga = models.IntegerField(default=0)
    home_ftm = models.IntegerField(default=0)
    home_fta = models.IntegerField(default=0)
    home_threesm = models.IntegerField(default=0)
    home_pts = models.IntegerField(default=0)
    home_asts = models.IntegerField(default=0)
    home_rebs = models.IntegerField(default=0)
    home_stls = models.IntegerField(default=0)
    home_blks = models.IntegerField(default=0)
    home_tos = models.IntegerField(default=0)

    away_fgm = models.IntegerField(default=0)
    away_fga = models.IntegerField(default=0)
    away_ftm = models.IntegerField(default=0)
    away_fta = models.IntegerField(default=0)
    away_threesm = models.IntegerField(default=0)
    away_pts = models.IntegerField(default=0)
    away_asts = models.IntegerField(default=0)
    away_rebs = models.IntegerField(default=0)
    away_stls = models.IntegerField(default=0)
    away_blks = models.IntegerField(default=0)
    away_tos = models.IntegerField(default=0)

    def get_percentage(self, m, a):
    	try:
    		pct = round(m/a, 3)
    	except ZeroDivisionError:
    		pct = .00
    	return pct

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

    def away_data(self):
        away_data = {"totals": [], "players": []}
        for player in self.away_team.players.all():
        	sls = self.away_statlines.filter(player=player)
        	if sls.count() > 0:
				fgpct = self.get_percentage(sum(sl.fgm for sl in sls), sum(sl.fga for sl in sls))
				ftpct = self.get_percentage(sum(sl.ftm for sl in sls), sum(sl.fta for sl in sls))
				away_data["players"].append({
					"id": player.id,
					"name": player.name,
					"fgpct": fgpct,
					"ftpct": ftpct,
					"threesm": sum(sl.threesm for sl in sls),
					"pts": sum(sl.pts for sl in sls),
					"rebs": sum(sl.trbs for sl in sls),
					"asts": sum(sl.asts for sl in sls),
					"stls": sum(sl.stls for sl in sls),
					"blks": sum(sl.blks for sl in sls),
					"tos": sum(sl.tos for sl in sls)
				})

		team_fgpct = self.get_percentage(self.away_fgm, self.away_fga)
		team_ftpct = self.get_percentage(self.away_ftm, self.away_fta)
		away_data["totals"] = [{
			'name': 'totals',
			'fgpct': team_fgpct,
			'ftpct': team_ftpct,
			'threesm': self.away_threesm,
			'pts': self.away_pts,
			'rebs': self.away_rebs,
			'asts': self.away_asts,
			'stls': self.away_stls,
			'blks': self.away_blks,
			'tos': self.away_tos
		}]
        
        return away_data

    def home_data(self):
        home_data = {"totals": [], "players": []}
        for player in self.home_team.players.all():
        	sls = self.home_statlines.filter(player=player)
        	if sls.count() > 0:
				fgpct = self.get_percentage(sum(sl.fgm for sl in sls), sum(sl.fga for sl in sls))
				ftpct = self.get_percentage(sum(sl.ftm for sl in sls), sum(sl.fta for sl in sls))
				home_data["players"].append({
					"id": player.id,
					"name": player.name,
					"fgpct": fgpct,
					"ftpct": ftpct,
					"threesm": sum(sl.threesm for sl in sls),
					"pts": sum(sl.pts for sl in sls),
					"rebs": sum(sl.trbs for sl in sls),
					"asts": sum(sl.asts for sl in sls),
					"stls": sum(sl.stls for sl in sls),
					"blks": sum(sl.blks for sl in sls),
					"tos": sum(sl.tos for sl in sls)
				})

		team_fgpct = self.get_percentage(self.home_fgm, self.home_fga)
		team_ftpct = self.get_percentage(self.home_ftm, self.home_fta)
		home_data["totals"] = [{
			'name': 'totals',
			'fgpct': team_fgpct,
			'ftpct': team_ftpct,
			'threesm': self.home_threesm,
			'pts': self.home_pts,
			'rebs': self.home_rebs,
			'asts': self.home_asts,
			'stls': self.home_stls,
			'blks': self.home_blks,
			'tos': self.home_tos
		}]
        
        return home_data

    def to_data(self):
		data = {
			"league_id": self.league_id,
			"home": {
				"id": self.home_team.id,
				"name": self.home_team.name,
				"record": self.home_team.record,
				"data": self.home_data()
			},
			"away": {
				"id": self.away_team.id,
				"name": self.away_team.name,
				"record": self.away_team.record,
				"data": self.away_data()
			},
			"week": self.week,
			"start_date": self.start_date, 
			"end_date": self.end_date,
		}

		return data

    def update_score(self):
        self.away_pts = sum(sl.pts for sl in self.away_statlines)
        self.away_asts = sum(sl.asts for sl in self.away_statlines)
        self.away_rebs = sum(sl.trbs for sl in self.away_statlines)
        self.away_stls = sum(sl.stls for sl in self.away_statlines)
        self.away_blks = sum(sl.blks for sl in self.away_statlines)
        self.away_tos = sum(sl.tos for sl in self.away_statlines)
        self.away_fta = sum(sl.fta for sl in self.away_statlines)
        self.away_fgm = sum(sl.fgm for sl in self.away_statlines)
        self.away_fga = sum(sl.fga for sl in self.away_statlines)
        self.away_ftm = sum(sl.ftm for sl in self.away_statlines)
        self.away_fta = sum(sl.fta for sl in self.away_statlines)
        self.away_threesm = sum(sl.threesm for sl in self.away_statlines)

        self.home_pts = sum(sl.pts for sl in self.home_statlines)
        self.home_asts = sum(sl.asts for sl in self.home_statlines)
        self.home_rebs = sum(sl.trbs for sl in self.home_statlines)
        self.home_stls = sum(sl.stls for sl in self.home_statlines)
        self.home_blks = sum(sl.blks for sl in self.home_statlines)
        self.home_tos = sum(sl.tos for sl in self.home_statlines)
        self.home_fta = sum(sl.fta for sl in self.home_statlines)
        self.home_fgm = sum(sl.fgm for sl in self.home_statlines)
        self.home_fga = sum(sl.fga for sl in self.home_statlines)
        self.home_ftm = sum(sl.ftm for sl in self.home_statlines)
        self.home_fta = sum(sl.fta for sl in self.home_statlines)
        self.home_threesm = sum(sl.threesm for sl in self.home_statlines)

        for stat in ['pts', 'asts', 'rebs', 'stls', 'blks', 'tos', 'fgpct', 'ftpct', 'threesm']:
        	if stat == 'fgpct':
        		sls = self.away_statlines
        		away = round(sum(sl.fgm for sl in sls)/sum(sl.fga for sl in sls), 3)
        		sls = self.home_statlines
        		home = round(sum(sl.fgm for sl in sls)/sum(sl.fga for sl in sls), 3)
        	elif stat == 'ftpct':
        		sls = self.away_statlines
        		away = round(sum(sl.ftm for sl in sls)/sum(sl.fta for sl in sls), 3)
        		sls = self.home_statlines
        		home = round(sum(sl.ftm for sl in sls)/sum(sl.fta for sl in sls), 3)
	    	else:
	    		away = getattr(self, 'away_{}'.format(stat))
	    		home = getattr(self, 'home_{}'.format(stat))

	    	if home > away:
	    		self.home_team.wins += 1
	    		self.away_team.losses += 1
	    	elif home < away:
	    		self.home_team.losses += 1
	    		self.away_team.wins += 1
	    	else:
	    		self.home_team.ties += 1
	    		self.home_team.losses += 1

		self.away_team.save()
		self.home_team.save()

        if self.end_date <= date.today():
            self.finalized = True

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
		"""
		Set up the snake draft
		"""
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

