from datetime import date, datetime
import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from leagues.models import League
from leagues.texts.teams.mascots import mascots
from leagues.texts.teams.towns import towns
from leagues.utils import random_item

from players.models import Player


class Command(BaseCommand):
	"""
	Create a new league, default 12 teams and 14 players per team
	"""
	def add_arguments(self, parser):
		parser.add_argument('name')
		parser.add_argument('num_teams')
		parser.add_argument('num_players')

	def handle(self, *args, **options):
		name = options['name']
		num_teams = int(options['num_teams'])
		num_players = int(options['num_players'])

		league = League.objects.create(name=name, manager=User.objects.first())

		for i in range(num_teams):
			town = random_item(towns)
			mascot = random_item(mascots)
			team = league.make_random_team(name='{0} {1}'.format(town, mascot), num_players=num_players)
			print('made team {}'.format(team))

		print('made league {}'.format(league))
