## 🗓️ **WEEK 6 — Blog Project (Part 2: Comments + Pagination)**

**Goal:** Add a real comment system, restrict actions to logged-in users, and handle long post lists cleanly with pagination.

---

### **🧠 Day 1 – Setup Comments Model**

**Focus:** Build DB structure for comments.

**Tasks**

* Open your `models.py`
* Add `Comment` model:

  ```python
  class Comment(models.Model):
      post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
  ```
* Run:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
* Add a few dummy comments via Django admin to verify.

**Mini Test:** Go to `/admin` → check if `Comment` appears.

---

### **💬 Day 2 – Post Detail + Display Comments**

**Focus:** Show comments under posts.

**Tasks**

* In `views.py`, create `post_detail` view:

  ```python
  def post_detail(request, pk):
      post = Post.objects.get(pk=pk)
      comments = post.comments.all().order_by('-created_at')
      return render(request, "blog/post_detail.html", {"post": post, "comments": comments})
  ```
* Create `post_detail.html`:

  ```html
  <h2>{{ post.title }}</h2>
  <p>{{ post.content }}</p>
  <hr>
  <h4>Comments</h4>
  {% for c in comments %}
    <p><b>{{ c.user.username }}</b>: {{ c.content }}</p>
  {% empty %}
    <p>No comments yet.</p>
  {% endfor %}
  ```
* Add route:

  ```python
  path("post/<int:pk>/", views.post_detail, name="post_detail")
  ```

**Mini Test:** Visit a post → you should see dummy comments from admin.

---

### **✍️ Day 3 – Add Comment Form (with Auth)**

**Focus:** Let users post comments directly.

**Tasks**

* Update `post_detail` view:

  ```python
  if request.method == "POST":
      if not request.user.is_authenticated:
          messages.error(request, "Login required to comment!")
          return redirect("login")

      Comment.objects.create(
          post=post,
          user=request.user,
          content=request.POST.get("content")
      )
      messages.success(request, "Comment added!")
      return redirect("post_detail", pk=pk)
  ```
* Update template:

  ```html
  {% if request.user.is_authenticated %}
    <form method="POST">{% csrf_token %}
      <textarea name="content" required class="form-control"></textarea>
      <button class="btn btn-primary mt-2">Add Comment</button>
    </form>
  {% else %}
    <p><a href="{% url 'login' %}">Login</a> to comment.</p>
  {% endif %}
  ```

**Mini Test:** Login → add a comment → reload → should appear.

---

### **📑 Day 4 – Pagination for Posts**

**Focus:** Handle large post lists gracefully.

**Tasks**

* Update `list_posts` view:

  ```python
  from django.core.paginator import Paginator

  def list_posts(request):
      posts = Post.objects.all().order_by('-created_at')
      paginator = Paginator(posts, 5)
      page = request.GET.get('page')
      page_obj = paginator.get_page(page)
      return render(request, "blog/list_posts.html", {"page_obj": page_obj})
  ```
* In `list_posts.html`, replace loop:

  ```html
  {% for post in page_obj %}
    <h4>{{ post.title }}</h4>
    <p>{{ post.content|truncatewords:20 }}</p>
  {% endfor %}

  <div class="pagination">
    {% if page_obj.has_previous %}
      <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
    {% endif %}
    <span>Page {{ page_obj.number }}</span>
    {% if page_obj.has_next %}
      <a href="?page={{ page_obj.next_page_number }}">Next</a>
    {% endif %}
  </div>
  ```

**Mini Test:** Add 10+ posts → check page numbers.

---

### **🧩 Day 5 – Polish & Protect**

**Focus:** UX, access rules, and testing.

**Tasks**

* Restrict comment form to logged-in users only.
* Add delete/edit buttons for comments (optional).
* Style with Bootstrap.
* Test:

  * Guest can read posts & comments.
  * Only logged-in users can comment.
  * Pagination works without breaking links.

**Mini Project Deliverable:**
✅ Fully working blog with

* Post CRUD
* Comments per post
* Pagination
* Auth checks
* Bootstrap UI

---
