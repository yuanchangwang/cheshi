from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("login_fbv/", views.login),
    path("login_cbv/", views.Login.as_view()),
    # 分页器的使用
    path("book_list/", views.BookList.as_view()),
]