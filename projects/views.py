from django.shortcuts import render
from projects.models import Project
# Create your views here.

def project(request):
    projects = Project.objects.all
    context = {
        "projects": projects
    }
    return render(request, "projects/projects.html", context)
