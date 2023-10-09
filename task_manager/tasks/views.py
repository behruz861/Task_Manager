from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def task_list(request):
    tasks = Task.objects.order_by('deadline', '-priority')
    completed_tasks = Task.objects.filter(status='completed').order_by('-priority')
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'completed_tasks': completed_tasks})
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {'form': form})
def task_edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_edit.html', {'form': form, 'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')