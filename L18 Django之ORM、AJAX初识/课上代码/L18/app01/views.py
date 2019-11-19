from django.shortcuts import render, HttpResponse
from app01 import models
# Create your views here.


def add_book(request):
    if request.method == "GET":
        return render(request, "add_book.html")
    else:

        # 获取数据
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")

        # 新增数据
        # 方式一：
        # book_obj = models.Book(title=title, price=price, pub_date=pub_date)
        # book_obj.save()  # 一定要save

        # 方式二： (推荐使用）
        # book_obj = models.Book.objects.create(title=title, price=price, pub_date=pub_date)

        # print(book_obj)

        # 及时注释掉
        # models.Book.objects.create(title="独孤九剑", price=180, pub_date="2019-1-12")
        # models.Book.objects.create(title="华山剑法", price=100, pub_date="2018-10-2")
        # models.Book.objects.create(title="挤奶龙爪手", price=200, pub_date="2019-2-22")
        # models.Book.objects.create(title="冲灵剑法", price=150, pub_date="2019-3-6")
        # models.Book.objects.create(title="吸星大法", price=190, pub_date="2019-2-6")
        # models.Book.objects.create(title="葵花宝典", price=280, pub_date="2018-1-17")
        # models.Book.objects.create(title="乾坤大挪移", price=260, pub_date="2019-1-6")
        # models.Book.objects.create(title="九阴真经", price=220, pub_date="2019-3-6")
        # models.Book.objects.create(title="九阳神功", price=230, pub_date="2019-3-11")
        # models.Book.objects.create(title="九阴白骨爪", price=50, pub_date="2019-2-7")

        return HttpResponse("新增成功！")


def query_book(request):

    # all  QuerySet类型 类似于列表 获取所有对象
    books = models.Book.objects.all()

    # filter  QuerySet类型 类似于列表 获取满足条件对象， filter可以多个条件，之间的关系为and
    books = models.Book.objects.filter(pk=3)

    # get  获取对象， 没有结果或者有多个结果时，会报错。
    # books = models.Book.objects.get(pk=13)

    # exclude  QuerySet类型  跟filter相反，排除满足条件的所有对象
    books = models.Book.objects.exclude(pk=3)

    # order_by 默认是升序， 降序（-）
    books = models.Book.objects.order_by("-price")

    # reverse  反转
    books = models.Book.objects.order_by("-price").reverse()

    # first  获取第一条记录
    books = models.Book.objects.filter(pk=4).first()

    # exists  # 判断结果的bool
    books = models.Book.objects.filter(pk=4).exists()

    # values  QuerySet类型  里面类似于字典
    books = models.Book.objects.values("title", 'price')

    # values_list  QuerySet类型， 里面类似于元祖
    books = models.Book.objects.values_list("title", 'price')

    # distinct
    books = models.Book.objects.values("price").distinct()  # 去除重复价格


    # 基于双下划线的模糊查询

    books = models.Book.objects.filter(price__in=[100, 200, 230])

    books = models.Book.objects.filter(price__range=[100, 200])

    print(books, type(books))


    return HttpResponse("查询成功！")


def del_book(request):
    pk = request.GET.get('pk')

    print(pk)

    # 方式一： (对象的形式删除）
    # book_obj = models.Book.objects.filter(pk=pk).first()
    # book_obj.delete()

    # 方式二： （queryset类型）
    books = models.Book.objects.filter(pk=pk).delete()  # 返回值为受影响的行数

    print(books)
    return HttpResponse("删除成功")


def edit_book(request):
    pk = request.GET.get("pk")
    if request.method == "GET":
        book_obj = models.Book.objects.filter(pk=pk).first()
        return render(request, "edit_book.html", {"book_obj": book_obj})

    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")

        # 方式一： （对象的形式)
        book_obj = models.Book.objects.filter(pk=pk).first()
        book_obj.price = price
        book_obj.save()

        # 方式二：(queryset)
        books = models.Book.objects.filter(pk=pk).update(price=price)
        print(books)
        return HttpResponse("编辑成功！")
