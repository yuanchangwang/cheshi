"""orm_demo URL Configuration

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
from django.urls import path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("add_book/", views.add_book),
    path("query_book/", views.query_book),
    # ajax 相关
    path("ajax_temp/", views.ajax_temp),
    path("ajax_sleep/", views.ajax_sleep),
    path("ajax_test/", views.ajax_test),
    path("ajax_sum/", views.ajax_sum),
    path("ajax_json/", views.ajax_json),
    path("upload/", views.upload),
]
