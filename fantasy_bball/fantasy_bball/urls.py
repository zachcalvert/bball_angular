from django.contrib import admin  
from django.conf.urls import include, url  
from django.views.generic import TemplateView

from leagues.views import HomePageView

urlpatterns = [  
    url(r'^admin/', admin.site.urls), # django admin

    url(r'^api/v3/', include('api.urls')), # django api

    url(r'^$', HomePageView.as_view(template_name="site_base.html"), name='site_home'),
    url(r'^leagues/', include('leagues.urls')),
    url(r'^players/', include('players.urls')),
    url(r'^season/', include('schedule.urls')),
    url(r'^react/$', TemplateView.as_view(template_name="index.html"), name='index'),  # react app
]