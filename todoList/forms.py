from django import forms
from django.db.models import fields

from .models import TodoTask

class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = '__all__'