from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from tast_tracer_app.forms import CommentForm, TaskForm
from .models import Task
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .mixins import AuthorRequiredMixin
from django.shortcuts import redirect

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task_list'
    ordering = ['-createde_at', '-priority']

    def get_queryset(self):
        status_filter = self.request.GET.get('status_filter')
        tasks = Task.objects.filter(author=self.request.user)
        status = self.kwargs.get('status', '')
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        return tasks

class TaskDetailView(AuthorRequiredMixin,DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = task
            comment.save()
            return redirect('task_detail', pk=task.pk)

class TaskCreateView(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class TaskUpdateView(AuthorRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('home')

class TaskDeleteView(AuthorRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('home')



