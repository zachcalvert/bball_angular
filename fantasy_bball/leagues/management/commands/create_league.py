from datetime import date, datetime
import random
from itertools import cycle

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core.management import call_command

from leagues.models import League, Team, Draft
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

		# sort players
		league = League.objects.create(name=name, manager=User.objects.first())
		players = [p for p in Player.objects.all() if p.is_available(league_id=league.id)]
		pl = sorted(players, key=lambda t: t.season_form)
		pl.reverse()
		
		# create teams
		for i in range(1, num_teams+1):
			town = random_item(towns)
			mascot = random_item(mascots)
			team = Team.objects.create(name="{0} {1}".format(town, mascot), league=league, place=i, owner=None)
			print('made team {}'.format(team.name))

		# create draft for league and set order (snake by default)
		draft = Draft.objects.create(league=league)
		draft.set_order()

		# draft!
		for count, pick in enumerate(draft.picks.all(), start=1):
			team = pick.team
			player = pl[count]
			team.players.add(player)
			pick.player = player
			pick.save()
			print("with pick number {0}, {1} selects {2}".format(count, team.name, player.name))

		print('made league {}'.format(league))

		# generate league schedule
		call_command('generate_matchups', league=league.name)
		call_command('update_team_records')

