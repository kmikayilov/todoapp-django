# from todoList.models import TodoTask
from django.contrib import admin

from .models import Priority, TodoTask, Label, Project, Color

class ColorAdmin(admin.ModelAdmin):
    list_display = ("name", "color",)

class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name", "rank",)

class LabelAdmin(admin.ModelAdmin):
    list_display = ("name", "color",)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "color",)

class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ("task", "description", "label", "time")


# Register your models here.
admin.site.register(Color, ColorAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(TodoTask, TodoTaskAdmin)
admin.site.register(Project, ProjectAdmin)
