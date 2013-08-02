from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render
from django.shortcuts import redirect

from django.template import RequestContext

from kanban.models import Task
from kanban.models import Board
from django.forms import ModelForm

from django.contrib.auth.models import User

def index(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards': boards})

def taskshow(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except:
        raise Http404

    return render(request, 'task.html', {'task': task})


class TaskNewForm(ModelForm):
    class Meta:
        model = Task
        exclude = ["done_date", "queue_number", "owner", "group"]

    def __init__(self, *args, **kwargs):
        super(TaskNewForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.format = '%m/%d/%Y'
        self.fields['start_date'].widget.attrs.update({'class':'datePicker', 'readonly':'true'})

def tasknew(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
    except:
        raise Http404
    cf = TaskNewForm()
    return render(request, 'newtask.html', {'board_id': board_id, 'form': cf})

def taskcreate(request, board_id):
    if request.method != 'POST':
        raise Http404

    form = TaskNewForm(data = request.POST)
    if not form.is_valid():
        raise Http404

    try:
        board = Board.objects.get(pk=board_id)
    except:
        raise Http404

    try:
        user = User.objects.get(pk=1)
    except:
        raise Http404

    obj = form.save(commit = False)
    obj.owner = user
    obj.queue_number = 0
    obj.save()
    task_id = obj.id
    board.save()
    board.task.add(obj)

    #return redirect('/kanban/board/%s' % (board_id))
    return redirect('kanban:boardshow', board_id)

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

    return redirect('kanban:boardshow', board_id)

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

    return redirect('kanban:boardshow', board_id)

def boardshow(request, board_id):
    try:
        board = Board.objects.get(pk=board_id)
    except:
        raise Http404

    return render(request, 'board.html', {'board': board})

class BoardNewForm(ModelForm):
    class Meta:
        model = Board
        #exclude = ["done_date", "queue_number", "owner", "group"]
        exclude = ["task"]

    def __init__(self, *args, **kwargs):
        super(BoardNewForm, self).__init__(*args, **kwargs)
        #self.fields['start_date'].widget = widgets.AdminDateWidget()
        self.fields['start_date'].widget.format = '%m/%d/%Y'
        self.fields['start_date'].widget.attrs.update({'class':'datePicker', 'readonly':'true'})

def boardnew(request):
    cf = BoardNewForm()
    return render(request, 'boardnew.html', {'form': cf})

def boardcreate(request):
    if request.method != 'POST':
        raise Http404

    form = BoardNewForm(data=request.POST)
    if not form.is_valid():
        raise Http404

    obj = form.save(commit = False)
    obj.save()
    form.save_m2m()
    if obj.phases.count() == 0:
        form = BoardNewForm(instance=obj, data=request.POST)
        return render(request, 'boardnew.html', {'form': form, 'errormsg': 'Please select at least one phase'} )
    board_id = obj.id

    return redirect('kanban:boardshow', board_id)
