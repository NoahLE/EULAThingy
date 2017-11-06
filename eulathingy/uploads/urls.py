from django.conf.urls import patterns, url

from .views import upload, upload_nginx

urlpatterns = patterns('',
                       url(r'^$', upload),
                       url(r'^submit/', upload_nginx)
                       )
