from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_posts, name="list_posts"),
    path("post/create/", views.create_post, name="create_post"),
    path("post/<int:pk>/edit/", views.update_post, name="update_post"),
    path("post/<int:pk>/delete/", views.delete_post, name="delete_post"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
