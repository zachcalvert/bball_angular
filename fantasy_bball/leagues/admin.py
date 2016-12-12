from django.contrib import admin

from leagues.models import League, Team 
from players.models import Player


class TeamInline(admin.TabularInline):
    model = Team
    extra = 0
    show_change_link = True
    readonly_fields = ['name', 'owner', 'record']

    def has_add_permission(self, request):
        return False


class AddTeamInline(admin.TabularInline):
    model = Team
    extra = 0
    show_change_link = True
    fields = ['name', 'owner']

    def has_change_permission(self, request, obj=None):
        return False


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 0
    readonly_fields = ('name', 'position', 'nba_team')

    fieldsets = [
        ('Players', {'fields': ['name', 'position', 'nba_team']}),
    ]


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'league', 'record')
    readonly_fields = ['record']
    filter_horizontal = ('players',)


class LeagueAdmin(admin.ModelAdmin):
	list_display = ('name', 'manager')
	inlines = [TeamInline, AddTeamInline]


admin.site.register(Team, TeamAdmin)
admin.site.register(League, LeagueAdmin)