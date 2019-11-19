from django.test import TestCase

# Create your tests here.

class A:
    pass


def foo():
    pass

print(isinstance(A, type))  # True   （元类，自己去了解一下）
print(isinstance(foo, type))  # False
