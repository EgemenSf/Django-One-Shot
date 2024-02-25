from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import ToDoCreateForm, EditForm, CreatTaskForm, EditTaskForm

def todo_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_lists": todo_lists,
    }

    return render(request, "todos/todo_list.html", context)


def show_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list": todo_list,
    }

    return render(request, "todos/detail.html", context)



def create_todo(request):
    if request.method == "POST":
        create_form = ToDoCreateForm(request.POST)
        if create_form.is_valid():
            newlist = create_form.save()
            return redirect("todo_list_detail", newlist.id)
    else:
        create_form = ToDoCreateForm()
        context = {
            "create_form": create_form,
        }

        return render(request, "todos/creat.html", context)



def edit_todo_list(request, id):
    list = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        edit_form = EditForm(request.POST, instance=list)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("todo_list_detail", id=id)

    else:
        edit_form = EditForm(instance=list)

    context = {
        "list_object": list,
        "edit_form": edit_form
    }

    return render(request, "todos/edit.html", context)


def delete_list(request, id):
    deleting = TodoList.objects.get(id=id)
    if request.method == "POST":
        deleting.delete()
        return redirect("todo_list_list")

    return render(request, "todos/delete.html")


def create_task(request):
    if request.method == "POST":
        task_form = CreatTaskForm(request.POST)
        if task_form.is_valid():
            item = task_form.save()
            return redirect("todo_list_detail", id=item.list.id)

    else:
        task_form = CreatTaskForm()
        context = {
            "task_form": task_form
        }

        return render(request, "todos/createtask.html", context)


def edit_task(request, id):
    task = get_object_or_404(TodoItem, id=id)
    if request.method == "POST":
        edit_task_form = EditTaskForm(request.POST, instance=task)
        if edit_task_form.is_valid():
            edited = edit_task_form.save()
            return redirect("todo_list_detail", id=edited.list.id)
    else:
        edit_task_form = EditTaskForm(instance=task)

    context = {
        "edit_task_form": edit_task_form
    }

    return render(request, "todos/edit_task.html", context)
