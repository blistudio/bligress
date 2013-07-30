from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render

from kanban.models import Task
from kanban.models import Board

def index(request):
    return HttpResponse("Heippa.")

def showtask(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except:
        raise Http404

    return render(request, 'task.html', {'task': task})

def showboard(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
    except:
        raise Http404

    return render(request, 'board.html', {'board': board})
