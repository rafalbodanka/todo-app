from django.shortcuts import render

from .forms import Task

# Create your views here.

def todo_view(request):

    form = Task(request.POST)

    if form.is_valid():
        return 0

    else:
        form = Task()

    context = {'form': form}

    response = render(request, "index.html", context)

    return response