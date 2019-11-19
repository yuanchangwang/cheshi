from django.shortcuts import render, HttpResponse, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


# def login_required(func):
#     def inner(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             path = request.path
#             print(path)
#             return redirect("/auth_demo/login/?next=%s" % path)
#         return func(request, *args, **kwargs)
#     return inner

@login_required
def index(request):

    return render(request, "auth_index.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            # path = request.GET.get("next", "/auth_demo/index/")
            path = request.GET.get("next") or "/auth_demo/index/"
            # if not path:
            #     path = "/auth_demo/index/"
            return redirect(path)
        else:
            return redirect("/auth_demo/login/")


def logout(request):
    auth.logout(request)
    return redirect("/auth_demo/login/")

@login_required
def order(request):
    return HttpResponse("order 页面。。。")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            User.objects.create_user(username=username, password=password1)
            return redirect("/auth_demo/login/")
        else:
            return redirect("/auth_demo/register/")
