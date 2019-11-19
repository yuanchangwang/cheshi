from django.test import TestCase

# Create your tests here.


class A:
    def __init__(self, name):
        self.name = name

    def __setitem__(self, key, value):
        print("setitem")

    def __getitem__(self, item):
        print("getitem")


a = A("alex")
print(a.name)
a["age"] = 18
a['name']
