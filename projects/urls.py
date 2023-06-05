from django.urls import path
from projects.views import project

urlpatterns = [
    path("", project, name="list_projects")
]
