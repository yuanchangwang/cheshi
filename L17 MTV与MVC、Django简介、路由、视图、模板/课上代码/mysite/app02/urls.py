from django.urls import path
from app02 import views

urlpatterns = [
    path("test02/", views.test02, name="test1"),
    path("book_list/", views.book_list),
    path("publish_list/", views.publish_list),
    
]