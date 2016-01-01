from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'picoblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),

    url(r'^admin/', include(admin.site.urls)),
)
