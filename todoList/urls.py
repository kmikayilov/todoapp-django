from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.startingPage),
    path('app/today/', views.todayTodo, name="today-tasks"),
    path('app/upcoming/', views.upcomingTodo, name="upcoming-tasks"),
    path('app/project/<id>/', views.projectsTodo, name="project-detail"),
    path('app/task-done/', views.taskDone, name="task-done"),
]
