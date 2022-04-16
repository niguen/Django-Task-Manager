from django import forms
from django.forms import Textarea

from .models import Employee, Task

class TaskForm(forms.ModelForm):
    #task_name = forms.CharField(label='Task name', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    #employee = forms.ModelChoiceField(empty_label=None, label='Employee', queryset=Employee.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    #due_date = forms.DateField(label='Due Date', widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))

    class Meta:
        model = Task
        fields = '__all__'

        widgets = {
            'task_title': forms.TextInput(attrs={'class':'form-control'}),
            'employee': forms.Select(attrs={'class':'form-control'}),
            'due_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }