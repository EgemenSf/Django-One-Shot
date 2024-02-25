from django.forms import ModelForm
from todos.models import TodoList, TodoItem

class ToDoCreateForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name"
        ]

class EditForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name"
        ]

class CreatTaskForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "task",
            "due_date",
            "is_completed",
            "list"
        ]

class EditTaskForm(ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            "task",
            "due_date",
            "is_completed",
            "list"
        ]
