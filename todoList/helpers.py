from .models import Project, TodoTask
from datetime import date


def all_tasks():

    # inbox project tasks
    inbox_tasks = Project.objects.filter(name='Inbox')[0].tasks.all() 

    # getting all today tasks by ordering comparing priority in asc order
    today_tasks = TodoTask.objects.filter(time=date.today()).order_by('priority')

    # getting all the upcoming tasks by ordering comparing priority in asc order
    upcoming_tasks = TodoTask.objects.filter(time__gt=date.today()).order_by('priority')

    tasks = {
        "inbox": inbox_tasks,
        "today": today_tasks,
        "upcoming": upcoming_tasks
    }

    return tasks