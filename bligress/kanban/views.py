from django.http import HttpResponse

def index(request):
    return HttpResponse("Heippa.")

def showtask(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)

def showboard(request, board_id):
    return HttpResponse("You're looking at board %s." % board_id)
