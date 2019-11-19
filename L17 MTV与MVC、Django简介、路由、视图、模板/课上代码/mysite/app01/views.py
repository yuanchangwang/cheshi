from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

# Create your views here.


def login(request):
    print(request.method, reverse("Login"))
    if request.method == "GET":

    # return HttpResponse("ok")
        return render(request, "login.html")
    else:
        print(111, request.body)
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        print(user, pwd)
        if user == 'longyang' and pwd == '123':
            return HttpResponse("登录成功！")
        else:
            # return render(request, "login.html")
            return redirect(reverse("Login"))



def articles_2019(request):
    print("articles_2019")
    return HttpResponse("articles_2019")


def articles_year(request, year):  # 无名分组，按照位置传参
    print("articles_%s" % year)
    return HttpResponse("articles_%s" % year)



def articles_y_m(request, m, y):
    
    return HttpResponse("%s---%s" % (y, m))


#  -------------------- 路由分发 -----------------------


def test1(request):
    # print(reverse("app01:test1"))  # 反向解析

    # request对象的常用属性
    # GET方式：
    # print(request.GET)
    # print(request.GET.get("name"))

    # < QueryDict: {'name': ['alex'], 'hobby': ['chui', 'la', 'tan']} >
    # request.GET.getlist("hobby")  # 获取多个值时，使用getlist方法。

    # request.POST 同上

    # request.body 原生的请求体里的内容
    b"name=alex&age=18"

    print(request.path)  # 获取当前请求的URL路径

    # print(request.method)  # 获取当前请求的方式

    # request对象常用的方法
    print(request.get_full_path())  # 获取当前请求的完整路径

    # 判断当前请求是否是ajax请求
    print(request.is_ajax())
    


    return HttpResponse("test1 函数")


# 模板相关
import datetime

def temp_test(request):
    
    # name = "alex"
    name = "111"
    num = 2223000000
    list1 = ["alex", "egon", "yuan"]
    dict1 = {"name": "alex", "age": 18}
    now_time = datetime.datetime.now()
    str1 = "When you say goodnight to me, can I understand that you say I love you?"
    
    str_a = '<a href="http://www.baidu.com">百度一下</a>'
    num1 = 10
    
    class A:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def eat(self):
            return "666"
        
    a1 = A("alex", 18)
    a2 = A("egon", 22)
    a3 = A("yuan", 24)
    
    a_list = [a1, a2, a3]
    
    
    return render(request, "temp_test.html", {"username": name,
                                              "list1": list1,
                                              "dict1": dict1,
                                              "a1": a1,
                                              "num": num,
                                              "now_time": now_time,
                                              "str1": str1,
                                              "str_a": str_a, 
                                              "a_list": a_list,
                                              "num1": num1,
                                              })

