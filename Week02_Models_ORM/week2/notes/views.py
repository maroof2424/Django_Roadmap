from django.shortcuts import render,redirect
from .models import Note
# Create your views here.

def notes_list(request):
    notes = Note.objects.all().order_by("-created_at")
    return render(request,"notes/notes_list.html", {"notes": notes})

def create_notes(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        content = data.get("content")
        Note.objects.create(title=title,content=content)
        return redirect("notes_list")
    return render(request,"notes/create_notes.html")

def delete_note(request,note_id):
    note = Note.objects.get(id = note_id)
    note.delete()
    return redirect("notes_list")