from datetime import date, timedelta
from dateutil import rrule

from leagues.models import League, Team, Matchup

from django.core.management.base import BaseCommand


class Command(BaseCommand):
	"""
	Generates matchups between the teams in the league from season start to season end.
	"""

	def create_matchups_for_league(self, league):
		season_start = date(2016, 10, 25)
		season_end = date(2017, 4, 12)

		teams = list(Team.objects.filter(league=league))
		season = []

		if len(teams) % 2 == 1: teams = teams + ["BYE"]

		i = 1
		for dt in rrule.rrule(rrule.WEEKLY, dtstart=season_start, until=season_end):
			one_week = timedelta(days=6)
			end_date = dt + one_week


			mid = len(teams) / 2
			l1 = teams[:mid]
			l2 = teams[mid:]
			l2.reverse()    

			# Switch sides after each round
			if(i % 2 == 1):
				this_week = [ zip(l1, l2) ]
			else:
				this_week = [ zip(l2, l1) ]

			print("Week {0}: {1} - {2}".format(i, dt, end_date))
			for matchup in this_week[0]:
				home_team = matchup[0]
				away_team = matchup[1]
				print("Home - {0} vs. Away - {1}".format(home_team, away_team))
				Matchup.objects.create(league=league, home_team=home_team, away_team=away_team, 
					week=i, start_date=dt, end_date=end_date)
			print("")

			season = season + [ zip(l2, l1) ]

			teams.insert(1, teams.pop())
			i += 1


	def add_arguments(self, parser):
		parser.add_argument('--league', dest='league', default=None)

	def handle(self, *args, **options):

		league = options['league']

		if league:
			league = League.objects.get(name=league)
			self.create_matchups_for_league(league)

		else:
			for league in League.objects.all():
				self.create_matchups_for_league(league)
