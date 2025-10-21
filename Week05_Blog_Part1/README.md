## 🗓️ **Week 5 – Blog Project (Part 1)**

### **📅 Day 1 – Setup & Models**

**Goal:** Set up a new `blog` app and define your models.
**Tasks:**

1. `python manage.py startapp blog`
2. Add `'blog'` in `INSTALLED_APPS` inside `settings.py`
3. In `blog/models.py`:

   ```python
   from django.db import models
   from django.contrib.auth.models import User

   class Post(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
       title = models.CharField(max_length=200)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)

       def __str__(self):
           return self.title
   ```
4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Register model in `admin.py`:

   ```python
   from .models import Post
   admin.site.register(Post)
   ```

---

### **📅 Day 2 – CRUD Views (Create, Read, Update, Delete)**

**Goal:** Create basic views and templates.
**Files:** `blog/views.py`, `blog/urls.py`

1. In `views.py`:

   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from django.contrib.auth.decorators import login_required
   from django.contrib import messages
   from .models import Post

   def post_list(request):
       posts = Post.objects.all().order_by('-created_at')
       return render(request, 'blog/post_list.html', {'posts': posts})

   @login_required
   def create_post(request):
       if request.method == "POST":
           title = request.POST.get("title")
           content = request.POST.get("content")
           Post.objects.create(user=request.user, title=title, content=content)
           messages.success(request, "Post created successfully!")
           return redirect("post_list")
       return render(request, "blog/post_form.html")

   @login_required
   def update_post(request, pk):
       post = get_object_or_404(Post, pk=pk, user=request.user)
       if request.method == "POST":
           post.title = request.POST.get("title")
           post.content = request.POST.get("content")
           post.save()
           messages.success(request, "Post updated successfully!")
           return redirect("post_list")
       return render(request, "blog/post_form.html", {"post": post})

   @login_required
   def delete_post(request, pk):
       post = get_object_or_404(Post, pk=pk, user=request.user)
       if request.method == "POST":
           post.delete()
           messages.info(request, "Post deleted successfully!")
           return redirect("post_list")
       return render(request, "blog/post_confirm_delete.html", {"post": post})
   ```

2. `blog/urls.py`:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.post_list, name='post_list'),
       path('create/', views.create_post, name='create_post'),
       path('update/<int:pk>/', views.update_post, name='update_post'),
       path('delete/<int:pk>/', views.delete_post, name='delete_post'),
   ]
   ```

3. Include `blog.urls` in your **main project’s** `urls.py`:

   ```python
   path('blog/', include('blog.urls')),
   ```

---

### **📅 Day 3 – Templates with Bootstrap**

**Goal:** Build clean templates for your blog pages.
Make a `templates/blog/` folder with these files:

* `post_list.html`
* `post_form.html`
* `post_confirm_delete.html`

Example for `post_list.html`:

```html
{% extends 'base.html' %}
{% block content %}
<div class="container mt-5">
  <div class="d-flex justify-content-between align-items-center mb-4">
    <h2>All Posts</h2>
    <a href="{% url 'create_post' %}" class="btn btn-primary">+ New Post</a>
  </div>
  {% for post in posts %}
    <div class="card mb-3 shadow-sm">
      <div class="card-body">
        <h5 class="card-title">{{ post.title }}</h5>
        <p class="card-text">{{ post.content|truncatechars:150 }}</p>
        <small class="text-muted">By {{ post.user.username }} • {{ post.created_at|date:"M d, Y" }}</small><br>
        {% if post.user == request.user %}
          <a href="{% url 'update_post' post.pk %}" class="btn btn-sm btn-outline-warning mt-2">Edit</a>
          <a href="{% url 'delete_post' post.pk %}" class="btn btn-sm btn-outline-danger mt-2">Delete</a>
        {% endif %}
      </div>
    </div>
  {% empty %}
    <p>No posts yet.</p>
  {% endfor %}
</div>
{% endblock %}
```

---

### **📅 Day 4 – Restrict Edit/Delete to Owners**

Already handled in the views:

```python
post = get_object_or_404(Post, pk=pk, user=request.user)
```

This ensures only the post creator can edit or delete.

---

### **📅 Day 5 – Final Touch & Testing**

**Goal:**
✅ Test all CRUD routes
✅ Check ownership restriction
✅ Add success/error messages
✅ Polish UI with Bootstrap alerts

---

### 💡 Mini Project Goal:

By the end of Week 5, you’ll have:

> A fully functional Blog App with CRUD, user link, and ownership restrictions.

---