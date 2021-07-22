from todoList.forms import TodoTaskForm
from django.shortcuts import render, redirect
from datetime import date
from .models import TodoTask, Project
from django.http import HttpResponseRedirect
from .forms import TodoTaskForm

# Create your views here.


def startingPage(request):
    return redirect('/app/today')


def todayTodo(request):

    # inbox project filtering from all projects
    projects = Project.objects.filter(name='Inbox')

    # getting the date of today
    d = date.today().strftime("%a %d %B")

    # getting all tasks for today by ordering comparing priority in asc order
    tasks = TodoTask.objects.filter(time=date.today()).order_by('priority')

    # if new task is added
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/today")

    else:
        # if the page is loaded
        form = TodoTaskForm(initial={'time': date.today()})

    return render(request, 'todoList/todayTodoPage.html', {
        "url": request.path[5:-1],
        "inbox_id": projects[0].id,
        "date": d,
        "tasks": tasks,
        "form": form
    })


def upcomingTodo(request):
    return render(request, 'todoList/todayTodoPage.html')


def projectsTodo(request, id):
    full_path = request.path
    print(full_path[5:12])

    projects = Project.objects.filter(name='Inbox')

    d = date.today().strftime("%a %d %B")
    tasks = TodoTask.objects.filter(project=projects[0]).order_by('priority')

    if request.method == 'POST':
        form = TodoTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/today")

    else:
        form = TodoTaskForm(initial={'time': date.today()})

    return render(request, 'todoList/inboxTodoPage.html', {
        "url": request.path[5:12],
        "tasks": tasks,
        "form": form
    })


def taskDone(request):
    task_id = request.POST["task-id"]
    task_to_be_deleted = TodoTask.objects.filter(id=task_id)
    task_to_be_deleted.delete()
    return HttpResponseRedirect("/app/today")
