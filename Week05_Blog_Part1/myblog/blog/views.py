from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required(login_url="login")
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            messages.error(request, "⚠️ Title and content cannot be empty.")
            return redirect("create_post")

        Post.objects.create(user=request.user, title=title, content=content)
        messages.success(request, "✅ Post created successfully!")
        return redirect("list_posts")

    return render(request, "blog/post_form.html")


@login_required(login_url="login")
def list_posts(request):
    posts = Post.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "blog/list_posts.html", {"posts": posts})


@login_required(login_url="login")
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()

        if not title or not content:
            messages.error(request, "⚠️ Title and content cannot be empty.")
            return redirect("update_post", pk=pk)

        post.title = title
        post.content = content
        post.save()
        messages.success(request, "✏️ Post updated successfully!")
        return redirect("list_posts")

    return render(request, "blog/post_form.html", {"post": post})


@login_required(login_url="login")
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user=request.user)

    if request.method == "POST":
        post.delete()
        messages.info(request, "🗑️ Post deleted successfully!")
        return redirect("list_posts")

    return render(request, "blog/post_confirm_delete.html", {"post": post})


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm = request.POST.get("confirm", "")

        # Validation checks
        if not username or not email or not password:
            messages.error(request, "⚠️ All fields are required.")
            return redirect("signup")

        if password != confirm:
            messages.error(request, "⚠️ Passwords do not match.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "⚠️ Password must be at least 8 characters long.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ Username already exists.")
            return redirect("signup")

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "✅ Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "blog/auth.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "🎉 Logged in successfully!")
            next_url = request.GET.get("next", "list_posts")
            return redirect(next_url)
        else:
            messages.error(request, "❌ Invalid credentials.")
            return redirect("login")

    return render(request, "blog/auth.html")


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.info(request, "👋 Logged out successfully.")
    return redirect("login")
