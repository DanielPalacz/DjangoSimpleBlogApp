from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def home(request):
    posts = Post.newmanager.all()
    return render(request, "blog/index.html", {"posts": posts})


def post_single(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status="published")
    return render(request, "blog/single.html", {"post": post})
