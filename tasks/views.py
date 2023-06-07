from django.shortcuts import render, redirect
from tasks.forms import CreateTaskForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
# feature 15
@login_required
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.assignee = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


@login_required
def view_tasks(request):
    tasks_view = Task.objects.filter(assignee=request.user)
    context = {"tasks_view": tasks_view}
    return render(request, "tasks/view_tasks.html", context)


# @login_required
# def show_project(request, id):
#     project = get_object_or_404(Project, id=id)
#     # project = Project.objects.filter(owner=request.user)
#     context = {
#         "project_object": project
#     }
#     return render(request, "projects/show_project.html", context)
