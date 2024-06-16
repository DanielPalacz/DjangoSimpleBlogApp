from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "blog/home.html", {})


def contact_details(request):
    return render(request, "blog/contact_details.html", {})


def projects(request):
    return render(request, "blog/projects.html", {})


def blog(request):
    posts = Post.newmanager.all()
    return render(request, "blog/blog.html", {"posts": posts})


def post_single(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status="published")
    return render(request, "blog/single.html", {"post": post})
