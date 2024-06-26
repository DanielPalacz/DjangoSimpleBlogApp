from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog'),
    path('<slug:post_slug>/', views.post_single, name='post_single'),
]
