from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.urls import reverse
from django.views import View


from .models import Priority, TodoTask, Project, Label, Color
from .forms import TodoTaskForm, ProjectForm, LabelForm
from .helpers import all_tasks_counter, upcomingTasksFetch

# Create your views here.


def startingPage(request):
    return redirect('/app/today/')

class todayView(View):
    template_name = 'todoList/pages/TodayTasks.html'
    
    def get(self, request):
        form = TodoTaskForm(
            initial={
                'time': date.today(),
                'priority': Priority.objects.filter(rank=4)[0] if Priority.objects.filter(rank=4) else None,
                'project': Project.objects.filter(name="inbox")[0] if Project.objects.filter(name="inbox") else None
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
    template_name = 'todoList/pages/UpcomingTasks.html'
    
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
    template_name = 'todoList/pages/ProjectDetails.html'
    
    def get(self, request, name):
        form = TodoTaskForm(
            initial={
                'time': date.today(),
                'priority': Priority.objects.filter(rank=4)[0] if Priority.objects.filter(rank=4) else None,
                'project': Project.objects.filter(name=name)[0] if Project.objects.filter(name=name) else None
                }
            )

        project = Project.objects.filter(name=name)

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
    template_name = 'todoList/pages/LabelDetails.html'
    
    def get(self, request, name):
        label = Label.objects.filter(name=name)[0] if Label.objects.filter(name=name) else None

        
        if not label:
            raise Http404("There is no such label.")


        context = {
            'label_name': label.name,
            'tasks': label.tasks.all().order_by('priority'),
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
            return HttpResponseRedirect(reverse('project-detail', args=[request.POST["project_name"]]))
        elif (request.POST["url"] == 'label'):
            return HttpResponseRedirect(reverse('label-detail', args=[request.POST["label_name"]]))
        else:
            return HttpResponseRedirect(reverse('today-tasks'))


class itemAddView(View):
    template_name = 'todoList/pages/ItemAdd.html'
    
    def get(self, request, type):
        if type == 'project': 
            form = ProjectForm(initial={'color': Color.objects.filter(name='Charcoal')[0] if Color.objects.filter(name='Charcoal') else None})
        elif type == 'label':
            form = LabelForm(initial={'color':  Color.objects.filter(name='Charcoal')[0] if Color.objects.filter(name='Charcoal') else None})
        else:
            return Http404("No such feature!")
            
        context = {
            'type': type.capitalize(),
            'form': form,
            'all_tasks_count': all_tasks_counter(),
            'url': request.path[5:10]
        }
        return render(request, self.template_name, context)

    def post(self, request, type):
        if type == 'project': 
            form = ProjectForm(request.POST)
        else:
            form = LabelForm(request.POST)
       

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item-add', args=[type]))

        return render(request, self.template_name, {"form": form})


class itemEditView(View):
    template_name = 'todoList/pages/ItemEdit.html'
    
    def get(self, request, type, name):
        if type == 'project':
            project =  Project.objects.filter(name=name)[0] if Project.objects.filter(name=name) else None
            form = ProjectForm(initial={'name': project.name,'color': project.color})
        elif type == 'label':
            label =  Label.objects.filter(name=name)[0] if Label.objects.filter(name=name) else None
            form = LabelForm(initial={'name': label.name,'color': label.color})
        else:
            return Http404("No such feature!")
            
        context = {
            'type': type.capitalize(),
            'form': form,
            'all_tasks_count': all_tasks_counter(),
            'url': request.path[5:10]
        }
        return render(request, self.template_name, context)

    def post(self, request, type, name):
        if type == 'project': 
            form = ProjectForm(request.POST, instance =  get_object_or_404(Project, name=name))
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('project-detail', args=[request.POST['name']]))
        else:
            form = LabelForm(request.POST, instance =  get_object_or_404(Label, name=name))
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('label-detail', args=[request.POST['name']]))
       

        return render(request, self.template_name, {"form": form})


class itemDeleteView(View):
    def get(self, request, type, name):
        if type == 'project': 
            item = Project.objects.filter(name=name)[0] if Project.objects.filter(name=name) else None
        elif type == 'label':
            item = Label.objects.filter(name=name)[0] if Label.objects.filter(name=name) else None
        else:
            return Http404("No such feature!")

        if item is not None:
            item.delete()
      
        return HttpResponseRedirect(reverse('today-tasks'))


class taskEditView(View):
    template_name = 'todoList/pages/TaskEdit.html'
    
    def get(self, request, id):
        print(id)
        task =  get_object_or_404(TodoTask, id=id)
        form = TodoTaskForm(instance=task)
            
        context = {
            'id': id,
            'form': form,
            'all_tasks_count': all_tasks_counter(),
            'url': request.path[5:10]
        }
        return render(request, self.template_name, context)

    def post(self, request, id):
        task =  get_object_or_404(TodoTask, id=id)
        form = TodoTaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('today-tasks'))
        
        return render(request, self.template_name, {"form": form})
