from django.shortcuts import render, HttpResponse
from app01 import models
# Create your views here.


def add_book(request):

    # 一对多的新增------------------------
    # 方式一: 传对象
    # pub_obj = models.Publish.objects.filter(name="华山出版社").first()
    # books = models.Book.objects.create(title="独孤九剑", price=130, pub_date="2007-10-13", publish=pub_obj)
    # 方式二： 传pk值（数字）
    # books = models.Book.objects.create(title="吸星大法", price=110, pub_date="2017-10-13", publish_id=pub_obj.pk)


    # 多对多新增

    # 方式一 传对象的形式
    # book = models.Book.objects.filter(title="独孤九剑").first()
    # ling = models.Author.objects.filter(name="令狐冲").first()
    # ying = models.Author.objects.filter(name="任盈盈").first()
    # book.authors.add(ling, ying)

    # 方式二 传对象id的形式
    # book = models.Book.objects.filter(title="吸星大法").first()
    # ling = models.Author.objects.filter(name='令狐冲').first()
    # ying = models.Author.objects.filter(name='任我行').first()
    # book.authors.add(ling.pk, ying.pk)

    # 通过作者删除与书籍的关系
    # author_obj = models.Author.objects.filter(pk=1).first()
    # author_obj.book_set.clear()

    # 通过出版社删除书籍
    # pub_obj = models.Publish.objects.get(pk=1)
    # book_obj = models.Book.objects.get(pk=1)
    # pub_obj.book_set.remove(book_obj)
    # 1. 外建字段，必须指定null=True，才有remove
    # 2. 如果没有执行数据库迁移命令，数据不允许为空。会报错，所以，要执行迁移命令，才可正常删除。

    # print(books)


    return HttpResponse("新增成功！")


def query_book(request):

    # 基于对象查询
    """
                正向：按字段
    book  ----------------------->  publish
            反向：按小写表名+_set
    """
    # 一对多关系
    # 正向
    # 查询主键为1的书籍的出版社所在的城市
    # book_obj = models.Book.objects.filter(pk=1).first()
    # print(book_obj.publish.city)

    # 反向
    # 查询明教出版社出版的书籍名
    # pub_obj = models.Publish.objects.filter(name="华山出版社").first()
    # for book in pub_obj.book_set.all():
    #     print(book.title)

    #  一对一关系
    # 正向  按字段即可
    # 查询令狐冲的电话
    author_obj = models.Author.objects.filter(name="令狐冲").first()
    print(author_obj.au_detail.tel)

    # 反向 一对一时，反向不用  +  _set
    # 查询所有住址在黑木崖的作者的姓名
    # au_detail_list = models.AuthorDetail.objects.filter(addr="黑木崖")
    # for au in au_detail_list:
    #     print(au.author.name)


    # 多对多关系
    # 正向：
    # 独孤九剑所有作者的名字以及手机号
    # book_obj = models.Book.objects.filter(title="独孤九剑").first()
    # for au in book_obj.authors.all():
    #     print(au.name, au.au_detail.tel)

    # 反向
    # 查询令狐冲出过的所有书籍的名字
    # au_obj = models.Author.objects.filter(name="令狐冲").first()
    # for book in au_obj.book_set.all():
    #     print(book.title)


    # 基于双下划线查询--------------------------------
    # 正向查询按字段,反向查询按表名小写   用来告诉ORM引擎join哪张表
    # 一对多
    # 练习: 查询明教出版社出版过的所有书籍的名字与价格(一对多)
    # 反向：
    # books = models.Publish.objects.filter(name="华山出版社").values("book__title", "book__price")

    # 正向：
    # books = models.Book.objects.filter(publish__name="华山出版社").values("title", "price")

    # 多对多
    # 练习: 查询令狐冲出过的所有书籍的名字(多对多)
    # books = models.Book.objects.filter(authors__name="令狐冲").values("title")
    # books = models.Author.objects.filter(name="令狐冲").values("book__title")


    # 聚合查询 aggregate()是QuerySet 的一个终止子句, 字典
    from django.db.models import Avg, Max, Min, Count, Sum, F, Q
    # 计算所有图书的平均价格
    # books = models.Book.objects.aggregate(Avg("price"))

    # 练习：统计每一个出版社的最便宜的书的价格
    books = models.Publish.objects.values('name').annotate(min_price=Min("book__price"))

    # F 对象 动态获取数据库的值
    # models.Book.objects.update(price=F("price") + 100)

    # Q 对象， filter多个条件时，and关系， 需要用or的话，就要使用Q对象

    # 查询价格大于220或者名称以独开头的书籍
    books = models.Book.objects.filter(Q(price__gt=220)|Q(title__startswith="独") )

    # 查询价格大于220或者不是2007年十月份的书籍
    books = models.Book.objects.filter(Q(price__gt=220)|~Q(Q(pub_date__year=2007)&Q(pub_date__month=10)))

    print(books)


    return HttpResponse("查询成功！")


def ajax_sleep(request):
    import time
    time.sleep(3)
    return HttpResponse("睡了3s")


def ajax_test(request):
    return HttpResponse("test...")


def ajax_temp(request):
    return render(request, "ajax_temp.html")
from django.http import JsonResponse

def ajax_sum(request):
    if request.is_ajax():
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        ret = {"status": 1, "msg": None}
        try:
            total = int(num1) + int(num2)
            ret['msg'] = total
        except Exception as e:
            ret['status'] = 0
            ret['msg'] = "请输入数字"
        # return HttpResponse(total)
        return JsonResponse(ret)
    ###  视图响应时，只能时HttpResponse或者JsonResponse，render和redirect不能作为ajax请求的返回对象。


def ajax_json(request):
    import json

    print(1, request.POST)
    print(2, request.body)
    print(3, request.FILES)
    data = json.loads(request.body.decode())
    print(data, type(data))
    return HttpResponse("ok")
import os
def upload(request):
    print(request.POST)
    print(request.FILES)
    # print(request.body)  # 会报错

    file_obj = request.FILES.get('file_name')
    name = file_obj.name
    with open(os.path.join("media", name), "wb") as f:
        for i in file_obj:
            f.write(i)
    return HttpResponse('上传成功')