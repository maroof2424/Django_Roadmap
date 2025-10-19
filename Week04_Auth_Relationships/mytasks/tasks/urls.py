from django.urls import path
from . import views
urlpatterns = [
    path('',views.task_list,name="task_list"),
    path('create_task/',views.create_task,name="create_task"),
    path('update_task/<int:pk>/',views.update_task,name="update_task"),
    path('delete_task/<int:pk>/',views.delete_task,name="delete_task"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]
