from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Schedule
from .forms import ScheduleForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after successful registration
            login(request, user)
            return redirect('task_list')
    else:
        form = RegistrationForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Schedule.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user  # Assign the logged-in user to the task
            schedule.save()
            return redirect('task_list')
    else:
        form = ScheduleForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('calendar')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def delete_task(request, task_id):
    # Get the task by ID or return a 404 if not found
    schedule = get_object_or_404(Schedule, id=task_id)

    # Perform the deletion
    schedule.delete()

    # Return a JSON response indicating success
    return JsonResponse({'message': 'Task deleted successfully'})


def index_view(request):
    return render(request, 'tasks/index.html')

@login_required()
def calendar_view(request):
    return render(request,'tasks/calendar.html')