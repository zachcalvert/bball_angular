from django.views.generic import View, TemplateView

from schedule.models import Season, Game


class SeasonView(TemplateView):
	template_name = 'season.html'

	def get_context_data(self, season_id, *args, **kwargs):
		context = super(SeasonView, self).get_context_data(*args, **kwargs)
		season = Season.objects.get(id=season_id)
		context["season"] = season
		return context


class GameView(TemplateView):
	template_name = 'game.html'

	def get_context_data(self, season_id, game_id, *args, **kwargs):
		context = super(GameView, self).get_context_data(*args, **kwargs)
		game = Game.objects.get(id=game_id)
		context["game_day"] = game.date.strftime("%A, %B %-d")
		context["game"] = game
		return context
