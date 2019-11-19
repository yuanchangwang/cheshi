from django.shortcuts import render, HttpResponse
from django.views import View
from students.models import Student
from ser.serializers import StudentSerializer
from django.http import JsonResponse

# Create your views here.

class Student1(View):
    def get(self, request):
        """
        获取所有数据， 序列化操作
        :param request:
        :return:
        """

        student_list = Student.objects.all()
        # many=True 表示本次序列化器转换如果有多个模型对象列参数，则必须声明 Many=True
        serializer = StudentSerializer(instance=student_list, many=True)

        print(111, serializer.data)

        return JsonResponse(serializer.data, safe=False)
        # return HttpResponse(serializer.data)


class Student2(View):
    def get(self, request, pk):
        student_obj = Student.objects.get(pk=pk)

        serializer = StudentSerializer(instance=student_obj)

        print(serializer.data)

        return JsonResponse(serializer.data)

import json
from ser.serializers import Student2Serializer

class Student3(View):
    def post(self, request):
        data = request.body.decode()
        data_dict = json.loads(data)

        serializer = Student2Serializer(data=data_dict)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        print("errors", serializer.errors)

        print(serializer.validated_data)

        return JsonResponse(serializer.data)


class Student4(View):
    def put(self, request, pk):
        data = request.body.decode()
        data_dict = json.loads(data)
        student_obj = Student.objects.get(pk=pk)

        serializer = Student2Serializer(instance=student_obj, data=data_dict)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(serializer.data)

from ser.serializers import Student3Serializer


class Student5(View):
    def get(self, request):
        # 获取所有数据
        student_list = Student.objects.all()

        serializer = Student3Serializer(instance=student_list, many=True)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        #　新增一条数据
        data = request.body.decode()
        data_dict = json.loads(data)

        serializer = Student3Serializer(data=data_dict)

        # 数据校验
        serializer.is_valid(raise_exception=True)

        # 数据保存
        serializer.save()

        return JsonResponse(serializer.data)


class Student6(View):
    def get(self, request, pk):
        # 获取一条
        student_obj = Student.objects.get(pk=pk)

        serializer = Student3Serializer(instance=student_obj)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        #　更新一条数据
        student_obj = Student.objects.get(pk=pk)

        data = request.body.decode()
        data_dict = json.loads(data)

        serializer = Student3Serializer(instance=student_obj, data=data_dict)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(serializer.data)

    def delete(self, request, pk):

        student_obj = Student.objects.get(pk=pk)
        student_obj.delete()

        return HttpResponse("ok")


from ser.serializers import Student4ModelSerializer

class Student7(View):
    def get(self, reuquest):
        # 获取所有数据
        student_list = Student.objects.all()

        serializer = Student4ModelSerializer(instance=student_list, many=True)

        return JsonResponse(serializer.data, safe=False)
    def post(self, request):
        #　新增一条数据
        data = request.body.decode()
        data_dict = json.loads(data)

        serializer = Student4ModelSerializer(data=data_dict)

        # 数据校验
        serializer.is_valid(raise_exception=True)

        # 数据保存
        serializer.save()

        return JsonResponse(serializer.data)


class Student8(View):
    def get(self, request, pk):
        # 获取一条
        student_obj = Student.objects.get(pk=pk)

        serializer = Student4ModelSerializer(instance=student_obj)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        #　更新一条数据
        student_obj = Student.objects.get(pk=pk)

        data = request.body.decode()
        data_dict = json.loads(data)

        serializer = Student4ModelSerializer(instance=student_obj, data=data_dict)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(serializer.data)

    def delete(self, request, pk):

        student_obj = Student.objects.get(pk=pk)
        student_obj.delete()

        return HttpResponse("ok")