from django.conf.urls import url, include
from django.views.decorators.cache import cache_page

from api import views

urlpatterns = [
	url(r'^home.json', views.FeaturedPageView.as_view(), name='featured_page'),

	url(r'^leagues.json', views.LeaguesView.as_view(), name='leagues'),
    url(r'^leagues/(?P<league_id>\d+).json$', views.LeagueView.as_view(), name='league'),
	url(r'^leagues/(?P<league_id>\d+)/free_agents.json$', cache_page(60*60) (views.FreeAgentsView.as_view()), name='free_agents'),
	url(r'^leagues/(?P<league_id>\d+)/matchups.json$', cache_page(60*60) (views.MatchupsView.as_view()), name='matchups'),

    url(r'^teams/(?P<team_id>\d+).json$', views.TeamView.as_view(), name='team'),

	url(r'^players/all.json', cache_page(60*60)(views.PlayersView.as_view()), name='players_api'),
    url(r'^players/(?P<player_id>\d+).json$', views.PlayerView.as_view(), name='player_api'),
]