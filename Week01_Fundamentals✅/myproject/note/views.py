from django.shortcuts import HttpResponse,render
from .models import Note
# def home(request):
#     return HttpResponse("Hello, Django! this is my first view")


def home(request):
    return render(request,"note/index.html")
def about(request):
    return render(request,"note/about.html")
# def contact(request):
#     return render(request,"note/contact.html")
def notes_list(request):
    notes = Note.objects.all()
    return render(request, "note/notes_list.html", {"notes": notes})