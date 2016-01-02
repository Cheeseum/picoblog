from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

app_name = 'picoblog'
urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^p/(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),

    url(r'^admin/', include(admin.site.urls)),
)
