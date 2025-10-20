from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task, Profile


@login_required(login_url="login")
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


@login_required(login_url="login")
def create_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(user=request.user, title=title, description=description)
        messages.success(request, "✅ Task created successfully!")
        return redirect("task_list")
    return render(request, "tasks/task_form.html")


@login_required(login_url="login")
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.completed = "completed" in request.POST
        task.save()
        messages.success(request, "✅ Task updated successfully!")
        return redirect("task_list")
    return render(request, "tasks/task_form.html", {"task": task})


@login_required(login_url="login")
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.success(request, "🗑️ Task deleted.")
        return redirect("task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})


@login_required(login_url='login')
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "tasks/profile.html", {"profile": profile})

@login_required(login_url='login')
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        bio = request.POST.get("bio")
        location = request.POST.get("location")
        profile.bio = bio
        profile.location = location
        profile.save()

        messages.success(request, "Profile updated successfully ✅")
        return redirect("profile")

    return render(request, "tasks/edit_profile.html", {"profile": profile})


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request, "⚠️ Passwords do not match.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email,password=password)
        Profile.objects.create(user=user)
        messages.success(request, "✅ Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "tasks/auth.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "🎉 Logged in successfully!")
            return redirect("task_list")
        else:
            messages.error(request, "❌ Invalid credentials.")
            return redirect("login")

    return render(request, "tasks/auth.html")


def logout_view(request):
    logout(request)
    messages.info(request, "👋 Logged out successfully.")
    return redirect("login")
