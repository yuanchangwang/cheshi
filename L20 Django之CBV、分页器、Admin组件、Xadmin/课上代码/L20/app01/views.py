from django.shortcuts import render, HttpResponse, redirect
from django.views import View
import time
from django.utils.decorators import method_decorator
from app01.models import Book
from app01.utils import Paginator as MyPaginator
import random
# Create your views here.


def timer(func):
    def inner(request, *args, **kwargs):
        start_time = time.time()
        time.sleep(1)
        rep = func(request, *args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return rep
    return inner


# FBV
@timer
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "alex" and password == "123":
            return HttpResponse('登录成功')
        else:
            return render(request, "login.html")

# CBV
# cbv下的方法名称必须是Http请求方式的小写名称
# @method_decorator(timer, name="post")
# @method_decorator(timer, name="get")  # 方式三： 直接给类加上装饰器，后面必须要指定name参数，否则会报错。
@method_decorator(timer, name="dispatch")
class Login(View):
    # @method_decorator(timer)  # 方式二 给dispatch方法加上装饰器之后，该类下的所有方法都加上装饰器。
    def dispatch(self, request, *args, **kwargs):
        obj = super().dispatch(request, *args, **kwargs)
        return obj

    # @method_decorator(timer)  # 方式一 直接给方法加上对应的装饰器。
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "alex" and password == "123":
            return HttpResponse('登录成功')
        else:
            return render(request, "login.html")


# ------------------- 分页器 -----------------------
from django.core.paginator import Paginator


class BookList(View):
    def get(self, request):
        # 新增完数据，及时注释掉。
        # temp_list = []
        # for i in range(1, 101):
        #     # Book.objects.create(title="book_%s" % i, price=random.randint(30, 200))
        #     temp_list.append(Book(title="book_%s" % i, price=random.randint(30, 200)))
        # Book.objects.bulk_create(temp_list)

        book_list = Book.objects.all()
        # paginator = Paginator(book_list, 12)

        # print("count", paginator.count)  # 数据的总数
        # print("num_pages", paginator.num_pages)  # 分页的总页数
        # print("page_range", paginator.page_range)  # 页数的范围列表

        # page1 = paginator.get_page(1)

        # for i in page1:
        #     print(i)

        # print(page1.object_list)

        # page2 = paginator.get_page("12")

        # print(page2.has_next())  # True 是否有下一页
        # print(page2.next_page_number())  #3 下一页的页码
        # print(page2.has_previous())  #True 是否有上一页
        # print(page2.previous_page_number())  #1 上一页的页码


        # 基本使用

        current_page = int(request.GET.get('page', 1))

        # page = paginator.get_page(current_page)

        # if paginator.num_pages > 11: # 假设页面显示11个页码
        #     if current_page - 5 < 1:  # 最前面的情况
        #         page_range = range(1, 12)
        #     elif current_page + 5 > paginator.num_pages:  #　最后面的情况
        #         page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        #     else:  # 中间情况
        #         page_range = range(current_page - 5, current_page + 6)
        # else:
        #     page_range = paginator.page_range

        paginator = MyPaginator(request, current_page, book_list.count(), 8, 11)

        book_list = book_list[paginator.start: paginator.end]


        # return render(request, "book_list.html", {
        return render(request, "book_list1.html", {
            # "book_list": book_list,
            # "page": page,
            # "page_range": page_range,
            'paginator': paginator,
            "current_page": current_page,
            "book_list": book_list
        })


