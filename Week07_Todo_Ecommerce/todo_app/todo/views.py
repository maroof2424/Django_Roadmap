from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo


def list_tasks(request):
    tasks = Todo.objects.all().order_by("-created_at")
    return render(request, "todo/list_tasks.html", {"tasks": tasks})


def create_task(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully ✅")
            return redirect("list_tasks")
    else:
        form = TodoForm()

    return render(request, "todo/form.html", {"form": form})


def update_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated ✅")
            return redirect("list_tasks")
    else:
        form = TodoForm(instance=task)

    return render(request, "todo/form.html", {"form": form, "task": task})


def delete_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted ✅")
        return redirect("list_tasks")

    return render(request, "todo/confirm_delete.html", {"task": task})
