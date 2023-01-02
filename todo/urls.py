from django.contrib import admin
from django.urls import path

from .views import todo_view

urlpatterns = [
    path('', todo_view),
]