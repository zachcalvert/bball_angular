from rest_framework import viewsets 
 
from leagues.models import League, Team
from players.models import Player
from api.v1 import serializers


class LeagueViewSet(viewsets.ModelViewSet):  
    queryset = League.objects.all()
    serializer_class = serializers.LeagueSerializer


class TeamViewSet(viewsets.ModelViewSet):  
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):  
    queryset = Player.objects.all()
    serializer_class = serializers.PlayerSerializer