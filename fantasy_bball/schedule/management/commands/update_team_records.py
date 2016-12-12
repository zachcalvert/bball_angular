from datetime import date

from schedule.models import Matchup
from leagues.models import Team

from django.core.management.base import BaseCommand


class Command(BaseCommand):
	"""
	Updates team records based on matchups that have already taken place.
	"""
	def handle(self, *args, **options):
		season_start = date(2016, 10, 25)
		today = date.today()

		for team in Team.objects.all():
			team.wins = 0
			team.losses = 0
			team.ties = 0
			team.save()
		
		for matchup in Matchup.objects.filter(start_date__gte=season_start, end_date__lt=today):
			matchup.update_score()

			



