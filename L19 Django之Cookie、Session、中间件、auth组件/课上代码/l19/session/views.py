from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    if not request.session.get('is_login'):
        """
        1. 从cookie中取出sessionid
        2. 拿到随机字符串到django_session 表中过滤对象
        3. 拿到对象取出data值。
        """
        return redirect("/session/login/")
    return render(request, "session_index.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # if request.session.get("keep_str").upper() == request.POST.get("keep_str"): # 验证码的校验
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username in ["alex", "egon"] and password == "123":
            request.session['is_login'] = True
            """
            1. 生产随机字符串
            2. 将数据存到django_session表中
            3. 设置cookie值。（sessionid，值为随机字符串）
            """

            # rep.set_cookie("is_login", True)  # 设置cookie
            return redirect("/session/index/")
        else:
            return redirect("/session/login/")


def logout(request):
    request.session.flush()
    """
    1. 从cookie中取出sessionid
    2. 拿到随机字符串到django_session 表中过滤对象
    3. 删除该对象。
    """
    return redirect("/session/login/")