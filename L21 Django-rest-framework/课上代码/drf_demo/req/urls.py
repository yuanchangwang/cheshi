from django.urls import path, re_path
from req import views

urlpatterns = [
    # View与APIView的区别
    path('student1/', views.Student1View.as_view()),
    path('student2/', views.Student2APIView.as_view()),

    # 使用APIView
    path("student3/", views.Student3APIView.as_view()),
    re_path(r"^student3/(?P<pk>\d+)/$", views.Student4APIView.as_view()),

    # 使用GenericAPIView
    path("student4/", views.Student5GenericAPIView.as_view()),
    re_path(r"^student4/(?P<pk>\d+)/$", views.Student6GenericAPIView.as_view()),

    # 使用GenericAPIView，结合Mixin的扩展类
    path("student5/", views.Student7GenericAPIView.as_view()),
    re_path(r"^student5/(?P<pk>\d+)/$", views.Student8GenericAPIView.as_view()),

    # 使用内置的扩展子类，生成API接口
    path("student6/", views.Student9GenericAPIView.as_view()),
    re_path(r"^student6/(?P<pk>\d+)/$", views.Student10GenericAPIView.as_view()),
]