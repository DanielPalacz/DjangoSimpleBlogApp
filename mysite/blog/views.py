from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    posts = Post.newmanager.all()
    return render(request, "blog/index.html", {"posts": posts})


@login_required
def post_single(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status="published")
    return render(request, "blog/single.html", {"post": post})
