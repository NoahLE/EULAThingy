from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',
                       url(r'^$', views.upload),
                       url(r'^submit/', views.upload_nginx)

)