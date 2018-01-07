from django.contrib import admin

from players.models import Player, Quote


class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name', 'position', 'nba_team')


class QuoteAdmin(admin.ModelAdmin):
	list_display = ('person', 'year', 'content')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Quote, QuoteAdmin)