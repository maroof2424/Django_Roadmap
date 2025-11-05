from django.urls import path
from . import views

urlpatterns = [
    path("",views.list_tasks,name="list_tasks"),
    path("create/",views.create_task,name="create_task"),
    path("update/",views.update_task,name="update_task"),
    path("delete/",views.delete_task,name="delete_task")
]
