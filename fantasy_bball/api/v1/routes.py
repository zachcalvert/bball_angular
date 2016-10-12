from rest_framework import routers  
from api.v1 import viewsets


api_router = routers.SimpleRouter()  
api_router.register('leagues', viewsets.LeagueViewSet)
api_router.register('teams', viewsets.TeamViewSet)    
api_router.register('players', viewsets.PlayerViewSet)  