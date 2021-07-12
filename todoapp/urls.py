from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("todoList.urls")),
]
