from django.urls import path, re_path
from . import views

urlpatterns = [
    path("test1/", views.test1, name="test1"),
    path("temp_test/", views.temp_test),
]