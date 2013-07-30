from django.conf.urls import patterns, url

from kanban import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^task/(?P<task_id>\d+)/$', views.taskshow, name='taskshow'),
    url(r'^taskback/(?P<board_id>\d+)/(?P<task_id>\d+)/$', views.taskback, name='taskback'),
    url(r'^taskforw/(?P<board_id>\d+)/(?P<task_id>\d+)/$', views.taskforw, name='taskforw'),
    url(r'^board/(?P<board_id>\d+)/$', views.boardshow, name='boardshow')
)
