from datetime import date

from leagues.models import Team, League, Matchup

from django.core.management.base import BaseCommand


class Command(BaseCommand):
	"""
	Updates team records based on matchups that have already taken place.
	"""
	def update_records_for_league(self, league):
		season_start = date(2016, 10, 25)
		today = date.today()
		teams = Team.objects.filter(league=league)

		for team in teams:
			team.wins = 0
			team.losses = 0
			team.ties = 0
			team.save()
		
		for matchup in Matchup.objects.filter(start_date__gte=season_start, end_date__lte=today, home_team__in=teams):
			matchup.update_score()

	def add_arguments(self, parser):
		parser.add_argument('--league', dest='league', default=None)

	def handle(self, *args, **options):
		league = options['league']

		if league:
			league = League.objects.get(name=league)
			self.update_records_for_league(league)

		else:
			for league in League.objects.all():
				self.update_records_for_league(league)

			



