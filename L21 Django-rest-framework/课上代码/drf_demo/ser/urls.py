from django.urls import path, re_path
from ser import views

urlpatterns = [
    path('student1/', views.Student1.as_view()),
    re_path(r'^student1/(?P<pk>\d+)/$', views.Student2.as_view()),

    # 数据校验
    path('student2/', views.Student3.as_view()),  # 通过post方式新增一条数据
    re_path(r'^student2/(?P<pk>\d+)/$', views.Student4.as_view()), # 修改操作

    # 序列化器的整合使用
    path('student3/', views.Student5.as_view()),
    re_path(r'^student3/(?P<pk>\d+)/$', views.Student6.as_view()),

    # 模型类序列化器的使用
    path('student4/', views.Student7.as_view()),
    re_path(r'^student4/(?P<pk>\d+)/$', views.Student8.as_view()),
]