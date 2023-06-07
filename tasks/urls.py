from django.urls import path
from tasks.views import create_task, view_tasks

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", view_tasks, name="show_my_tasks"),
]
