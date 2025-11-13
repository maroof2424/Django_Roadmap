from django.urls import path
from . import views

urlpatterns = [
    path("",views.ListPostView.as_view(),name="list_post"),
    path("post_details/<int:pk>/",views.PostDetailsView.as_view(),name="post_details"),
    path("create_post/new/",views.CreatePostView.as_view(),name="create_post"),
    path("update_post/<int:pk>/",views.UpdatePostView.as_view(),name="update_post"),
    path("delete_post/<int:pk>/",views.DeletePostView.as_view(),name="delete_post"),
]
