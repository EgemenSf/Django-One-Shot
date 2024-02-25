from django.urls import path
from todos.views import todo_list, show_todo_list, create_todo, edit_todo_list, delete_list, create_task, edit_task

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("create/", create_todo, name="todo_list_create"),
    path("<int:id>/edit/", edit_todo_list, name="todo_list_update"),
    path("<int:id>/delete/", delete_list, name="todo_list_delete"),
    path("items/create/", create_task, name="todo_item_create"),
    path("items/<int:id>/edit/", edit_task, name="todo_item_update"),
    path("<int:id>/", show_todo_list, name="todo_list_detail")
]



