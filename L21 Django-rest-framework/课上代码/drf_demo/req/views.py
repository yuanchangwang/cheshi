from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from students.models import Student
from req.serializers import StudentModelSerializer


# Create your views here.


class Student1View(View):
    def get(self, request):
        print(request.GET)
        print(type(request))

        return HttpResponse("view1")


class Student2APIView(APIView):
    def get(self, request):
        print(request.query_params)
        print(type(request))

        # return HttpResponse("view2")
        return Response("view2", status=status.HTTP_204_NO_CONTENT, headers={'name': "alex"})


"""
使用APIView提供学生信息的5个API接口
GET    /req/student3/               # 获取全部数据
POST   /req/student3/               # 添加数据

GET    /req/student3/(?P<pk>\d+)    # 获取一条数据
PUT    /req/student3/(?P<pk>\d+)    # 更新一条数据
DELETE /req/student3/(?P<pk>\d+)    # 删除一条数据
"""

class Student3APIView(APIView):
    def get(self, request):
        """获取所有数据"""
        student_list = Student.objects.all()
        # 序列化操作
        serializer = StudentModelSerializer(instance=student_list, many=True)

        return Response(serializer.data)

    def post(self, request):
        # 继承Ｖｉｅｗ的时候获取用户提交的数据
        # data = request.body.decotde()
        # data_dict = json.loads(data)

        # 获取用户提交的数据
        data_dict = request.data
        # 实例化序列化器对象
        serializer = StudentModelSerializer(data=data_dict)
        # 数据校验
        serializer.is_valid(raise_exception=True)
        # 保存数据
        serializer.save()

        return Response(serializer.validated_data)


class Student4APIView(APIView):
    def get(self, request, pk):
        # 过滤pk对应的学生对象
        student_obj = Student.objects.get(pk=pk)

        serializer = StudentModelSerializer(instance=student_obj)

        return Response(serializer.data)

    def put(self, request, pk):
        # 过滤pk对应的学生对象
        student_obj = Student.objects.get(pk=pk)
        # 获取用户提交的数据
        data_dict = request.data

        serializer = StudentModelSerializer(instance=student_obj, data=data_dict)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.validated_data)

    def delete(self, request, pk):
        Student.objects.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
使用GenericAPIView提供学生信息的5个API接口
GET    /req/student4/               # 获取全部数据
POST   /req/student4/               # 添加数据

GET    /req/student4/(?P<pk>\d+)    # 获取一条数据
PUT    /req/student4/(?P<pk>\d+)    # 更新一条数据
DELETE /req/student4/(?P<pk>\d+)    # 删除一条数据
"""

from rest_framework.generics import GenericAPIView

class Student5GenericAPIView(GenericAPIView):
    # 当前视图类中操作的公共数据，先从数据库查询出来
    queryset = Student.objects.all()
    # 设置类视图中所有方法共有调用的序列化器类
    serializer_class = StudentModelSerializer

    def get(self, request):
        # 获取模型数据
        student_list = self.get_queryset()

        # 调用序列化器
        serializer = self.get_serializer(instance=student_list, many=True)

        return Response(serializer.data)

    def post(self, request):
        """新增数据"""
        # 获取用户提交的数据并实例化序列化器对象
        serializer = self.get_serializer(data=request.data)
        # 数据校验
        serializer.is_valid(raise_exception=True)
        # 保存数据
        serializer.save()
        return Response(serializer.data)


class Student6GenericAPIView(GenericAPIView):
    # 当前视图类中操作的公共数据，先从数据库查询出来
    queryset = Student.objects.all()
    # 设置类视图中所有方法共有调用的序列化器类
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        """参数pk名，必须要叫pk，否则会报错。"""
        # 获取模型对象
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)

        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object()

        serializer = self.get_serializer(instance=instance, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        # 获取模型对象
        instance = self.get_object()
        # 删除模型对象
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


"""
使用GenericAPIView结合视图Mixin扩展类，快速实现数据接口的APIView
ListModelMixin      实现查询所有数据功能
CreateModelMixin    实现添加数据的功能
RetrieveModelMixin  实现查询一条数据功能
UpdateModelMixin    更新一条数据的功能
DestroyModelMixin   删除一条数据的功能
"""

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class Student7GenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request):
        # 获取所有数据
        return self.list(request)

    def post(self, request):
        # 新增操作
        return self.create(request)


class Student8GenericAPIView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)



"""
DRF里面，内置了一些同时继承了GenericAPIView和Mixins扩展类的视图子类，
我们可以直接继承这些子类就可以生成对应的API接口
"""

"""
ListAPIView      获取所有数据
CreateAPIView    添加数据
"""
from rest_framework.generics import ListAPIView, CreateAPIView


class Student9GenericAPIView(ListAPIView, CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


"""
RetrieveAPIView                 获取一条数据
UpdateAPIView                   更新一条数据
DestorAPIView                   删除一条数据
RetrieveUpdateDestoryAPIView    上面三个的缩写
"""
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class Student10GenericAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

