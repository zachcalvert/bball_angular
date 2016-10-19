from rest_framework.serializers import ModelSerializer, ReadOnlyField  
from leagues.models import League, Team
from players.models import Player


class LeagueSerializer(ModelSerializer):
	teams = ReadOnlyField(source='get_teams')

	class Meta:
		model = League
		fields = ('id', 'name', 'manager', 'is_public', 'teams')

class TeamSerializer(ModelSerializer):

    class Meta:
        model = Team


class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player