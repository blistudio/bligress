from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return redirect('kanban:index')

def loginview(request):
    if request.method != 'POST':
        username = request.POST['username']
        password = request.POST['password']
    else:
        username = None
        password = None

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('kanban:index')

    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('kanban:index')
