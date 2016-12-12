from django.conf.urls import url  

from leagues import views

urlpatterns = [  
	# url(r'^all/?$', views.Leagues.as_view()), name='leagues'),
    url(r'^(?P<league_id>\d+)/?$', views.LeagueView.as_view(), name='league'),
    url(r'^(?P<league_id>\d+)/team/(?P<team_id>\d+)?$', views.TeamView.as_view(), name='team'),
]