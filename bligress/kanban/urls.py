from django.conf.urls import patterns, url

from kanban import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^task/(?P<task_id>\d+)/$', views.showtask, name='showtask')
    url(r'^board(?P<board_id>\d+)/$', views.showboard, name='showboard')
)
