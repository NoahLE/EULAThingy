from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^index', views.index, name='index'),
                       url(r'^contact/', views.contact, name='contact'),
                       url(r'^app/', views.app, name='app'),
                       url(r'^results/', views.results, name='results'),
                       url(r'^app/', views.app, name='app'),
                       url(r'^results/', views.results, name='results'),
                       url(r'^read/', views.read, name='read')
)
