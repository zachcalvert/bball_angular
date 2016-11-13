from django.contrib import admin  
from django.conf.urls import include, url  
from django.views.generic import TemplateView

from api.v1.routes import api_router

urlpatterns = [  
    url(r'^admin/', admin.site.urls),

    # API:V1
    url(r'^api/v1/', include(api_router.urls)),

    url(r'^api/v2/', include('leagues.api_urls')),
    # url(r'^api/v2/teams', include('teams.api_urls')),
    # url(r'^api/v2/players', include('players.api_urls')),


    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),  
]