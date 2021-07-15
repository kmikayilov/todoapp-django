from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.startingPage),
    path('app/today/', views.todayTodo, name="today-tasks"),
    path('app/upcoming/', views.upcomingTodo, name="upcoming-tasks"),
    path('app/inbox/', views.inboxTodo, name="inbox-tasks"),
]
