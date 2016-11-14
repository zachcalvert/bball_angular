from django.conf.urls import url, include

from leagues import views

urlpatterns = (
	url(r'^leagues.json', views.LeaguesView.as_view(), name='leagues'),
    url(r'^leagues/(?P<league_id>\d+).json$', views.LeagueView.as_view(), name='league'),
    url(r'^teams/(?P<team_id>\d+).json$', views.TeamView.as_view(), name='team'),
    url(r'^players/', include('players.api_urls')),
)