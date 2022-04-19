from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'task_title': forms.TextInput(attrs={'class':'form-control'}),
            'employee': forms.Select(attrs={'class':'form-control'}),
            'due_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }