from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import CreateProjectForm
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

#feature 14
@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = CreateProjectForm()
    context = {
        "form": form
    }
    return render(request, "projects/create_project.html", context)
