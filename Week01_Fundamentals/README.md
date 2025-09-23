# 🗓️ Week 1 – Django Fundamentals

---

## **Day 1: Setup Django**

* Create a new virtual environment inside `Week01_Fundamentals`

```powershell
cd P:\Python\Django_Roadmap\Week01_Fundamentals
python -m venv venv
.\venv\Scripts\activate
pip install django
```

* Start your first project:

```powershell
django-admin startproject myproject .
```

👉 This will create:

```
Week01_Fundamentals/
  venv/
  manage.py
  myproject/
      __init__.py
      settings.py
      urls.py
      asgi.py
      wsgi.py
```

* Run server:

```powershell
python manage.py runserver
```

---

## **Day 2: Apps & Views**

* Create your first app:

```powershell
python manage.py startapp home
```

* Add `"home"` to `INSTALLED_APPS` in `settings.py`.
* In `home/views.py`:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django 🚀")
```

* In `myproject/urls.py`:

```python
from django.urls import path
from home.views import index

urlpatterns = [
    path('', index, name='home'),
]
```

---

## **Day 3: Templates Basics**

* Create `templates/` folder inside `home/`.
* Add in `settings.py`:

```python
'DIRS': [BASE_DIR / "home" / "templates"]
```

* Create `home/templates/home/index.html`:

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Hello from Template 🚀</h1>
  </body>
</html>
```

* Update `views.py`:

```python
from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")
```

---

## **Day 4: Template Inheritance**

* Create `base.html` in `templates/`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}My Site{% endblock %}</title>
  </head>
  <body>
    <header><h1>My Site Header</h1></header>
    <main>
      {% block content %}{% endblock %}
    </main>
    <footer>© 2025</footer>
  </body>
</html>
```

* Update `index.html`:

```html
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
<h2>Welcome to Django!</h2>
{% endblock %}
```

---

## **Day 5: Static Files**

* In `settings.py`:

```python
STATICFILES_DIRS = [BASE_DIR / "home" / "static"]
```

* Create `home/static/css/style.css`:

```css
body { font-family: Arial; background: #f4f4f4; }
h1 { color: darkblue; }
```

* Link it in `base.html`:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

## **Day 6: Models & Migrations (Intro)**

* In `home/models.py`:

```python
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

* Run migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

## **Day 7: Mini Project – Notes App (Basic)**

* Register model in `admin.py`:

```python
from django.contrib import admin
from .models import Note

admin.site.register(Note)
```

* Create superuser:

```powershell
python manage.py createsuperuser
```

* Run server, log into `/admin`, add notes, and display them in a template:

```python
# views.py
from .models import Note

def notes_list(request):
    notes = Note.objects.all()
    return render(request, "home/notes_list.html", {"notes": notes})
```

```html
<!-- notes_list.html -->
{% extends "base.html" %}
{% block title %}Notes{% endblock %}
{% block content %}
  <h2>Notes</h2>
  <ul>
    {% for note in notes %}
      <li><b>{{ note.title }}</b> - {{ note.content }}</li>
    {% endfor %}
  </ul>
{% endblock %}
```

---

✅ By the end of Week 1:

* You’ll know how to start a Django project, create apps, use templates, static files, and define your first model.
* You’ll have a **Notes App** with an admin panel + template rendering.

---
