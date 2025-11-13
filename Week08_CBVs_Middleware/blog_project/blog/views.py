from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.

# base_dir = "blog/"
# class list_post(View):
#     template_name = base_dir+"list_post.html"
#     def get(self, request):
#         posts = Post.objects.all().order_by("-created_at","-updated_at")
#         return render(request,self.template_name,{"posts":posts})

class list_post(ListView):
    model = Post
    template_name = "blog/list_post.html"
    context_object_name = "posts"
    ordering = ["-created_at","-updated_at"]

class post_details(DetailView):
    model = Post
    template_name = "blog/post_details.html"
    context_object_name = "post"
