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
		manager = User.objects.create_user(username="{0} manager".format(name), password='manager', email="m@m.com")
		league = League.objects.create(name=name, manager=manager, roster_size=num_players)
		players = [p for p in Player.objects.all() if p.is_available(league_id=league.id)]
		pl = sorted(players, key=lambda t: t.season_form)
		pl.reverse()
		pl = [0] + pl
		
		# create teams
		for i in range(1, num_teams+1):
			town = random_item(towns)
			mascot = random_item(mascots)
			team = Team.objects.create(name="{0} {1}".format(town, mascot), league=league, place=i, owner=None)
			print('made team {}'.format(team.name))

		# create draft for league and set order (snake by default)
		draft = Draft.objects.create(league=league)
		draft.set_order()

		stat = None
		# draft
		for count, pick in enumerate(draft.picks.all(), start=1):
			team = pick.team
			index = count
			# if count > 3 * num_teams:
			# 	# start in 3rd round
			# 	stat = team.needed_stat
			# 	eligible = pl[1:count+10]
			# 	ranked = sorted(eligible, key=lambda x: x.stats["averages"][stat], reverse=True)
			# 	import pdb
			# 	pdb.set_trace()
			# 	best_player = ranked[0]
			# 	index = pl.index(best_player)

			player = pl[index]
			team.players.add(player)
			pick.player = player
			pick.save()
			if stat is not None:
				print("\nThe {0} need {1}".format(team, stat))
			print("Pick {0}: the {1} select {2} {3}".format(count, team.name, player.name, player.season_form))

		print('made league {}'.format(league))

		# generate league schedule
		call_command('generate_matchups', league=league.name)
		call_command('update_team_records', league=league.name)

