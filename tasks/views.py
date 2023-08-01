from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect("projects_list")
    else:
        form = CreateTaskForm()
    context = {"form": form}
    return render(request, "tasks/create_task.html", context)


@login_required
def view_my_tasks(request):
    view_my_tasks = Task.objects.filter(assignee=request.user)
    context = {"view_my_tasks": view_my_tasks}
    return render(request, "tasks/view_my_tasks.html", context)

@login_required
def edit_my_tasks(request, id):
    edit = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = CreateTaskForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks", id=id)
    else:
        form = CreateTaskForm(instance=edit)
    context = {
        "task_object": edit,
        "form": form
    }
    return render(request, "tasks/edit_my_tasks.html", context)
