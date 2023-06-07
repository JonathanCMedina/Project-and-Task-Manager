from django.urls import path
from projects.views import project, show_project, create_project

# feature 13 step 3
urlpatterns = [
    path("", project, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
]
