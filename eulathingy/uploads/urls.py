from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',
                       url(r'^$', views.upload),
                       url(r'^nginx/', views.upload_nginx)
)