from django.urls import path, re_path
from app01 import views

urlpatterns = [
    path("add_book/", views.add_book),  # 新增操作
    path("query_book/", views.query_book),  #　查询操作
    path("del_book/", views.del_book),  # 删除操作
    path("edit_book/", views.edit_book),  # 编辑操作
]