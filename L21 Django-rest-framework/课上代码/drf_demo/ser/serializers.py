from rest_framework import serializers
from students.models import Student


# 所有的自定义序列化器必须直接或间接继承于 serializers.Serializer
class StudentSerializer(serializers.Serializer):
    # 声明序列化器
    # 1. 字段声明[ 要转换的字段，当然，如果写了第二部分代码，有时候也可以不用写字段声明 ]
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    # class_null = serializers.CharField()
    # description = serializers.CharField()

    # 2. 可选[ 如果序列化器继承的是ModelSerializer，则需要声明对应的模型和字段, ModelSerializer是Serializer的子类 ]

    # 3. 可选[ 用于对客户端提交的数据进行验证 ]

    # 4. 可选[ 用于把通过验证的数据进行数据库操作，保存到数据库 ]



"""
  在drf中，对于客户端提供的数据，往往需要验证数据的有效性，这部分代码是写在序列化器中的。
  在序列化器中，已经提供三个地方给我们针对客户端提交的数据进行验证。
  1. 内置选项，字段声明的小圆括号中，以选项存在作为验证提交
  2. 自定义方法，在序列化器中作为对象方法来提供验证[ 这部分验证的方法，必须以"validate_<字段>" 或者 "validate" 作为方法名 ]
  3. 自定义函数，在序列化器外部，提前声明一个验证代码，然后在字段声明的小圆括号中，通过 "validators=[验证函数１,验证函数２...]"
"""


def check_user(data):
    if data == "oldboy":
        raise serializers.ValidationError("用户名不能为oldboy！")
    return data



class Student2Serializer(serializers.Serializer):
    # 声明序列化器
    # 1. 字段声明[ 要转换的字段，当然，如果写了第二部分代码，有时候也可以不用写字段声明 ]
    name = serializers.CharField(max_length=10, min_length=4, validators=[check_user])
    sex = serializers.BooleanField(required=True)
    age = serializers.IntegerField(max_value=150, min_value=0)

    # 3. 可选[ 用于对客户端提交的数据进行验证 ]
    """验证单个字段值的合法性"""
    def validate_name(self, data):
        if data == "root":
            raise serializers.ValidationError("用户名不能为root！")
        return data

    def validate_age(self, data):
        if data < 18:
            raise serializers.ValidationError("年龄不能小于18")
        return data

    """验证多个字段值的合法性"""

    def validate(self, attrs):
        name = attrs.get('name')
        age = attrs.get('age')

        if name == "alex" and age == 22:
            raise serializers.ValidationError("alex在22时的故事。。。")

        return attrs

    def create(self, validated_data):
        print(validated_data)
        name = validated_data.get("name")
        sex = validated_data.get("sex")
        age = validated_data.get("age")

        instance = Student.objects.create(name=name, sex=sex, age=age)
        # instance = Student.objects.create(**validated_data)

        return instance

    def update(self, instance, validated_data):

        instance.name = validated_data.get("name")
        instance.sex = validated_data.get("sex")
        instance.age = validated_data.get("age")

        instance.save()

        return instance


class Student3Serializer(serializers.Serializer):
    # 将序列化与反序列整合成一个序列化器类
    # 1. 字段声明[ 要转换的字段，当然，如果写了第二部分代码，有时候也可以不用写字段声明 ]
    name = serializers.CharField(max_length=10, min_length=4, validators=[check_user])
    sex = serializers.BooleanField(required=True)
    age = serializers.IntegerField(max_value=150, min_value=0)

    # 3. 可选[ 用于对客户端提交的数据进行验证 ]
    """验证单个字段值的合法性"""

    def validate_name(self, data):
        if data == "root":
            raise serializers.ValidationError("用户名不能为root！")
        return data

    def validate_age(self, data):
        if data < 18:
            raise serializers.ValidationError("年龄不能小于18")
        return data

    """验证多个字段值的合法性"""

    def validate(self, attrs):
        name = attrs.get('name')
        age = attrs.get('age')

        if name == "alex" and age == 22:
            raise serializers.ValidationError("alex在22时的故事。。。")

        return attrs

    # 第四部分， 数据保存
    def create(self, validated_data):
        print(validated_data)
        name = validated_data.get("name")
        sex = validated_data.get("sex")
        age = validated_data.get("age")

        instance = Student.objects.create(name=name, sex=sex, age=age)
        # instance = Student.objects.create(**validated_data)

        return instance

    def update(self, instance, validated_data):

        instance.name = validated_data.get("name")
        instance.sex = validated_data.get("sex")
        instance.age = validated_data.get("age")

        instance.save()

        return instance


class Student4ModelSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=10, min_length=4, validators=[check_user])

    # 第二部分代码
    class Meta:
        model = Student
        # fields = "__all__"  # 表示引用所有字段
        fields = ["id", "name", "age", "class_null", "is_18"]  # is_18 为自定制字段，需要在models里自定义方法。
        # exclude = ["age"]  # 使用exclude可以明确排除掉哪些字段, 注意不能和fields同时使用。
        # 传递额外的参数，为ModelSerializer添加或修改原有的选项参数
        extra_kwargs = {
            "name": {"max_length": 10, "min_length": 4, "validators": [check_user]},
            "age": {"max_value": 150, "min_value": 0},
        }

    # 第三部分　数据校验
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

    # 第四部分　数据保存不用自己写了