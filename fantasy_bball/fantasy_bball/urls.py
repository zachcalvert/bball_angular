from django.contrib import admin  
from django.conf.urls import include, url  
from django.views.generic import TemplateView

urlpatterns = [  
    url(r'^admin/', admin.site.urls),

    url(r'^api/v2/', include('leagues.api_urls')),
    # url(r'^api/v2/teams', include('teams.api_urls')),
    # url(r'^api/v2/players', include('players.api_urls')),


    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),  
]