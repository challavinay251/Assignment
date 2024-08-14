from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-edit'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('project/<int:project_pk>/task/new/', TaskCreateView.as_view(), name='task-create'),
    path('project/<int:project_pk>/task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('project/<int:project_pk>/task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
