from django.conf.urls import patterns, url

from .views import index, contact, results, read, app


urlpatterns = patterns('',
                       url(r'^$', index, name='index'),
                       url(r'^index', index, name='index'),
                       url(r'^contact/', contact, name='contact'),
                       url(r'^app/', app, name='app'),
                       url(r'^results/', results, name='results'),
                       url(r'^results/', results, name='results'),
                       url(r'^read/', read, name='read')
)
