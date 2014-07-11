#from django.conf.urls import patterns, include, url
#
from django.contrib import admin
admin.autodiscover()
#
#urlpatterns = patterns('',
#    # Examples:
#    # url(r'^$', 'lolth.views.home', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    url(r'^admin/', include(admin.site.urls)),
#)

from django.conf.urls import url, include
from django.contrib.gis import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    ]
