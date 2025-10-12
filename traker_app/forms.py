from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority', 'date_limit']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']