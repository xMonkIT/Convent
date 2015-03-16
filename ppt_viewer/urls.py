from django.conf.urls import patterns, url
from ppt_viewer import views

urlpatterns = patterns('',
		url(r'^$', 'ppt_viewer.views.home', name='home'),
		url(r'^presentation/(?P<thesis_id>\d+)/$', views.presentation, name='presentation'),
		url(r'^thesis_list/(?P<section_id>\d+)$', views.thesis_list, name='thesis_list'),
)
