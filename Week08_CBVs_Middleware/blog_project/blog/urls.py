from django.urls import path
from . import views

urlpatterns = [
    path("",views.list_post.as_view(),name="list_post"),
    path("post_details/<int:pk>/",views.post_details.as_view(),name="post_details"),
]
