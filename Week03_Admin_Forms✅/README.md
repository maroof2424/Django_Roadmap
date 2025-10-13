
# 🧭 Week 3 – Admin Panel & Forms

**Goal:** Learn Django Admin customization and form handling (both `forms.Form` and `forms.ModelForm`).

---

## 🗓️ Weekly Overview

| Day | Topic | Focus |
|-----|--------|--------|
| 1 | Admin Panel Setup | Register models, customize list display, filters, search |
| 2 | Django Forms (forms.Form) | Create and validate plain Django forms |
| 3 | ModelForm | Auto-generate forms using models |
| 4 | Validation | Add custom field validation (clean methods) |
| 5 | Display Feedback List | Render submitted feedback on a page |
| 6 | Styling | Add Bootstrap and improve UI |
| 7 | Mini Project | Build Feedback Form App |

---

## 📁 Project Structure
```

Week03_Admin_Forms/
│
├── feedback/
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── feedback_form.html
│   │   └── feedback_list.html
│   └── static/
│       └── css/style.css
│
├── manage.py
└── README.md
```

---

## 🧩 Day 1 – Admin Panel Setup

- Create a `Feedback` model with name, email, rating, and message fields.
- Register it in `admin.py`:
  ```python
  from django.contrib import admin
  from .models import Feedback

  @admin.register(Feedback)
  class FeedbackAdmin(admin.ModelAdmin):
      list_display = ('name', 'email', 'rating', 'created_at')
      search_fields = ('name', 'email')
      list_filter = ('rating',)


 Run:

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  ```
* Open `/admin` and test it.

---

## 🧩 Day 2 – Django Forms (forms.Form)

Create a `forms.py`:

```python
from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=5)
    message = forms.CharField(widget=forms.Textarea)
```

Use it in `views.py`:

```python
from .forms import FeedbackForm
from django.shortcuts import render

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = FeedbackForm()
    return render(request, "feedback/feedback_form.html", {"form": form})
```

---

## 🧩 Day 3 – ModelForm

Create model:

```python
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"
```

Update form:

```python
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
```

---

## 🧩 Day 4 – Validation

Add validation to form:

```python
def clean_email(self):
    email = self.cleaned_data.get("email")
    if not email.endswith(".com"):
        raise forms.ValidationError("Email must end with .com")
    return email
```

---

## 🧩 Day 5 – Display Feedback List

In `views.py`:

```python
from .models import Feedback

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, "feedback/feedback_list.html", {"feedbacks": feedbacks})
```

Template example:

```html
{% extends "base.html" %}
{% block title %}All Feedback{% endblock %}
{% block content %}
<h2>All Feedback</h2>
<ul>
  {% for fb in feedbacks %}
    <li><b>{{ fb.name }}</b> ({{ fb.rating }}/5) - {{ fb.message }}</li>
  {% empty %}
    <li>No feedback yet.</li>
  {% endfor %}
</ul>
{% endblock %}
```

---

## 🧩 Day 6 – Add Bootstrap

* Add Bootstrap 5 CDN in `base.html`
* Style your form and list pages using Bootstrap cards and tables.

---

## 🧩 Day 7 – Mini Project: Feedback Form App

✅ **Features:**

* Submit feedback through a form
* Admin panel to view and filter feedback
* Frontend list of all feedback entries
* Bootstrap styling
* Custom validation

---

## ✅ Deliverables

* `/admin` working with Feedback model
* Feedback form (manual + ModelForm)
* Validation
* Frontend feedback list
* Bootstrap-styled templates

---