from django.contrib import admin  
from django.conf.urls import include, url  
from django.views.generic import TemplateView

from leagues import views

urlpatterns = [  
    url(r'^admin/', admin.site.urls), # django admin

    url(r'^api/v3/', include('api.urls')), # django api

    url(r'^$', views.HomePageView.as_view(template_name="site_base.html"), name='site_home'),
    url(r'^players/', include('players.urls')),  
    url(r'^react/$', TemplateView.as_view(template_name="index.html"), name='index'),  # react app
]