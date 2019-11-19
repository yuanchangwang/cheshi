from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def login_required(func):
    def inner(request, *args, **kwargs):
        if not request.COOKIES.get("is_login"):  # 获取cookie值 当用户没有登录时，跳转到登录页面
            return redirect("/cookie/login/")
        rep = func(request, *args, **kwargs)
        return rep
    return inner


@login_required
def index(request):
    # if not request.COOKIES.get("is_login"):  # 当用户没有登录时，跳转到登录页面
    #     return redirect("/cookie/login/")
    print("index 视图")
    # int("aaa")
    rep = render(request, "index.html")
    # print(id(rep))
    return rep


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "alex" and password == "123":
            rep = redirect("/cookie/index/")
            rep.set_cookie("is_login", True)  # 设置cookie
            return rep
        else:
            return redirect("/cookie/login/")


def logout(request):
    rep = redirect("/cookie/login/")
    rep.delete_cookie("is_login")
    return rep


@login_required
def order(request):
    # if not request.COOKIES.get("is_login"):  # 当用户没有登录时，跳转到登录页面
    #     return redirect("/cookie/login/")
    return HttpResponse("order页面。。。")
