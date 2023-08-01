from django.urls import path
from tasks.views import create_task, view_my_tasks, edit_my_tasks

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", view_my_tasks, name="show_my_tasks"),
    path("edit/<int:id>/", edit_my_tasks, name="edit_my_tasks")
]
