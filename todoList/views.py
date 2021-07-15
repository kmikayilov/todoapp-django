from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def startingPage(request):
    return redirect('/app/today')


def todayTodo(request):
    return render(request, 'todoList/todayTodoPage.html')

def upcomingTodo(request):
    pass

def inboxTodo(request):
    pass
