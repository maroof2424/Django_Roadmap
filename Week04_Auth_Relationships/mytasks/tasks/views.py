from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request,"tasks/task_list.html",{'tasks':tasks})

@login_required(login_url='login')
def create_task(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")

        Task.objects.create(title=title,description=description)

        messages.success(request, "Task created successfully..")
        return redirect("task_list")
    return render(request,"tasks/task_form.html")

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_task(request,pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request, "⚠️ Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username already taken.")
            return redirect("signup")

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "✅ Account created! Please log in.")
        return redirect("login")

    return render(request, "tasks/signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("task_list")
        else:
            messages.error(request, "❌ Invalid credentials.")
            return redirect("login")

    return render(request, "tasks/login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "👋 Logged out successfully.")
    return redirect("login")


