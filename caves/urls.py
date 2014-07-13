from django.conf.urls import patterns, url

from caves import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<cave_id>\d+)/name$', views.name, name='name')
	url(r'^(?P<cave_id>\d+)/entrances$', views.entrances, name='entrances')
)
