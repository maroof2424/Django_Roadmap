from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def list_tasks(request):
    tasks = Todo.objects.all().order_by("-created_at")
    return render(request, "todo/list_tasks.html", {"tasks": tasks})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  
            task.user = request.user  
            task.save()

            messages.success(request, "Task created successfully ✅")
            return redirect("list_tasks")
    else:
        form = TodoForm()

    return render(request, "todo/forms.html", {"form": form})

@login_required
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

    return render(request, "todo/forms.html", {"form": form, "task": task})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted ✅")
        return redirect("list_tasks")

    return render(request, "todo/confirm_delete.html", {"task": task})
