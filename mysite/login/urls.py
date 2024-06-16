from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(http_method_names=['post']), name='logout'),
    path('account/', views.dashboard, name='dashboard'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('api-info', views.info, name='api-info'),
]
