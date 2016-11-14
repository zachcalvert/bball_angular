from django.conf.urls import url
from django.views.decorators.cache import cache_page

from players import views

urlpatterns = (
	url(r'^all.json', cache_page(60*60)(views.PlayersView.as_view()), name='players'),
    url(r'^(?P<player_id>\d+).json$', views.PlayerView.as_view(), name='player'),
)