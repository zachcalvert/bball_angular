import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from players.models import Player


class Command(BaseCommand):
    """
    This has a running time of over 20 minutes, preferable to load the .sql file which contains the respective ids.
    Gets the ids of players to fetch their notes. Brute forces the rotoworld urls since they are formatted with ids
    """
    def handle(self, *args, **options):
        i = 2850
        while i < 2890:
            url = 'http://www.rotoworld.com/player/nba/{}/'.format(i)
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
            playername = soup.find_all('div', class_='playername')

            name = (str(playername))
            name = name[29:]
            name = name.split('|')
            name = (name[0])
            name = name[:-1]

            print("trying to find player: {}.".format(name))
            try:
                player = Player.objects.get(name=name)
                print("found")
            except Player.DoesNotExist:
                print("Not playing anymore")
                i += 1
                continue

            if i < 800:
                player.retired = True

            player.roto_id = i
            player.save()
            print("saved {0} with roto_id {1}".format(player.name, i))
            i += 1