from django import forms
from .models import TodoTask

class DateInput(forms.DateInput):
    input_type = 'date'
    class Meta:
        format = '%d %b, %Y'
class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = '__all__'
        widgets = {
            'task': forms.TextInput(attrs={'placeholder': 'Task name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': '3'}),
            'label': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Select...'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'time': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reminder': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }