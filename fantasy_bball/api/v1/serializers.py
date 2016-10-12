from rest_framework.serializers import ModelSerializer  
from leagues.models import League, Team
from players.models import Player


class LeagueSerializer(ModelSerializer):

    class Meta:
        model = League

class TeamSerializer(ModelSerializer):

    class Meta:
        model = Team


class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player