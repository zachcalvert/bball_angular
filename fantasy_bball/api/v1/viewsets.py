from rest_framework import viewsets
from rest_framework_extensions.mixins import ReadOnlyCacheResponseAndETAGMixin
 
from leagues.models import League, Team
from players.models import Player
from api.v1 import serializers


class LeagueViewSet(viewsets.ModelViewSet):  
    queryset = League.objects.all()
    serializer_class = serializers.LeagueSerializer


class TeamViewSet(viewsets.ModelViewSet):  
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all()
        league_id = self.request.query_params.get('league_id', None)

        if league_id:
            queryset = queryset.filter(league_id=league_id)

        return queryset
    

class PlayerViewSet(ReadOnlyCacheResponseAndETAGMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'list':
            return serializers.PlayerList
        if hasattr(self, 'action') and self.action == 'retrieve':
            return serializers.PlayerDetail
        return serializers.PlayerList


    def get_queryset(self):
        queryset = Player.objects.all()
        league_id = self.request.query_params.get('league_id', None)
        free_agents = self.request.query_params.get('free_agents', None)
        position = self.request.query_params.get('pos', None)
        team = self.request.query_params.get('team', None)

        if league_id:
            if free_agents:
                league = League.objects.get(id=league_id)
                fa_ids = league.free_agents
                queryset = queryset.filter(id__in=fa_ids)

        if position:
            queryset = queryset.filter(position=position)

        if team:
            queryset = queryset.filter(nba_team=team)

        return queryset
        