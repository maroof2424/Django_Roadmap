from django.urls import path
from . import views

urlpatterns = [
    path("",views.list_post.as_view(),name="list_post"),
]
