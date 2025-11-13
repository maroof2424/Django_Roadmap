from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
# Create your views here.

# base_dir = "blog/"
# class list_post(View):
#     template_name = base_dir+"list_post.html"
#     def get(self, request):
#         posts = Post.objects.all().order_by("-created_at","-updated_at")
#         return render(request,self.template_name,{"posts":posts})

class ListPostView(ListView):
    model = Post
    template_name = "blog/list_post.html"
    context_object_name = "posts"
    ordering = ["-created_at","-updated_at"]

class PostDetailsView(DetailView):
    model = Post
    template_name = "blog/post_details.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("list_post")

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm 
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("list_post")

class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("list_post")
