from django.contrib import admin
from django.urls import path

from .views import Todo, TaskDetail, TaskDelete

urlpatterns = [
    path('', Todo.as_view(), name='todo'),
    path('<str:pk>/', TaskDetail.as_view(), name='task'),
    path('<str:pk>/delete/', TaskDelete.as_view(), name="delete"),
]