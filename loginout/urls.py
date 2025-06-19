from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='loginout/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
        