from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task
    # path('',views.task_list,name="task_list"),
    # path('create_task/',views.create_task,name="create_task"),
    # path('update_task/<int:pk>/',views.update_task,name="update_task"),
    # path('delete_task/<int:pk>/',views.delete_task,name="delete_task"),
    # path('signup/', views.signup_view, name='signup'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),

login_required(login_url="login")
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    return render(request,"tasks/task_list.html",{"tasks":tasks})

login_required(login_url="login")
def create_task(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")
        Task.objects.create(title=title,description=description)
        messages.success(request,"Task Created Successfully...")
        return redirect("task_list")
    return redirect(request,"tasks/task_form.html")

login_required(login_url="login")
def update_task(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.completed = "completed" in request.POST
        task.save()
        messages.success(request,"Task Updated successfully...")
        return redirect("task_list")
    return render(request,"tasks/task_form.html",{"task":task})

login_required(login_url="login")
def delete_task(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request,"task_confirm_delete.html",{"task":task})

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request,"Password do not match.")
            return redirect("signup")
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exist...")
        
        user = User.objects.create_user(username,username,password,password)
        user.save()
        messages.success(request,"account created successfully...")
        return redirect("login")
    return render(request,"tasks/auth.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request,username=username,password=password)

        if user:
            login(request, user)
            messages.success(request, "User login successfully...")
            return redirect("task_list")
        else:
            messages.error(request, "❌ Invalid credentials.")
            return redirect("login")

    return render(request, "tasks/auth.html")

def logout_view(request):
    logout(request)
    messages.info(request,"Logged out successfully...")
    return redirect("login")