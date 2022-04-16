from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('taskManager.urls')),
    path('admin/', admin.site.urls),
]