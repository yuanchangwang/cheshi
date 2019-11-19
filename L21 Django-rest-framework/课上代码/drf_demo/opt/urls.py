from django.urls import path
from opt import views

urlpatterns = [
    path('auth1/', views.Demo1APIView.as_view()),
    path('auth2/', views.Demo2APIView.as_view()),

    # 自定义权限
    path('auth3/', views.Demo3APIView.as_view()),

    # 限流
    path('auth4/', views.Demo4APIView.as_view()),

    # 过滤
    path('data5/', views.Demo5APIView.as_view()),

    # 排序
    path('data6/', views.Demo6APIView.as_view()),

    # 分页
    path('data7/', views.Demo7APIView.as_view()),
]