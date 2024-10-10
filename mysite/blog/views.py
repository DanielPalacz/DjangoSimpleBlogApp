from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Post
# from django.contrib.auth.decorators import login_required
from .forms import ContactForm


def home(request):
    return render(request, "blog/home.html", {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                subject=f"Message from {name} [{email}]",  # Subject of the email
                message=message,  # Message content
                from_email='daniel.palacz@pyx.solutions',  # From email
                recipient_list=['daniel.palacz@pyx.solutions'],  # Recipient email list
                fail_silently=False,  # Raise exception if the email fails to send
            )
            return HttpResponseRedirect("/contact/")

    else:
        form = ContactForm()
        return render(request, "blog/contact.html", {"form": form})

def projects(request):
    return render(request, "blog/projects.html", {})


def blog(request):
    posts = Post.newmanager.all()
    return render(request, "blog/blog.html", {"posts": posts})


def post_single(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status="published")
    return render(request, "blog/single.html", {"post": post})
