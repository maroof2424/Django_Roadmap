from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Post, Comment


@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            messages.error(request, "Title aur Content empty nahi ho sakte.")
            return redirect("create_post")

        Post.objects.create(user=request.user, title=title, content=content)
        messages.success(request, "Post created successfully!")
        return redirect("list_posts")

    return render(request, "blog/post_form.html")


@login_required(login_url="login")
def list_posts(request):
    query = request.GET.get("q", "")
    filter_option = request.GET.get("filter", "latest")

    posts = Post.objects.filter(user=request.user)

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    ordering = "-created_at" if filter_option == "latest" else "created_at"
    posts = posts.order_by(ordering)

    page_obj = Paginator(posts, 5).get_page(request.GET.get("page"))

    return render(request, "blog/list_posts.html", {
        "page_obj": page_obj,
        "query": query,
        "filter_option": filter_option,
    })


@login_required(login_url="login")
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            messages.error(request, "Title aur Content empty nahi ho sakte.")
            return redirect("update_post", pk=pk)

        post.title = title
        post.content = content
        post.save()

        messages.success(request, "Post updated!")
        return redirect("list_posts")

    return render(request, "blog/post_form.html", {"post": post})


@login_required(login_url="login")
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)

    if request.method == "POST":
        post.delete()
        messages.info(request, "Post deleted!")
        return redirect("list_posts")

    return render(request, "blog/post_confirm_delete.html", {"post": post})


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm = request.POST.get("confirm", "")

        if not username or not email or not password:
            messages.error(request, "All fields required.")
            return redirect("signup")

        if password != confirm:
            messages.error(request, "Passwords match nahi kar rahe.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password 8 characters ka hona chahiye.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created! Login karein.")
        return redirect("login")

    return render(request, "blog/auth.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect(request.GET.get("next", "list_posts"))

        messages.error(request, "Invalid credentials.")
        return redirect("login")

    return render(request, "blog/auth.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect("login")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by("-created_at")

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Login karke comment karen.")
            return redirect("login")

        content = request.POST.get("content", "").strip()

        if not content:
            messages.error(request, "Comment empty nahi ho sakta.")
            return redirect("post_detail", pk=pk)

        Comment.objects.create(post=post, user=request.user, content=content)
        messages.success(request, "Comment added!")
        return redirect("post_detail", pk=pk)

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
    })
