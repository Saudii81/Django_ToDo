from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here. 
def home(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request, "tasks/home.html", {"tasks": tasks})

def add_task(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "tasks/add_task.html", {"form": form})

