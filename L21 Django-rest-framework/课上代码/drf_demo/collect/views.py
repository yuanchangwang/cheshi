from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from students.models import Student
from collect.serializers import StudentModelSerializer
from rest_framework.response import Response

# Create your views here.


class Student1ViewSet(ViewSet):
    def get_5(self, request):
        queryset = Student.objects.all()[:5]

        serializer = StudentModelSerializer(instance=queryset, many=True)

        return Response(serializer.data)

    def get_5_girl(self, request):
        queryset = Student.objects.filter(sex=False)[:5]

        serializer = StudentModelSerializer(instance=queryset, many=True)

        return Response(serializer.data)

    def get_one(self, request, pk):
        student_obj = Student.objects.get(pk=pk)

        serializer = StudentModelSerializer(instance=student_obj)

        return Response(serializer.data)


from rest_framework.viewsets import GenericViewSet


class Student3GenericViewSet(GenericViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def get_5(self, request):
        student_list = self.get_queryset()[:5]

        serializer = self.get_serializer(instance=student_list, many=True)

        return Response(serializer.data)

    def get_5_girl(self, request):
        student_list = self.get_queryset().filter(sex=False)[:5]

        serializer = self.get_serializer(instance=student_list, many=True)

        return Response(serializer.data)


from rest_framework.mixins import ListModelMixin, CreateModelMixin


class Student4GenericViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


from rest_framework.viewsets import ModelViewSet


class Student5ModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


from rest_framework.viewsets import ReadOnlyModelViewSet


class Student6ReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


from rest_framework.decorators import action


class Student7ModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    # methods 指定允许哪些http请求访问当前视图方法
    # detail  指定生成的路由地址中是否要夹带pk值，True为需要
    # @action(methods=['get'], detail=False)
    # def get_4(self, request):
    @action(methods=['get'], detail=True)
    def get_4(self, request, pk):
        serilizer = self.get_serializer(instance=self.get_queryset().get(pk=pk))
        return Response(serilizer.data)


from rest_framework.generics import GenericAPIView
from collect.serializers import StudentInfoModelSerializer


class Student8GenericAPIView(GenericAPIView):
    queryset = Student.objects.all()

    # GenericAPI内部调用序列化器的方法，我们可以重写这个方法来实现根据不同的需求来调用不同的序列化器
    def get_serializer_class(self):
        if self.request.method == "GET":
            # 2个字段
            return StudentInfoModelSerializer
        return StudentModelSerializer

    def get(self, request):
        """获取所有数据的id和name"""
        student_list = self.get_queryset()

        serializer = self.get_serializer(instance=student_list, many=True)
        # serializer = StudentInfoModelSerializer(instance=student_list, many=True)

        return Response(serializer.data)

    def post(self, request):
        """添加数据"""
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


"""2. 在一个视图集中调用多个序列化器"""

class Student9ModelViewSet(ModelViewSet):
    queryset = Student.objects.all()

    """要求:
            列表数据list，返回２个字段，
            详情数据retrieve，返回所有字段，
    """
    def get_serializer_class(self):
        # 本次客户端请求的视图方法名  self.action
        print(self.action)
        if self.action == "list":
            return StudentInfoModelSerializer
        return StudentModelSerializer
