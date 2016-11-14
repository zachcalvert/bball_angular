from leagues.views import JSONView
from players.models import Player


class PlayersView(JSONView):

	def get(self, request):
		data = [player.to_data() for player in Player.objects.all()]
		return data


class PlayerView(JSONView):

	def get(self, request, player_id):
		player = Player.objects.get(id=player_id)
		return player.to_data(details=True)

