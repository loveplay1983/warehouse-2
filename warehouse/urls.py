from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from reporting import urls as reporting_urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(reporting_urls)),
)