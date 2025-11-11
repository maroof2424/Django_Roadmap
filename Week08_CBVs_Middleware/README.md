
# 📘 **Week 8 – Class-Based Views (CBVs) & Middleware**

**Goal:** Apna Blog App fully **CBVs** me convert karna + ek custom **middleware** banana.

---

## ✅ **Day 1 – FBVs vs CBVs (Basics)**

### 🧠 What are FBVs?

Function-based views → simple, readable, beginners ke liye perfect.

```python
def home(request):
    return render(request, "home.html")
```

### 🧠 What are CBVs?

Class-based views → reusable, structured, extendable.

```python
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")
```

### ✅ Tasks for Day 1

* FBV vs CBV difference samajhna
* `View` class use karke ek HomeView banana
* URL me `as_view()` implement karna

---

## ✅ **Day 2 – ListView & DetailView**

Today focus on **reading data** with built-in class-based views.

### 📌 ListView

* Post list display
* Search + pagination later add karenge

### 📌 DetailView

* Single post detail page
* Comments show karna

### ✅ Tasks

* `PostListView` banana
* `PostDetailView` banana
* Templates update karna (`post_list.html`, `post_detail.html`)

---

## ✅ **Day 3 – CreateView, UpdateView, DeleteView**

Aaj hum likhenge CRUD using CBVs.

### 📍 CreateView

* New post create
* Owner = `request.user`

### 📍 UpdateView

* Sirf owner edit kare (Day 4 me secure karenge)

### 📍 DeleteView

* Confirmation + redirect using `reverse_lazy()`

### ✅ Tasks

* `PostCreateView`
* `PostUpdateView`
* `PostDeleteView`

---

## ✅ **Day 4 – Mixins (LoginRequiredMixin + UserPassesTestMixin)**

Aaj tum apna Blog App **secure** banaoge.

### ✅ LoginRequiredMixin

Unauthorized users ko login page per redirect karta hai.

### ✅ UserPassesTestMixin

Post edit/delete sirf owner kare.

Example:

```python
def test_func(self):
    return self.request.user == self.get_object().user
```

### ✅ Tasks

* Saare views me LoginRequiredMixin add karna
* Update/DeleteView me UserPassesTestMixin add karna

---

## ✅ **Day 5 – Custom Middleware**

Aaj ek real industry-level skill:

### 🎯 Middleware functions:

* Request intercept karna
* Response modify karna
* Logging
* Performance tracking

### ✅ Tasks

* `middleware.py` file create
* Har request ka URL log karna
* Username print karna
* Time measure karna

---

## ✅ **Day 6 – Convert Full Blog App to CBVs**

Aaj poori app CBVs me convert:

### ✅ Convert These

* list_posts → PostListView
* post_detail → PostDetailView
* create_post → PostCreateView
* update_post → PostUpdateView
* delete_post → PostDeleteView

### ✅ Update URLs

`path("posts/", PostListView.as_view(), name="list_posts")`

### ✅ Update Templates

* form handling with CBVs
* delete confirmation
* detail view comment form

---

## ✅ **Day 7 – Final Polish + Mini Project**

### ✅ Tasks

* Middleware logs improve
* Pagination add in ListView
* UI cleanup
* Reusable templates banana
* Errors handle karna (404, 403, etc.)
* Comments ko CBVs me convert karna (optional advanced)

### ✅ Final Mini Project Output

✅ Blog App fully CBVs me
✅ Authentication + Mixins
✅ Secure Edit/Delete
✅ Middleware working
✅ Pagination + Search
✅ Clean UI

---

## ⭐ Weekly Summary

| Topic         | Skill                          |
| ------------- | ------------------------------ |
| CBVs          | Advanced Django patterns       |
| Mixins        | Security + Access Control      |
| Middleware    | Request manipulation + logging |
| CRUD via CBVs | Professional-level Django      |
| Pagination    | User-friendly UI               |
| Final Project | Blog App (Advanced version)    |

---
