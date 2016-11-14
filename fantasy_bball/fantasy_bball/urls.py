from django.contrib import admin  
from django.conf.urls import include, url  
from django.views.generic import TemplateView

urlpatterns = [  
    url(r'^admin/', admin.site.urls), # django admin

    url(r'^api/v2/', include('leagues.api_urls')), # django api

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),  # react app
]