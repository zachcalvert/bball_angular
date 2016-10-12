from django.contrib import admin

from players.models import Player


class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name', 'position', 'nba_team')


admin.site.register(Player, PlayerAdmin)