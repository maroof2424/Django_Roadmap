from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_posts,name="list_posts"),
    path('create_task/',views.create_post,name="create_post"),
    path('update_task/<int:pk>/',views.update_post,name="update_post"),
    path('delete_task/<int:pk>/',views.delete_post,name="delete_post"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]