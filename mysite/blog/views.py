from django.shortcuts import render, HttpResponse
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "blog/index.html", {"posts": posts})
