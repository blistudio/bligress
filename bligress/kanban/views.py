from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render
from django.shortcuts import redirect

from kanban.models import Task
from kanban.models import Board

def index(request):
    return HttpResponse("Heippa.")

def taskshow(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except:
        raise Http404

    return render(request, 'task.html', {'task': task})

def taskforw(request, board_id, task_id):
    try:
        board = Board.objects.get(pk=board_id)
    except:
        raise Http404
    try:
        task = Task.objects.get(pk=task_id)
    except:
        raise Http404

    nextphase = None
    getnext = False
    for phase in board.phases.order_by('order'):
        if getnext:
            nextphase = phase
            break 
        if phase == task.phase:
            getnext = True

    if nextphase is not None:
        task.phase = nextphase
        task.save()

    return redirect('/kanban/board/%s' % (board_id))

def taskback(request, board_id, task_id):
    try:
        board = Board.objects.get(pk=board_id)
    except:
        raise Http404
    try:
        task = Task.objects.get(pk=task_id)
    except:
        raise Http404

    prevphase = None
    getprev = False
    for phase in board.phases.order_by('order'):
        if phase == task.phase:
            getprev = True
            break
        prevphase = phase

    if getprev and prevphase is not None:
        task.phase = prevphase
        task.save()

    return redirect('/kanban/board/%s' % (board_id))

def boardshow(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
    except:
        raise Http404

    return render(request, 'board.html', {'board': board})
