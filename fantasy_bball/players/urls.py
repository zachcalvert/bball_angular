from django.conf.urls import url  
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from players import views

urlpatterns = [  
	# url(r'^all/?$', cache_page(60*60)(views.PlayersView.as_view()), name='players'),
    url(r'^(?P<player_id>\d+)/?$', views.PlayerView.as_view(), name='player'),
]