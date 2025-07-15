from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    status_filter = request.GET.get("status", "all")
    category_filter = request.GET.get("category", "all")

    if status_filter != "all":
        tasks = tasks.filter(is_completed=(status_filter == "completed"))

    if category_filter != "all":
        tasks = tasks.filter(category=category_filter)

    completed_tasks = tasks.filter(is_completed=True)
    pending_tasks = tasks.filter(is_completed=False)
    return render(
        request,
        "t1/task_list.html",
        {
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "status_filter": status_filter,
            "category_filter": category_filter,
        },
    )

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "t1/task_create.html", {"form": form})

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "t1/task_update.html", {"form": form, "task": task})

@login_required
def task_delete(request, task_id):
    
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    task.delete()
    return redirect("task_list")

@login_required
def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect("task_list")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
           
            login(request, user)
            return redirect("task_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

                                                                     