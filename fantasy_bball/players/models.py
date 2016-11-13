from __future__ import unicode_literals, division

from datetime import date

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.query import QuerySet
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe


from leagues.models import League


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


def memoize(function):
	memo = {}
	def wrapper(*args):
		if args in memo:
			return memo[args]
		else:
			rv = function(*args)
			memo[args] = rv
			return rv
	return wrapper


class Player(models.Model):
	"""
	A simple model describing an NBA player that may be on one Team per League.
	"""
	# attributes
	name = models.CharField(max_length=35)
	position = models.CharField(u'Position', choices=POSITIONS, default='PG', max_length=15)
	nba_team = models.CharField(u'NBA Team', choices=NBA_TEAMS, default='FA', max_length=25)

	# notes
	roto_id = models.IntegerField(default=0)
	recent_notes = models.CharField(max_length=2000, default='No recent notes.')
	image_url = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		ordering = ['name']

	def __unicode__(self):
		return self.name

	@property
	def short_name(self):
		return "{0} {1} {2}".format(self.name, self.nba_team, self.position)

	def is_available(self, league_id):
		league = League.objects.get(id=league_id)
		for team in league.teams.all():
			if self in team.players.all():
				return False
		return True

	def notes(self):
		splits = self.recent_notes.split('date:')
		notes = []
		for i in range(len(splits)):
			if i == 0:
				continue
			else:
				note = splits[i]
				note = note.replace('\\u2019', "'")
				note = note.replace('\n', "")
				note = note.replace("\ ", "")
				try:
					note_date, note_report = note.split('report:')
					note_date = note_date[1:]
					note_report, note_impact = note.split('impact:')
					note_report = note_report[25:]
					note_impact = note_impact[1:]
				except ValueError:
					continue

				data =  {
					'date': note_date,
					'report': note_report,
					'impact': note_impact
				}
				notes.append(data)

				return notes

	@cached_property
	def stats(self, since_date=None):
		from schedule.models import Game, StatLine
		if not since_date:
			since_date = date(2016, 03, 10)

		data = {}
		games = Game.objects.filter(date__gt=since_date)
		statlines = StatLine.objects.filter(game__in=games, player_id=self.pk)
		gp = statlines.count() # games played
		
		try:
			pts = sum(sl.pts for sl in statlines)
			rebs = sum(sl.trbs for sl in statlines)
			asts = sum(sl.asts for sl in statlines)
			stls = sum(sl.stls for sl in statlines)
			blks = sum(sl.blks for sl in statlines)
			fgm = sum(sl.fgm for sl in statlines)
			fga = sum(sl.fga for sl in statlines)
			ftm = sum(sl.ftm for sl in statlines)
			fta = sum(sl.fta for sl in statlines)
			threesm = sum(sl.threesm for sl in statlines)
			threesa = sum(sl.threesa for sl in statlines)
			tos = sum(sl.tos for sl in statlines)

			data = {
				'totals': {
					'pts': pts,
					'rebs': rebs,
					'asts': asts,
					'stls': stls,
					'blks': blks,
					'fgm': fgm,
					'fga': fga,
					'ftm': ftm,
					'fta': fta,
					'threesm': threesm,
					'threesa': threesa,
					'tos': tos
				},
				'averages': {
					'pts': round(pts/gp, 2),
					'rebs': round(rebs/gp, 2),
					'asts': round(asts/gp, 2),
					'stls': round(stls/gp, 2),
					'blks': round(blks/gp, 2),
					'fgm': round(fgm/gp, 1),
					'fga': round(fga/gp, 1),
					'fgpct': "{0:.1f}%".format(fgm/fga * 100),
					'ftm': round(ftm/gp, 1),
					'fta': round(fta/gp, 1),
					'ftpct': "{0:.1f}%".format(ftm/fta * 100),
					'threesm': round(threesm/gp, 1),
					'threesa': round(threesa/gp, 1),
					'threespct': "{0:.1f}%".format(threesm/threesa * 100),
					'tos': round(tos/gp, 2)
				}
			}
		except ZeroDivisionError:
			pass

		return data

	@property
	def recent_form(self, num_games=25):
		from schedule.models import Game, StatLine
		statlines = list(StatLine.objects.filter(player_id=self.pk).order_by('-game__date')[:num_games])
		total = sum(statline.game_score for statline in statlines)
		return round(total/num_games, 2)

	def recent_games(self, num_games=20):
		from schedule.models import Game, StatLine

		statlines = list(StatLine.objects.filter(player_id=self.pk).order_by('-game__date')[:num_games])
		statlines.reverse()
		data = {
			'statlines': [
				statline.game_score for statline in statlines
			],
			'games': [
				statline.short_format for statline in statlines
			]
		}

		return data

	def to_data(self, league_id=None):
		data = {
			'id': self.id,
			'name': self.name,
			'position': self.position,
			'nba_team': self.nba_team,
		}

		if league_id is not None:
			data.update({
				'is_available': self.is_available(league_id=league_id)
				})

		return data



		