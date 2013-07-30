from django.contrib import admin
from kanban.models import Task
from kanban.models import Phase

admin.site.register(Task)
admin.site.register(Phase)
