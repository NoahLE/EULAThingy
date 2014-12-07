from django.conf.urls import patterns, url, include
from dashboard import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^app/', views.app, name='app'),
)