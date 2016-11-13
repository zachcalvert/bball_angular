from django.conf.urls import url

from leagues import views

urlpatterns = (
	url(r'^leagues.json', views.LeaguesView.as_view(), name='leagues'),
    url(r'^leagues/(?P<league_id>\d+).json$', views.LeagueView.as_view(), name='league'),
)