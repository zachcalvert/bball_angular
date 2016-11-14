from django.conf.urls import url, include
from django.views.decorators.cache import cache_page

from leagues import views

urlpatterns = (
	url(r'^leagues.json', views.LeaguesView.as_view(), name='leagues'),
    url(r'^leagues/(?P<league_id>\d+).json$', views.LeagueView.as_view(), name='league'),
	url(r'^leagues/(?P<league_id>\d+)/free_agents.json$', cache_page(60*60) (views.FreeAgentsView.as_view()), name='free_agents'),

    url(r'^teams/(?P<team_id>\d+).json$', views.TeamView.as_view(), name='team'),

    url(r'^players/', include('players.api_urls')),
)