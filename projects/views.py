from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import CreateProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.


# feature 5, technically the "list" or "home" page
# html is created as the projects.html
# url is created as "" and name="home"
# Feature 8 is responsible for the login_required decorator
# and the filter on the projects = line
@login_required
def projects_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects_list": projects}
    return render(request, "projects/projects_list.html", context)


# feature 13
@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    # project = Project.objects.filter(owner=request.user)
    context = {"project_object": project}
    return render(request, "projects/project_detail.html", context)


# feature 14
@login_required
def create_project(request):
    if request.method == "POST":
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("projects_list")
    else:
        form = CreateProjectForm()
    context = {"form": form}
    return render(request, "projects/create_project.html", context)

@login_required
def edit_project(request, id):
    edit = get_object_or_404(Project, id=id)
    if request.method == "POST":
        form = CreateProjectForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect("projects_list", id=id)
    else:
        form = CreateProjectForm(instance=edit)
    context = {
        "project_object": edit,
        "form": form
    }
    return render(request, "projects/edit_project.html", context)
