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
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'time': DateInput(),
            'reminder': DateInput(),
        }