from django.contrib import admin
from todos.models import TodoList, TodoItem

@admin.register(TodoList)
class ToDoAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "id"
    ]

@admin.register(TodoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = [
       "task",
       "due_date",
       "is_completed",
       "list",
    ]
