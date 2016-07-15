from rest_framework import viewsets 
 
from applications.leagues.models import League, Team
from applications.players.models import Player
from applications.api.v1 import serializers


class LeagueViewSet(viewsets.ModelViewSet):  
    queryset = League.objects.all()
    serializer_class = serializers.LeagueSerializer


class TeamViewSet(viewsets.ModelViewSet):  
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):  
    queryset = Player.objects.all()
    serializer_class = serializers.PlayerSerializer