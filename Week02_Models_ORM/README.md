

# **Week 2: Models & ORM (Manual CRUD)**

## **Day 1 – Models & Migrations**

* Create `Note` model in `home/models.py`:

  ```python
  from django.db import models

  class Note(models.Model):
      title = models.CharField(max_length=200)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
          return self.title
  ```
* Run:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

## **Day 2 – ORM Basics**

Shell practice:

```bash
python manage.py shell
```

Examples:

```python
from home.models import Note
# Create
Note.objects.create(title="First Note", content="This is my first note")
# Read
Note.objects.all()
# Filter
Note.objects.filter(title__icontains="first")
# Update
note = Note.objects.first()
note.title = "Updated Title"
note.save()
# Delete
note.delete()
```

---

## **Day 3 – List Notes (Read)**

`views.py`:

```python
from django.shortcuts import render
from .models import Note

def notes_list(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request, "home/notes_list.html", {"notes": notes})
```

`notes_list.html`:

```html
{% extends "base.html" %}
{% block content %}
  <h2>All Notes</h2>
  <ul>
    {% for note in notes %}
      <li>{{ note.title }} - {{ note.content }}</li>
    {% empty %}
      <li>No notes yet.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

---

## **Day 4 – Create Note (Manual Form)**

`create_note.html`:

```html
{% extends "base.html" %}
{% block content %}
  <h2>Add Note</h2>
  <form method="post">
    {% csrf_token %}
    <input type="text" name="title" placeholder="Title"><br><br>
    <textarea name="content" placeholder="Content"></textarea><br><br>
    <button type="submit">Save</button>
  </form>
{% endblock %}
```

`views.py`:

```python
from django.shortcuts import redirect

def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Note.objects.create(title=title, content=content)
        return redirect("notes_list")
    return render(request, "home/create_note.html")
```

`urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_list, name="notes_list"),
    path("create/", views.create_note, name="create_note"),
]
```

---

## **Day 5 – Delete Note**

`views.py`:

```python
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect("notes_list")
```

`urls.py`:

```python
path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
```

`notes_list.html`:

```html
{% for note in notes %}
  <li>
    <b>{{ note.title }}</b> - {{ note.content }}
    <a href="{% url 'delete_note' note.id %}">❌ Delete</a>
  </li>
{% endfor %}
```

---

## **Day 6 – Update Note**

`update_note.html`:

```html
{% extends "base.html" %}
{% block content %}
  <h2>Edit Note</h2>
  <form method="post">
    {% csrf_token %}
    <input type="text" name="title" value="{{ note.title }}"><br><br>
    <textarea name="content">{{ note.content }}</textarea><br><br>
    <button type="submit">Update</button>
  </form>
{% endblock %}
```

`views.py`:

```python
def update_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        return redirect("notes_list")
    return render(request, "home/update_note.html", {"note": note})
```

`urls.py`:

```python
path("update/<int:note_id>/", views.update_note, name="update_note"),
```

---

## **Day 7 – Mini Project Wrap**

* Features covered ✅

  * Add Note
  * List Notes
  * Update Note
  * Delete Note
* Manual forms used, no Django `ModelForm`.
* ORM fully practiced.

---

⚡ By end of Week 2 → You’ll be fully comfortable with **Django ORM + manual CRUD**.

---
