from django.urls import path, re_path
from session import views

urlpatterns = [
    path("index/", views.index),
    path("login/", views.login),
    path("logout/", views.logout),
]