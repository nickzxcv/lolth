from django.conf.urls import url, patterns, include
from django.contrib.gis import admin

from caves import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^caves/', include('caves.urls')),
)
