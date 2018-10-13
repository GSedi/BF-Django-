from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoList, Task
from .forms import TodoListForm, TaskForm, SearchForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def to_do_lists(request):
    todo_lists = request.user.todo_lists.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            context = {
                'todo_lists': todo_lists.filter(name__contains = search),
            }
            return render(request, 'todo_list/show.html', context)
        else:
            error = "input is empty"
            context = {
                'todo_lists': todo_lists,
                'error': error,        
            }
            return render(request, 'todo_list/show.html', context)

    context = {
        'todo_lists': todo_lists,
    }
    return render(request, 'todo_list/show.html', context)

@login_required
def add_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('todo_lists')
    form = TodoListForm
    context = {
        'form': form,
    }
    return render(request, "todo_list/add.html", context)
@login_required
def delete_todo_list(request, id):
    TodoList.objects.get(pk=id).delete()
    return redirect('todo_lists')

@login_required
def update_todo_list(request, id):
    instance = get_object_or_404(TodoList, pk=id)
    form = TodoListForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('todo_lists')
    context = {
        'form': form,
        'name': instance.name,
        'id': id,
    }
    return render(request, 'todo_list/update.html', context) 

def tasks(request, id):
    ilist = TodoList.objects.get(pk=id)
    tasks = ilist.tasks.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            context = {
                'tasks': tasks.filter(title__contains = search),
                'ilist': ilist,
            }
            return render(request, 'task/show.html', context)
        else:
            error = "input is empty"
            context = {
                'tasks': tasks,
                'error': error,        
                'ilist': ilist,
            }
            return render(request, 'task/show.html', context)
    context = {
        'tasks': tasks,
        'ilist': ilist,
    }
    return render(request, "task/show.html", context)

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            fk = form.cleaned_data['todo_list'].id
            return redirect('tasks', fk)
        else:
            error = "something not valid"
            context = {
                'form': form,
                'error': error,
            }
            return render(request, "task/add.html", context)
    form = TaskForm()
    context = {
        'form': form,
    }
    return render(request, "task/add.html", context)
@login_required
def delete_task(request, id):
    fk = Task.objects.get(pk=id).todo_list.id
    Task.objects.get(pk=id).delete()
    return redirect('tasks', fk)
@login_required
def update_task(request, id):
    instance = get_object_or_404(Task, pk=id)
    form = TaskForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            fk = form.cleaned_data['todo_list'].id
            return redirect('tasks', fk)
        else:
            error = "something not valid"
            context = {
                'form': form,
                'error': error,
            }
            return render(request, "task/add.html", context)
    context = {
        'form': form,
        'name': instance.title,
        'id': id,
    }
    return render(request, 'task/update.html', context)
@login_required
def change_mark(request, id):
    fk = Task.objects.get(pk=id).todo_list.id
    ilist = TodoList.objects.get(pk=fk)
    tasks = ilist.tasks.all()
    task = tasks.get(pk=id)
    if task.mark:
        task.mark = False
    else:
        task.mark = True
    task.save()
    return redirect('tasks', fk)

def done_tasks(request, id):
    ilist = TodoList.objects.get(pk=id)
    tasks = [i for i in ilist.tasks.all() if i.mark is True]
    context = {
        'tasks': tasks,
        'ilist': ilist,
    }
    return render(request, "task/show.html", context)

def order(request, order_by):
    return
