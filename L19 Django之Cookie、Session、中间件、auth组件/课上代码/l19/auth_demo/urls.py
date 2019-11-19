from django.urls import path, re_path
from auth_demo import views

urlpatterns = [
    path("index/", views.index),
    path("login/", views.login),
    path("logout/", views.logout),
    path('order/', views.order),
    path("register/", views.register),
]