from rest_framework.serializers import ModelSerializer  
from applications.leagues.models import League, Team
from applications.players.models import Player


class LeagueSerializer(ModelSerializer):

    class Meta:
        model = League

class TeamSerializer(ModelSerializer):

    class Meta:
        model = Team


class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player