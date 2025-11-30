from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    ordering = ['-createde_at']

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
