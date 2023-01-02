from django.shortcuts import render

# Create your views here.

def todo_view(request):

    context = {}

    response = render(request, "index.html", context)

    return response