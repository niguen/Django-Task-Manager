from django.db import models
from datetime import date
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    due_date = models.DateField('Due Date')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title

    @property
    def is_past_due(self):
        return date.today() > self.due_date
