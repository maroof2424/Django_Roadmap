from django.shortcuts import render,redirect
from .models import Feedback
from .forms import FeedbackForm

# Create your views here.

def feedback_list(request):
    feedbacks = Feedback.objects.all().order_by("-created_at")
    return render(request,"feedback/feedback_list.html",{"feedbacks":feedbacks})

def feedback_form(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("feedback_list")
    else:
        form = FeedbackForm()
    return render(request,"feedback/feedback_form.html",{"form":form})