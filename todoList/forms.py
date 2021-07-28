from django import forms
from .models import Project, TodoTask, Label
import random

class DateInput(forms.DateInput):
    input_type = 'date'
    class Meta:
        format = '%d %b, %Y'
class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = '__all__'
        widgets = {
            'task': forms.TextInput(attrs={'placeholder': 'Task name', 'id': 'id_task_' + str(random.randint(0, 100))}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': '3', 'id': 'id_desc_' + str(random.randint(0, 100))}),
            'label': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select...', 'id': 'id_label_' + str(random.randint(0, 100))}),
            'project': forms.Select(attrs={'class': 'form-select', 'id': 'id_project_' + str(random.randint(0, 100))}),
            'priority': forms.Select(attrs={'class': 'form-select', 'id': 'id_priority_' + str(random.randint(0, 100))}),
            'time': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'id_time_' + str(random.randint(0, 100))}),
            'reminder': DateInput(attrs={'class': 'form-control', 'type': 'date', 'id': 'id_reminder_' + str(random.randint(0, 100))}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'color': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select...'}),
        }


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'color': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select...'}),
        }