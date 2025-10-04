from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes_list, name="notes_list"),
    path("create_notes/", views.create_notes, name="create_notes"),
    path("delete_note/<int:note_id>", views.delete_note, name="delete_note"),
]
