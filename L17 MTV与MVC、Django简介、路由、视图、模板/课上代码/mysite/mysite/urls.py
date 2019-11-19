"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login111/', views.login, name="Login"),
    # re_path('^login/$', views.login),
    # path("articles/2019/", views.articles_2019),
    # 无名分组,按位置传参
    # re_path("^articles/([0-9]{4})/$", views.articles_year),
    # 有名分组， 按关键字传参
    # re_path("^articles/(?P<year>[0-9]{4})/$", views.articles_year),
    #无名分组，年月
    # re_path("^articles/([0-9]{4})/([0-9]{2})/$", views.articles_y_m),
    # 有名分组， 年月
    re_path("^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/$", views.articles_y_m),
    
    # path("app01/", include("app01.urls")),
    # path("app02/", include("app02.urls")),
    # 名称空间
    path("app01/", include(("app01.urls", "app01"))),
    path("app02/", include(("app02.urls", 'app02'))),
]
