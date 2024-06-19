from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone


class CreatePostForm(forms.Form):
    users = tuple([(user.username, user.username.capitalize) for user in User.objects.all()])

    options = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    title = forms.CharField(label="Title", max_length=200)
    publish = forms.DateTimeField(label="Publish date", initial=timezone.now)
    # author = forms.ChoiceField(choices=users)
    author = forms.TypedChoiceField(choices=users)
    content = forms.CharField(label="Content", max_length=4000, widget=forms.Textarea)
    status = forms.TypedChoiceField(choices=options)
    file = forms.FileField()


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {})


def logged_out(request):
    return render(request, "registration/user_logged_out.html", {})


@login_required
def info(request):
    return render(request, "registration/info.html", {})


@login_required
def crud_create(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            tdl_title = form.cleaned_data["title"]
            #tdl = ToDoList(name=tdl_name)
            # tdl.save()
            return HttpResponseRedirect(f"/{tdl.id}")

    else:
        form = CreatePostForm()


    return render(request, "account/crud_create.html", {"form": form})
