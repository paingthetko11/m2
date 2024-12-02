from django.urls import path
from .import views

urlpatterns = [
    path('task_list/',views.task_list,name='task_list'),
    path('task_create/',views.task_create,name='task_create'),
    path('task_delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
