from django.conf.urls import patterns, url

from kanban import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^task/(?P<board_id>\d+)/(?P<task_id>\d+)/$', views.taskshow, name='taskshow'),
    url(r'^taskedit/(?P<board_id>\d+)/(?P<task_id>\d+)/$', views.taskedit, name='taskedit'),
    url(r'^taskback/(?P<board_id>\d+)/(?P<task_id>\d+)/$', views.taskback, name='taskback'),
    url(r'^tasknew/(?P<board_id>\d+)/$', views.tasknew, name='tasknew'),
    url(r'^taskforw/(?P<board_id>\d+)/(?P<task_id>\d+)/$', views.taskforw, name='taskforw'),
    url(r'^taskcreate/(?P<board_id>\d+)/$', views.taskcreate, name='taskcreate'),
    url(r'^board/(?P<board_id>\d+)/$', views.boardshow, name='boardshow'),
    url(r'^boardnew/$', views.boardnew, name='boardnew'),
    url(r'^boardcreate/$', views.boardcreate, name='boardcreate'),
)
