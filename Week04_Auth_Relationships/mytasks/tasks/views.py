from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request,"tasks/task_list.html",{'tasks':tasks})

def create_task(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")

        Task.objects.create(title=title,description=description)

        messages.success(request, "Task created successfully..")
        return redirect("task_list")
    return render(request,"tasks/task_form.html")

def update_task(request,pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.title = request.POST.get("title")
        task.completed = "completed" in request.POST
        task.save()
        messages.success(request, "Task updated successfully..")
        return redirect("task_list")
    return render(request,"tasks/task_form.html",{"task":task})

def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

