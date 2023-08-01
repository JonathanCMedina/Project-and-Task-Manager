from django.forms import ModelForm, forms
from tasks.models import Task




class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "start_date", "due_date", "project", "assignee"]
