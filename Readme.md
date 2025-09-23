# 📅 Django 12-Week Roadmap (Week by Week)

---

## **Week 1: Django Setup & Basics**

* Install Django, set up first project & app
* Explore `settings.py`, `urls.py`, `views.py`
* URL routing (`path`, `include`)
* Templates basics (`{{ }}`, `{% %}`)
* Template inheritance (`base.html`)
* Static files (CSS, JS, images)

**Mini Project:** Simple "Hello Django" site with 2 pages (Home + About).

---

## **Week 2: Models & ORM**

* Define models & fields
* Run `makemigrations` & `migrate`
* Django ORM → Create, Read, Update, Delete
* Querysets (`filter`, `exclude`, `order_by`)
* Display DB data in templates

**Mini Project:** Notes App (add, list, delete notes).

---

## **Week 3: Admin Panel & Forms**

* Register models in admin
* Customize admin (search, filters, list\_display)
* Django Forms → `forms.Form` & `forms.ModelForm`
* Handle POST requests & CSRF
* Form validation (`clean_field`)

**Mini Project:** Feedback Form App.

---

## **Week 4: Authentication & Relationships**

* Built-in User model
* Signup, login, logout views
* `@login_required` decorator
* User profiles (OneToOne relation)
* ForeignKey & ManyToMany relationships

**Mini Project:** Task Manager (each user manages their own tasks).

---

## **Week 5: Blog Project (Part 1)**

* Create Blog app
* CRUD for posts
* Link posts to users
* Restrict edit/delete to post owners

**Mini Project:** Blog App – Post creation & management.

---

## **Week 6: Blog Project (Part 2)**

* Add comments feature
* Comment form inside post detail page
* User authentication for comments
* Pagination for posts

**Mini Project:** Blog App – Comments + Pagination.

---

## **Week 7: To-Do & Mini E-commerce**

* Build To-Do App (per-user tasks, status updates)
* Build Mini E-commerce (products, cart, checkout simulation)

**Mini Projects:**

* ✅ To-Do App
* ✅ Mini E-commerce

---

## **Week 8: Class-Based Views & Middleware**

* Function-based views (FBVs) vs Class-based views (CBVs)
* ListView, DetailView, CreateView, UpdateView, DeleteView
* Mixins (`LoginRequiredMixin`)
* Custom Middleware (logging requests)

**Mini Project:** Convert Blog App to CBVs.

---

## **Week 9: Django REST Framework (DRF) & Deployment**

* Install DRF
* Serializers & APIView
* ModelSerializer & ViewSets
* CRUD API with DRF
* Deploy Blog API to Railway/Render/Heroku

**Mini Project:** Blog REST API.

---

## **Week 10: Signals & Caching**

* Signals (auto-create profile when user signs up)
* Signals for email notification
* Caching → per-view, template fragment caching
* Low-level caching with Redis

**Mini Project:** Blog with signals + caching.

---

## **Week 11: Testing & Async**

* Django TestCase basics
* Pytest with Django
* Django Channels → WebSockets
* Build real-time notifications or chat app

**Mini Project:** Chat App with Django Channels.

---

## **Week 12: Scaling & Final Project**

* Switch DB to PostgreSQL
* Add Redis caching
* Dockerize Django project
* Scale app with proper settings for production

**Final Project (Pick One):**

* 📚 Learning Management System (LMS)
* 💬 Social Media Clone
* 🛍️ Full E-commerce with cart + API

