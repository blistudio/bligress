from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from bligress import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^kanban/', include('kanban.urls', namespace="kanban")),
     url(r'^kanbanadmin/', include(admin.site.urls)),
)
