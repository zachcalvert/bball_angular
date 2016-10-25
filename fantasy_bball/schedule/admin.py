from django.contrib import admin

from schedule.models import Season, Game, StatLine

class StatLineInline(admin.TabularInline):
    model = StatLine
    extra = 0
    readonly_fields = ['mp', 'pts', 'trbs', 'asts', 'stls', 'blks', 'fgm', 'fga', 'ftm', 'fta', 'threesm', 'threesa', 'tos']
    exclude = ['player', 'orbs', 'drbs', 'pfs', 'added_to_player',]
    can_delete = False


class GameInline(admin.TabularInline):
    model = Game
    extra = 0
    show_change_link = True
    readonly_fields = ['date', 'home_team', 'home_points', 'away_points', 'away_team']
    exclude = ['tipoff', 'boxscore_link', 'statlines']
    can_delete = False


class GameAdmin(admin.ModelAdmin):
    readonly_fields = ('season', 'date', 'result')
    exclude = ['home_team', 'away_team', 'home_points', 'away_points', 'tipoff', 'statlines', 'boxscore_link']
    list_display = ('date', 'home_team', 'home_points', 'away_points', 'away_team')

    inlines = [StatLineInline,]


class SeasonAdmin(admin.ModelAdmin):
	list_display = ('year',)
	inlines = [GameInline,]


admin.site.register(Game, GameAdmin)
admin.site.register(Season, SeasonAdmin)