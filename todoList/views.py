from todoList.forms import TodoTaskForm
from django.shortcuts import render, redirect
from datetime import date
from .models import TodoTask
from django.http import HttpResponseRedirect
from .forms import TodoTaskForm

# Create your views here.

def startingPage(request):
    return redirect('/app/today')


def todayTodo(request):
    d = date.today().strftime("%a %d %B")
    tasks = TodoTask.objects.all()

    if request.method == 'POST': 
        form = TodoTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/app/today")

    else:
        form = TodoTaskForm()

    return render(request, 'todoList/todayTodoPage.html', {
        "date": d,
        "tasks": tasks,
        "form": form
    })

def upcomingTodo(request):
    return render(request, 'todoList/todayTodoPage.html')

def inboxTodo(request):
    return render(request, 'todoList/todayTodoPage.html')

def taskDone(request):
    task_id = request.POST["task-id"]
    print(task_id)
    task_to_be_deleted = TodoTask.objects.filter(id = task_id)
    task_to_be_deleted.delete()
    return HttpResponseRedirect("/app/today")