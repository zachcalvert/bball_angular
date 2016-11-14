import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta

from schedule.models import Season, Game, StatLine
from players.models import Player

from django.core.management.base import BaseCommand

ROOT_URL = 'http://www.basketball-reference.com/'

class Command(BaseCommand):
	"""
	Scrapes the box scores on basketball reference and loads the relevant stats 
	for use in the app
	"""
	def handle(self, *args, **options):
		# can't get the boxscore for a game that hasn't yet been played
		today = datetime.today()
		season = Season.objects.last()
		games = Game.objects.filter(season=season, date__lt=today)

		for game in games:
			print("about to load stats for game: {}".format(game))
			# don't add game stats twice
			sls = StatLine.objects.filter(game_id=game.id)
			if sls.count() > 0:
				continue

			url = "{0}{1}".format(ROOT_URL, game.boxscore_link)
			r = requests.get(url)
			bs = BeautifulSoup(r.text)
			away_table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="box_{}_basic".format(game.away_team.lower()))
			try:
				away_rows = away_table.findAll(lambda tag: tag.name=='tr')
			except Exception:
				continue

			for row in away_rows:
				name = row.find('th')

				try:
					player_name = name['csk']
					last_name, first_name = player_name.split(',')
					full_name = "{0} {1}".format(first_name, last_name)
					player, created = Player.objects.get_or_create(name=full_name)
					player.nba_team = game.away_team
					player.save()
				except Exception:
					continue

				if StatLine.objects.filter(player=player, game=game).exists():
					continue

				try:
					cells = row.findAll('td')
				except Exception:
					continue
				for cell in cells:
					if cell.text == 'Did Not Play' or cell.text == 'Player Suspended':
						continue

					if cell['data-stat'] == "mp":
						mp = cell.text
					elif cell['data-stat'] == "fg":
						fgm = cell.text
					elif cell['data-stat'] == "fga":
						fga = cell.text
					elif cell['data-stat'] == "fg3":
						threesm = cell.text
					elif cell['data-stat'] == "fg3a":
						threesa = cell.text
					elif cell['data-stat'] == "ft":
						ftm = cell.text
					elif cell['data-stat'] == "fta":
						fta = cell.text
					elif cell['data-stat'] == "orb":
						orbs = cell.text
					elif cell['data-stat'] == "drb":
						drbs = cell.text
					elif cell['data-stat'] == "trb":
						trbs = cell.text
					elif cell['data-stat'] == "ast":
						asts = cell.text
					elif cell['data-stat'] == "stl":
						stls = cell.text
					elif cell['data-stat'] == "blk":
						blks = cell.text
					elif cell['data-stat'] == "tov":
						tos = cell.text
					elif cell['data-stat'] == "pf":
						pfs = cell.text
					elif cell['data-stat'] == "pts":
						pts = cell.text

				away_statline = StatLine.objects.create(game=game, player=player,
					mp=mp, fgm=fgm, fga=fga,ftm=ftm, fta=fta, threesm=threesm, threesa=threesa,
					orbs=orbs, drbs=drbs, trbs=trbs, asts=asts, stls=stls, blks=blks, tos=tos,
					pfs=pfs,pts=pts)
				# TODO: update the Game instance with the final score
				print('Loaded statline for {0} in game {1}'.format(player.name, game))


			home_table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="box_{}_basic".format(game.home_team.lower()))
			try:
				home_rows = home_table.findAll(lambda tag: tag.name=='tr')
			except Exception:
				continue

			for row in home_rows:
				name = row.find('th')

				try:
					player_name = name['csk']
					last_name, first_name = player_name.split(',')
					full_name = "{0} {1}".format(first_name, last_name)
					player, created = Player.objects.get_or_create(name=full_name)
					player.nba_team = game.home_team
					player.save()
				except Exception:
					continue

				if StatLine.objects.filter(player=player, game=game).exists():
					continue

				try:
					cells = row.findAll('td')
				except Exception:
					continue
				for cell in cells:
					if cell.text == 'Did Not Play' or cell.text == 'Player Suspended':
						continue

					if cell['data-stat'] == "mp":
						mp = cell.text
					elif cell['data-stat'] == "fg":
						fgm = cell.text
					elif cell['data-stat'] == "fga":
						fga = cell.text
					elif cell['data-stat'] == "fg3":
						threesm = cell.text
					elif cell['data-stat'] == "fg3a":
						threesa = cell.text
					elif cell['data-stat'] == "ft":
						ftm = cell.text
					elif cell['data-stat'] == "fta":
						fta = cell.text
					elif cell['data-stat'] == "orb":
						orbs = cell.text
					elif cell['data-stat'] == "drb":
						drbs = cell.text
					elif cell['data-stat'] == "trb":
						trbs = cell.text
					elif cell['data-stat'] == "ast":
						asts = cell.text
					elif cell['data-stat'] == "stl":
						stls = cell.text
					elif cell['data-stat'] == "blk":
						blks = cell.text
					elif cell['data-stat'] == "tov":
						tos = cell.text
					elif cell['data-stat'] == "pf":
						pfs = cell.text
					elif cell['data-stat'] == "pts":
						pts = cell.text

				home_statline = StatLine.objects.create(game=game, player=player,
					mp=mp, fgm=fgm, fga=fga,ftm=ftm, fta=fta, threesm=threesm, threesa=threesa,
					orbs=orbs, drbs=drbs, trbs=trbs, asts=asts, stls=stls, blks=blks, tos=tos,
					pfs=pfs,pts=pts)
				# TODO: update the Game instance with the final score
				print('Loaded statline for {0} in game {1}'.format(player.name, game))





