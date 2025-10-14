## 📅 **Week 4: Authentication & Relationships**

**Goal:** Build a **Task Manager App** — where users can **sign up, log in, log out**, and manage their **own tasks** (private to each user).

---

### 🧩 **Folder Setup**

```
Week04_Auth_Relationships/
├── venv/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── tasks/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── tasks/
    │       ├── task_list.html
    │       ├── task_form.html
    │       ├── signup.html
    │       ├── login.html
    │       └── base.html
```

---

## 🧱 **Day 1 – User Authentication Setup**

* Create a new app:

  ```bash
  python manage.py startapp tasks
  ```

* Add `tasks` to `INSTALLED_APPS` in `settings.py`.

* Add this in `myproject/urls.py`:

  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('tasks.urls')),
  ]
  ```

---

## 🔐 **Day 2 – Signup, Login, Logout**

* Use Django’s built-in `User` model and `AuthenticationForm`.

**`tasks/views.py`**

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
```

---

**`tasks/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.task_list, name='task_list'),
]
```

---

## ✅ **Day 3 – Task Model & One-to-Many Relationship**

Each task belongs to a single user.

**`tasks/models.py`**

```python
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Migrate:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ⚙️ **Day 4 – CRUD Views with @login_required**

**`tasks/views.py`**

```python
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST.get('description', '')
        Task.objects.create(user=request.user, title=title, description=desc)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')
```

---

## 🎨 **Day 5 – Templates (Bootstrap + Auth Links)**

**`base.html`**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{% block title %}Task Manager{% endblock %}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<nav class="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm">
  <div class="container">
    <a class="navbar-brand" href="{% url 'task_list' %}">TaskManager</a>
    <div class="navbar-nav">
      {% if user.is_authenticated %}
        <a class="nav-link" href="{% url 'task_list' %}">My Tasks</a>
        <a class="nav-link" href="{% url 'logout' %}">Logout</a>
      {% else %}
        <a class="nav-link" href="{% url 'login' %}">Login</a>
        <a class="nav-link" href="{% url 'signup' %}">Signup</a>
      {% endif %}
    </div>
  </div>
</nav>

<div class="container py-5">
  {% block content %}{% endblock %}
</div>

</body>
</html>
```

---

**`signup.html` & `login.html`**

```html
{% extends "base.html" %}
{% block content %}
<div class="col-md-4 offset-md-4">
  <div class="card shadow-sm">
    <div class="card-body">
      <h4 class="text-center mb-3">{% if request.path == '/signup/' %}Sign Up{% else %}Login{% endif %}</h4>
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button class="btn btn-primary w-100 mt-2">Submit</button>
      </form>
    </div>
  </div>
</div>
{% endblock %}
```

---

**`task_list.html`**

```html
{% extends "base.html" %}
{% block title %}My Tasks{% endblock %}
{% block content %}
<h2 class="mb-3">🧩 My Tasks</h2>

<form method="post" action="{% url 'add_task' %}">
  {% csrf_token %}
  <div class="input-group mb-3">
    <input type="text" name="title" class="form-control" placeholder="New Task" required>
    <button class="btn btn-success" type="submit">Add</button>
  </div>
</form>

<ul class="list-group">
  {% for task in tasks %}
    <li class="list-group-item d-flex justify-content-between align-items-center">
      <span>
        {% if task.completed %}
          <del>{{ task.title }}</del>
        {% else %}
          {{ task.title }}
        {% endif %}
      </span>
      <span class="badge bg-secondary">{{ task.created_at|date:"M d" }}</span>
    </li>
  {% empty %}
    <li class="list-group-item text-center">No tasks yet 😅</li>
  {% endfor %}
</ul>
{% endblock %}
```

---

## 🚀 **Day 6 – User Profiles (OneToOne) + Relationships**

You can extend users with a profile:

```python
# models.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

---

## 🧩 **Mini Project Summary – Task Manager**

✅ Sign Up / Login / Logout
✅ Add, view, and manage personal tasks
✅ Authenticated access only (`@login_required`)
✅ One-to-Many (User → Tasks)
✅ Optional Profile (OneToOne)

---