from django.conf.urls import url  
from django.views.decorators.cache import cache_page

from schedule import views

urlpatterns = [  
    url(r'^(?P<season_id>\d+)/?$', views.SeasonView.as_view(), name='season'),
    url(r'^(?P<season_id>\d+)/game/(?P<game_id>\d+)?$', views.GameView.as_view(), name='game'),
]