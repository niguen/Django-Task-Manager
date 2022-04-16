from django.urls import path

from . import views

app_name = 'taskManager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addTask/', views.add_task, name='addTask'),
    path('delete/<int:pk>', views.delete_task, name='delete'),
]