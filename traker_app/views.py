from django.views.generic import ListView, DetailView, DeleteView, CreateView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm


class TaskListView(ListView):
    model = Task
    template_name = "traker_app/task_list.html"
    context_object_name = "task_list"

from django.shortcuts import render, redirect
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user  
            task.save()
            return redirect('task_list') 
    else:
        form = TaskForm()

    return render(request, 'traker_app/task_add.html', {'form': form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect('task_list')
    else:
        form = CommentForm()

    return render(request, 'traker_app/task_detail.html', {
        'task': task,
        'comments': comments,
        'form': form
    })

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'traker_app/task_delete.html'
    success_url = reverse_lazy('task_list')