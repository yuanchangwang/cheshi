from rest_framework import serializers
from students.models import Student


# 创建序列化器类，回头会在视图中被调用
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ("id", "name")  # 也可指定字段