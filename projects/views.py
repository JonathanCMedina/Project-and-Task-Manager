from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
# Create your views here.

#feature 5, technically the "list" or "home" page
#html is created as the projects.html
#url is created as "" and name="home"
#Feature 8 is responsible for the login_required decorator
#and the filter on the projects = line
@login_required
def project(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects
    }
    return render(request, "projects/projects.html", context)

#feature 13
@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    # project = Project.objects.filter(owner=request.user)
    context = {
        "project_object": project
    }
    return render(request, "projects/show_project.html", context)
