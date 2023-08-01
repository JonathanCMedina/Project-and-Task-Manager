from django.urls import path
from projects.views import projects_list, project_detail
from projects.views import edit_project, create_project

# feature 13 step 3
urlpatterns = [
    path("", projects_list, name="projects_list"),
    path("<int:id>/", project_detail, name="project_detail"),
    path("create/", create_project, name="create_project"),
    path("edit/<int:id>/", edit_project, name="edit_project")
]
