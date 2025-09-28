from django.shortcuts import HttpResponse,render

# def home(request):
#     return HttpResponse("Hello, Django! this is my first view")


def home(request):
    return render(request,"note/index.html")
def about(request):
    return render(request,"note/about.html")
def contact(request):
    return render(request,"note/contact.html")