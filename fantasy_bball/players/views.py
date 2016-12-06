from leagues.views import BDLView

from players.models import Player, Quote

class PlayerView(BDLView):
    template_name = "player.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PlayerView, self).get_context_data(*args, **kwargs)
        player = Player.objects.get(id=kwargs['player_id'])
        player_data = player.to_data(full_stats=True)

        context["player_data"] = player_data
        return context