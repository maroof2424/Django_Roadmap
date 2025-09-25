from django.shortcuts import HttpResponse,render

# def home(request):
#     return HttpResponse("Hello, Django! this is my first view")


def home(request):
    return render(request,"blog/index.html")