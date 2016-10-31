from rest_framework.serializers import ModelSerializer, ReadOnlyField  
from leagues.models import League, Team
from players.models import Player


class LeagueSerializer(ModelSerializer):
	teams = ReadOnlyField(source='get_teams')

	class Meta:
		model = League
		fields = ('id', 'name', 'manager', 'is_public', 'teams')


class TeamSerializer(ModelSerializer):
	players = ReadOnlyField(source='get_players')

	class Meta:
		model = Team
		fields = ('id', 'name', 'record', 'league', 'owner', 'players')


class PlayerSerializer(ModelSerializer):

	class Meta:
		model = Player
		fields = ('id', 'name', 'image_url', 'position', 'nba_team', 'notes', 'stats')