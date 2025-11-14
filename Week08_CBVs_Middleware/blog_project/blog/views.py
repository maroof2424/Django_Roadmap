from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

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

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm 
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("list_post")

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm 
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("list_post")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("list_post")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "blog/signup.html"
    success_url = reverse_lazy('login')
