from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {}),
    path('base', views.base, {}),
    path('register', views.register, {}),
    path('login', views.login, {}),
    path('signup', views.signup, {}),
    path('dashboard', views.dashboard, {}),
    ]

