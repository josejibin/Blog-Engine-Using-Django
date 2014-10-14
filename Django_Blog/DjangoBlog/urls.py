from django.conf.urls import patterns, include, url
from django.contrib import admin

from blogengine  import views

urlpatterns = [
    url(r'^welcome/$','blogengine.views.welcome'),
    url(r'^signup/$','blogengine.views.signUp'),
    url(r'^login/$','blogengine.views.logIn'),
    url(r'^logout/$','blogengine.views.logOut'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'blogengine.views.getPosts'),
    url(r'^newpost/','blogengine.views.newpost'),
    url(r'^search-form/$', 'blogengine.views.search_form'),
    url(r'^search/$', 'blogengine.views.search'),
    url(r'^$', 'blogengine.views.getPosts'),
	url(r'^(?P<selected_page>\d+)/?$', 'blogengine.views.getPosts'),
	url(r'^posts/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),
]
