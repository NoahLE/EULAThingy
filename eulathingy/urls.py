from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from eulathingy.uploads.views import upload_nginx


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^dashboard/', include('dashboard.urls',
                                                   namespace='dashboard')),
                       url(r'^uploads/', include('uploads.urls',
                                                 namespace='uploads')),
                       url(r'^nginx_upload/', upload_nginx)
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)