from django.urls import path
from . import views
from .views import task_detail, TaskDeleteView  # імпортуємо тільки те, що не беремо через views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('add-task/', views.add_task, name='add_task'),
    path('task-list/', views.TaskListView.as_view(), name='task_list'),
    path('task-detail/<int:pk>/', task_detail, name='task_detail'),
    path('task/task-detail/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]