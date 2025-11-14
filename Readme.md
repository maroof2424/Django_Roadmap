# 📅 **Django 15-Week Full Roadmap**

---

## **Week 1: Django Setup & Basics**

**Goals:** Understand Django structure, URL routing, templates, static files

**Topics:**

* Install Django, create project & app
* `settings.py`, `urls.py`, `views.py` overview
* URL routing (`path`, `include`)
* Templates (`{{ }}`, `{% %}`) & template inheritance (`base.html`)
* Static files: CSS, JS, images

**Mini Project:** Hello Django (Home + About)

**Exercise:**

* Add custom CSS to Home page
* Add navigation bar with links

---

## **Week 2: Models & ORM**

**Goals:** Work with database using Django ORM

**Topics:**

* Models & fields
* `makemigrations`, `migrate`
* CRUD operations with ORM
* Querysets (`filter`, `exclude`, `order_by`)
* Display data in templates

**Mini Project:** Notes App (Add, List, Delete notes)

**Exercise:**

* Add timestamp to notes
* Add note categories

---

## **Week 3: Admin Panel & Forms**

**Goals:** Customize admin and handle forms

**Topics:**

* Register models in admin
* Customize admin (`search`, `filters`, `list_display`)
* Django Forms (`forms.Form`, `forms.ModelForm`)
* POST requests & CSRF
* Form validation (`clean_field`)

**Mini Project:** Feedback Form App

**Exercise:**

* Add validation (min/max length, email format)
* Customize form layout

---

## **Week 4: Authentication & Relationships**

**Goals:** Implement auth & user relations

**Topics:**

* Built-in User model
* Signup, login, logout
* `@login_required` decorator
* User Profiles (OneToOne relation)
* ForeignKey & ManyToMany relationships

**Mini Project:** Task Manager (per-user tasks)

**Exercise:**

* Assign tasks to users
* Filter tasks by status (Completed/Pending)

---

## **Week 5: Blog Project (Part 1)**

**Goals:** CRUD, user ownership

**Topics:**

* Create Blog app
* CRUD for posts
* Link posts to users
* Restrict edit/delete to post owners

**Mini Project:** Blog App – Post creation & management

**Exercise:**

* Add post categories
* Add post summary in list view

---

## **Week 6: Blog Project (Part 2)**

**Goals:** Comments, pagination

**Topics:**

* Add comments feature
* Comment form inside post detail page
* User auth for comments
* Pagination for posts

**Mini Project:** Blog App – Comments + Pagination

**Exercise:**

* Limit comments per user
* Display recent comments first

---

## **Week 7: To-Do & Mini E-commerce**

**Goals:** Build real-world apps

**Topics:**

* To-Do app: per-user tasks, status updates
* Mini E-commerce: products, cart, checkout simulation

**Mini Projects:**

* ✅ To-Do App
* ✅ Mini E-commerce

**Exercise:**

* Add product images & categories
* Add task due date reminder

---

## **Week 8: Class-Based Views & Middleware**

**Goals:** Speed up CRUD, understand request lifecycle

**Topics:**

* FBVs vs CBVs
* ListView, DetailView, CreateView, UpdateView, DeleteView
* Mixins (`LoginRequiredMixin`)
* Custom Middleware (logging requests)

**Mini Project:** Convert Blog App to CBVs

**Exercise:**

* Add login required to create/update post
* Create middleware to log request path & user

---

## **Week 9: Django Crispy Forms & Advanced Forms**

**Goals:** Beautiful & reusable forms

**Topics:**

* Install `django-crispy-forms`
* `FormHelper` for layouts
* Custom field ordering, submit buttons
* Reusable form components

**Mini Project:** Login/Signup + Profile Update Form using Crispy Forms

**Exercise:**

* Style forms with Bootstrap 5
* Add validation & error messages

---

## **Week 10: Django REST Framework (DRF) & API**

**Goals:** Build APIs for your apps

**Topics:**

* Install DRF
* Serializers & APIView
* ModelSerializer & ViewSets
* CRUD API
* Deploy API (Railway/Heroku/Render)

**Mini Project:** Blog REST API

**Exercise:**

* Create API for posts & comments
* Secure API with token authentication

---

## **Week 11: Signals & Caching**

**Goals:** Automation & performance

**Topics:**

* Signals → auto-create profile
* Signals for email notifications
* Caching: per-view, template fragment, Redis

**Mini Project:** Blog with Signals + Caching

**Exercise:**

* Cache popular posts
* Send email on new post creation

---

## **Week 12: Testing & Async**

**Goals:** Build robust & real-time apps

**Topics:**

* Django `TestCase`
* Pytest with Django
* Django Channels → WebSockets
* Real-time chat/notifications

**Mini Project:** Chat App with Channels

**Exercise:**

* Test login & chat endpoints
* Add real-time notifications for new messages

---

## **Week 13: Submodules Deep Dive**

**Goals:** Explore important Django utilities

**Topics:**

* File uploads → `FileField`, `ImageField`
* Django messages framework
* Custom template tags & filters
* Email sending
* Management commands
* Internationalization (i18n) & Localization (l10n)

**Mini Project:** Feedback + File Upload App with Messages

**Exercise:**

* Send confirmation email after feedback
* Display uploaded files

---

## **Week 14: Scaling, Deployment & Production**

**Goals:** Production-ready Django

**Topics:**

* Switch DB to PostgreSQL
* Redis caching
* Dockerize Django project
* Production-ready settings (`DEBUG=False`, `SECURE_*`)
* Security best practices

**Final Project Options:**

* 📚 Learning Management System (LMS)
* 💬 Social Media Clone
* 🛍️ Full E-commerce with cart + API

**Exercise:**

* Deploy final project on Railway / Render / Heroku
* Use environment variables for secret keys

---

## **Week 15: Django + ML Integration**

**Goals:** Serve ML models with Django

**Topics:**

* Train ML model (scikit-learn/XGBoost)
* Save model using `pickle`/`joblib`
* Load model in Django views or DRF API
* Build form/API to accept user input → return prediction
* Optional: Front-end integration with AJAX

**Mini Project Ideas:**

1. **Sentiment Analysis App**: Input text → return Positive/Negative/Neutral
2. **House Price Predictor**: Input features → return predicted price

**Exercise:**

* Keep ML code modular (`ml_utils.py`)
* Add input validation
* Version ML models

---

### ✅ **Roadmap Features**

* 15 weeks, beginner → advanced → ML integration
* Mini projects every week
* Hands-on coding, not just theory
* DRF + ML + Deployment included
* Submodules & Crispy Forms covered

---
