from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView, UpdateView


def index(request):
    return render(request, 'tasks/index.html')


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect(index)
    form = TaskForm()

    data = {
        'form': form
    }
    return render(request, 'tasks/add.html', data)


class EditDetailView(DetailView):
    model = Task
    template_name = 'tasks/edit.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/add.html'

    fields = ['title', 'description', 'is_completed', 'created_at']
