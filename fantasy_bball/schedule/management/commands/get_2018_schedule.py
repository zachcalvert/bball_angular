import requests
from bs4 import BeautifulSoup
from datetime import datetime

from schedule.models import Season, Game

from django.core.management.base import BaseCommand


class Command(BaseCommand):
	"""
	Scrapes the basketball reference schedule page for dates, games and teams playing
	"""
	def handle(self, *args, **options):
		# get the content of rotoworld's nba player page
		months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']

		for month in months:
			url = 'http://www.basketball-reference.com/leagues/NBA_2018_games-{}.html'.format(month)
			season, created = Season.objects.get_or_create(year='2017-18')
			r = requests.get(url)

			bs = BeautifulSoup(r.text)
			table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="schedule")
			rows = table.findAll(lambda tag: tag.name=='tr')

			for row in rows:
				cells = row.findAll('td')
				for cell in cells:
					date = row.find('a').text
					date = date[5:]
					date = date.replace(',','')
					date_object = datetime.strptime(date, '%b %d %Y')

					if cell['data-stat'] == "box_score_text":
						link = str(cell.a)
						boxscore_link = link[10:37]

					elif cell['data-stat'] == "visitor_team_name":
						link = str(cell.a)
						away_team = link[16:19]

					elif cell['data-stat'] == "home_team_name":
						link = str(cell.a)
						home_team = link[16:19]

					elif cell['data-stat'] == "visitor_pts":
						away_points = cell.text or None

					elif cell['data-stat'] == "home_pts":
						home_points = cell.text or None


				if row.find('td'):
					game, created = Game.objects.get_or_create(season=season, date=date_object,
						away_team=away_team, home_team=home_team)
					if home_points:
						game.home_points=home_points
						game.away_points=away_points
						game.save()
					print('Loaded game: {}'.format(game))

		now = datetime.now()
		today = now.date()

		games = Game.objects.filter(boxscore_link__isnull=True)

		for game in games:
			string = game.date.strftime('%m/%d/%Y')
			year = string[6:]
			day = string[3:5]
			month = string[:2]
			url = "boxscores/{0}{1}{2}0{3}.html".format(year, month, day, game.home_team)
			game.boxscore_link = url
			game.save()
			print("added boxcore_link for game: {}".format(game))
