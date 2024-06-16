from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_details, name='contact_details'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:post_slug>/', views.post_single, name='post_single'),
]
