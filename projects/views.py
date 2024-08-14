from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Project, Task

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'duration']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'description', 'duration']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project-list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project-list')

class TaskCreateView(CreateView):
    model = Task
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'projects/task_form.html'

    def form_valid(self, form):
        form.instance.project_id = self.kwargs['project_pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'pk': self.kwargs['project_pk']})

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['name', 'description', 'start_date', 'end_date']
    template_name = 'projects/task_form.html'

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'pk': self.kwargs['project_pk']})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'projects/task_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'pk': self.kwargs['project_pk']})
