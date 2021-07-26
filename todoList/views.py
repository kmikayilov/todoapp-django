from django.http.response import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.urls import reverse
from django.views import View


from .models import Priority, TodoTask, Project, Label
from .forms import TodoTaskForm
from .helpers import all_tasks_counter, upcomingTasksFetch

# Create your views here.


def startingPage(request):
    return redirect('/app/today/')

class todayView(View):
    template_name = 'todoList/todayTodoPage.html'
    
    def get(self, request):
        form = TodoTaskForm(
            initial={
                'time': date.today(),
                'priority': Priority.objects.filter(rank=4)[0],
                'project': Project.objects.filter(name="Inbox")[0]
                }
            )

        context = {
            'all_tasks_count': all_tasks_counter(),
            'form': form,
            'tasks': TodoTask.objects.filter(time=date.today()).order_by('priority'),
            'date': date.today().strftime("%a %d %B"),
            'url': request.path[5:-1]
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('today-tasks'))

        return render(request, self.template_name, {"form": form})


class upcomingView(View):
    template_name = 'todoList/upcomingTodoPage.html'
    
    def get(self, request):
        upcoming = upcomingTasksFetch()
        
        context = {
            'all_tasks_count': all_tasks_counter(),
            'url': request.path[5:-1],
            "upcomingInfoArr": upcoming
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('upcoming-tasks'))

        return render(request, self.template_name, {"form": form})


class projectView(View):
    template_name = 'todoList/projectTodoPage.html'
    
    def get(self, request, name):
        form = TodoTaskForm(
            initial={
                'time': date.today(),
                'priority': Priority.objects.filter(rank=4)[0],
                'project': Project.objects.filter(name=name.capitalize())[0]
                }
            )
        project = Project.objects.filter(name=name.capitalize())

        if not project:
            raise Http404("There is no such project.")


        context = {
            'project_name': project[0].name,
            'tasks': project[0].tasks.all().order_by('priority'),
            'all_tasks_count': all_tasks_counter(),
            'form': form,
            'url': request.path[5:12],
            'date': date.today()
        }

        return render(request, self.template_name, context)

    def post(self, request, name):
        form = TodoTaskForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('project-detail', args=[name]))

        return render(request, self.template_name, {"form": form})


class labelView(View):
    template_name = 'todoList/labelTodoPage.html'
    
    def get(self, request, name):
        label = Label.objects.filter(name=name.capitalize())

        
        if not label:
            raise Http404("There is no such label.")


        context = {
            'label_name': label[0].name,
            'tasks': label[0].tasks.all().order_by('priority'),
            'all_tasks_count': all_tasks_counter(),
            'url': request.path[5:10]
        }

        return render(request, self.template_name, context)
        
class taskDoneView(View):

    def post(self, request):
        task_id = request.POST["task-id"]
        task_to_be_deleted = TodoTask.objects.filter(id=task_id)
        task_to_be_deleted.delete()
        
        if (request.POST["url"] == 'today'): 
            return HttpResponseRedirect(reverse('today-tasks'))
        elif (request.POST["url"] == 'upcoming'):
            return HttpResponseRedirect(reverse('upcoming-tasks'))
        elif (request.POST["url"] == 'project'):
            return HttpResponseRedirect(reverse('project-detail', args=[request.POST["project_name"].lower()]))
        elif (request.POST["url"] == 'label'):
            return HttpResponseRedirect(reverse('label-detail', args=[request.POST["label_name"].lower()]))
        else:
            return HttpResponseRedirect(reverse('today-tasks'))
