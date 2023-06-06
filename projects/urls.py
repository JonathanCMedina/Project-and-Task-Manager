from django.urls import path
from projects.views import project, show_project

#feature 13 step 3
urlpatterns = [
    path("", project, name="list_projects"),
    path("<int:id>/", show_project, name="show_project")
]
