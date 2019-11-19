from students.models import Student
from rest_framework import serializers


# 直接或者间接继承Ｓｅｒｉａｌｉｚｅｒ类
class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ["id", "name", "age", "sex"]
        extra_kwargs = {
            "name": {"max_length": 10, "min_length": 4},
            "age": {"max_value": 150, "min_value": 0},
        }

    def validate_name(self, data):
        if data == "root":
            raise serializers.ValidationError("用户名不能为root！")
        return data

    def validate(self, attrs):
        name = attrs.get('name')
        age = attrs.get('age')

        if name == "alex" and age == 22:
            raise serializers.ValidationError("alex在22时的故事。。。")

        return attrs


class StudentInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name"]
