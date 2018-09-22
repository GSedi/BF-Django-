from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def todos(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "todos_list.html", context)

@csrf_exempt
def completed_todos(request):
    tasks = [i for i in Task.objects.all() if i.mark]
    context = {
        'tasks': tasks
    }
    return render(request, "completed_todos_list.html", context)

def completed_todo(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, "completed_todo.html", {'task': task})

@csrf_exempt
def todos_filter(request, filter_by):
    task = Task.objects.order_by(filter_by)
    context = {
        'tasks': task
    }
    return render(request, "todos_list.html", context)
