# from todoList.models import TodoTask
from django.contrib import admin

from .models import Priority, TodoTask, Label

# Register your models here.
admin.site.register(Label)
admin.site.register(Priority)
admin.site.register(TodoTask)
