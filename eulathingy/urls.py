from django.shortcuts import HttpResponseRedirect
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eulathingy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', lambda r : HttpResponseRedirect('dashboard/')),
    url(r'^index/', lambda r : HttpResponseRedirect('dashboard/')),
    url(r'^app/', lambda r : HttpResponseRedirect('dashboard/app')),
    url(r'^contact/', lambda r : HttpResponseRedirect('dashboard/contact')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
)