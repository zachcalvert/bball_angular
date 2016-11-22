from datetime import date, timedelta
from dateutil import rrule

from schedule.models import Matchup
from leagues.models import League, Team

from django.core.management.base import BaseCommand


def find_next_opponent(date, opponents):
	"""
	opponents is a list of teams
	date represents the start date of the given matchup
	"""
	for opponent in opponents:
		try:
			print("does {0} have a matchup this week?".format(opponent))
			matchup = opponent.matchups.get(start_date=date)
		except Matchup.DoesNotExist:
			print("{0} does not have a matchup this week, they should play".format(opponent))
			return opponent

		print("{0} does have a matchup this week, moving on".format(opponent))
		continue


class Command(BaseCommand):
	"""
	Generates matchups between the teams in the league from season start to season end.
	"""
	def handle(self, *args, **options):
		
		season_start = date(2016, 10, 25)
		season_end = date(2017, 4, 12)


		for league in League.objects.all():

			for team in Team.objects.filter(league=league):
				
				z = 1
				for dt in rrule.rrule(rrule.WEEKLY, dtstart=season_start, until=season_end):
					print('week {}'.format(dt))
					one_week = timedelta(days=6)
					end_date = dt + one_week

					try:
						matchup = team.matchups.get(start_date=dt)
					
					# if the team isn't playing
					except Matchup.DoesNotExist:
						print("no matchup scheduled for {0} yet, let's set one up".format(team))
						# sort by teams that have played this team the least
						opponents = sorted(Team.objects.all().exclude(name=team.name), key=lambda t: t.matchups.filter(home_team=team).count())
						opponent = find_next_opponent(dt, opponents)
						home = team
						away = opponent
						matchup = Matchup.objects.create(league=league, home_team=home, away_team=away, start_date=dt, end_date=end_date, week=z)

						print('created matchup between {0} and {1}'.format(home, away))

					print("{0} already has a matchup this week, onto next week!".format(team))
					z += 1
					continue
				continue
	
		# matchups = Matchup.objects.filter(start_date=datetime(2014, 10, 27))
		# for matchup in matchups:
		# 	matchup.start_date = datetime(2014, 10, 28)
		# 	matchup.save()

