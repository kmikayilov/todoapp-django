from todoList.forms import TodoTaskForm
from django.shortcuts import render, redirect
from datetime import date
from .models import TodoTask, Project
from django.http import HttpResponseRedirect
from .forms import TodoTaskForm

from .helpers import all_tasks
# Create your views here.


def startingPage(request):
    return redirect('/app/today/')


def todayTodo(request):

    # inbox project filtering from all projects
    projects = Project.objects.filter(name='Inbox')

    # getting the date of today
    d = date.today().strftime("%a %d %B")

    tasks = all_tasks()

    # if new task is added
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/today")

    # if the page is loaded
    else:
        form = TodoTaskForm(initial={'time': date.today()})

    return render(request, 'todoList/todayTodoPage.html', {
        "all_tasks": tasks,
        "url": request.path[5:-1],
        "inbox_id": projects[0].id,
        "date": d,
        "form": form
    })


def upcomingTodo(request):
    
    # inbox project filtering from all projects
    projects = Project.objects.filter(name='Inbox')

    tasks = all_tasks()

    if request.method == 'POST':
        form = TodoTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/upcoming/")

    # if the page is loaded
    else:
        form = TodoTaskForm()

    return render(request, 'todoList/upcomingTodoPage.html', {
        "all_tasks": tasks,
        "url": request.path[5:13],
        "inbox_id": projects[0].id,
        "form": form
    })


def projectsTodo(request, id):
    
    # inbox project filtering from all projects
    projects = Project.objects.filter(name='Inbox')

    tasks = all_tasks()

    # if new task is added
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/project/{projects[0].id}")

    # if the page is loaded
    else:
        form = TodoTaskForm(initial={'time': date.today()})

    return render(request, 'todoList/inboxTodoPage.html', {
        "all_tasks": tasks,
        "url": request.path[5:12],
        "inbox_id": projects[0].id,
        # "tasks": [],  change it to be dependant from id
        "form": form
    })

def taskDone(request):
    print(request)
    task_id = request.POST["task-id"]
    task_to_be_deleted = TodoTask.objects.filter(id=task_id)
    task_to_be_deleted.delete()
    
    return HttpResponseRedirect('/app/today/')
  