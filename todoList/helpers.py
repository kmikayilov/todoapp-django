from todoList.forms import TodoTaskForm
from .models import Project, TodoTask, Label, Priority
import datetime


def all_tasks_counter():
    
    all_counts = {
        'projects': [],
        'labels': [],
        'today': 0,
        'upcoming': 0
    }

    # 1. all projects tasks count
    all_projects = Project.objects.all()
    for project in all_projects:
        all_counts['projects'].append({
            'id': project.id,
            'name': project.name,
            'color': project.color,
            'task_count': project.tasks.count()
        })
    
    # 2. all labels tasks count
    all_labels = Label.objects.all()
    for label in all_labels:
        all_counts['labels'].append({
            'id': label.id,
            'name': label.name,
            'color': label.color,
            'task_count': label.tasks.count()
        })
   
    # 3. today tasks count
    today_tasks = TodoTask.objects.filter(time=datetime.datetime.today()).count()
    all_counts['today'] = today_tasks
   
    # 4. upcoming tasks count
    upcoming_tasks = TodoTask.objects.filter(time__gt=datetime.datetime.today()).count()
    all_counts['upcoming'] = upcoming_tasks
   
    return all_counts


def upcomingTasksFetch():
    dateArr = []
    upcomingInfoArray = []
    
    for i in range(1,8):
        d = datetime.datetime.today() + datetime.timedelta(days=i)
        dateArr.append(d)

    for i in dateArr:
        upcomingInfoArray.append({
            "date": i.strftime("%a %d %B"),
            "tasks": TodoTask.objects.filter(time=i).order_by("priority"),
            "form": TodoTaskForm(initial={
                'time': i,
                'priority': Priority.objects.filter(rank=4)[0] if Priority.objects.filter(rank=4) else None,
                'project': Project.objects.filter(name="inbox")[0] if Project.objects.filter(name="inbox") else None
            }, prefix=i)
        })
    return upcomingInfoArray