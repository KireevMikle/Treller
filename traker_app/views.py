from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class TaskListView(ListView):
    model = Task
    template_name = "traker_app/task_list.html"
    context_object_name = "task_list"
