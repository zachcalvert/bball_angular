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
		url = 'http://www.basketball-reference.com/leagues/NBA_2016_games.html'
		season = Season.objects.get(year='2015-16')
		r = requests.get(url)

		bs = BeautifulSoup(r.text)
		table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="games")
		rows = table.findAll(lambda tag: tag.name=='tr')

		for row in rows:
			cells = row.findAll('td')
			i = 0
			for cell in cells:
				value = cell.text
				if i == 0:
					value = value[5:]
					date = value.replace(',','')
					date_object = datetime.strptime(date, '%b %d %Y')
				elif i == 2:
					link = str(cell.a)
					boxscore_link = link[10:37]
				elif i == 3:
					link = str(cell.a)
					away_team = link[16:19]
				elif i == 4:
					if value:
						away_points = value
					else:
						away_points = 0
				elif i == 5:
					link = str(cell.a)
					home_team = link[16:19]
				elif i == 6:
					if value:
						home_points = value
					else:
						home_points = 0
				i += 1


			if row.find('td'):
				game = Game.objects.get_or_create(season=season, date=date_object,away_team=away_team, 
					away_points=away_points, home_team=home_team, home_points=home_points)
				print('Loaded game: {}'.format(game))

		now = datetime.now()
		today = now.date()

		games = Game.objects.all()

		for game in games:
			string = game.date.strftime('%m/%d/%Y')
			year = string[6:]
			day = string[3:5]
			month = string[:2]
			url = "boxscores/{0}{1}{2}0{3}.html".format(year, month, day, game.home_team)
			game.boxscore_link = url
			game.save()
			print("added boxcore_link for game: {}".format(game))
