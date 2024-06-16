from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {})


def logged_out(request):
    return render(request, "registration/user_logged_out.html", {})


def info(request):
    return render(request, "registration/info.html", {})
