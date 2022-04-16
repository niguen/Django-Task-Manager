from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from .models import Task, Employee
from django.contrib import messages
from .forms import TaskForm



class IndexView(generic.ListView):
    template_name = 'taskManager/index.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Return the last five tasks."""
        return Task.objects.order_by('task_title').order_by('due_date')


def add_task(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TaskForm()

    return render(request, 'taskManager/addTask.html', {'form': form})

def delete_task(request, pk):
    messages.info(request, 'Your password has been changed successfully!')
    Task.objects.get(pk=pk).delete()
    return redirect('taskManager:index')