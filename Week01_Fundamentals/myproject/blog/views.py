from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! this is my first view")
