from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url("", include('django_socketio.urls')),
    #home page
    (r"^$", TemplateView.as_view(template_name='index.html')),
)
