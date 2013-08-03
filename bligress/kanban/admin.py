from django.contrib import admin

from kanban.models import Task
from kanban.models import Phase
from kanban.models import Board

admin.site.register(Task)
admin.site.register(Phase)
admin.site.register(Board)
