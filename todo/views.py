from django.shortcuts import render, redirect
from .models import Task
from django.views import View

# Create your views here.

class Todo(View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {'tasks': tasks}
        return render(request, 'index.html', context)

    def post(self, request):
        task = Task.objects.create(
            title=request.POST.get('title')
        )
        task.save()
        return redirect('todo')

class TaskDetail(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'task.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.title = request.POST.get('title')
        task.save()
        return redirect('todo')

class TaskDelete(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        context = {'task':task}
        return render(request, 'delete.html', context)

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return redirect('todo')