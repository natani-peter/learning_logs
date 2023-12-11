from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("users/login/", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("users/logout", LogoutView.as_view(next_page='/'), name='logout'),
    path('users/register', views.register, name='register')
]
