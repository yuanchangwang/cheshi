# coding=utf-8
"""
author = jamon
"""

import gc
import objgraph
import sys
import weakref


def quote_demo():
    class Person:
        pass

    p_xxx = Person() # 1

    print(sys.getrefcount(p_xxx))


    def log(obj):
        print(sys.getrefcount(obj))


    log(p_xxx)

    p2 = p_xxx
    print(sys.getrefcount(p_xxx))
    del p2
    print(sys.getrefcount(p_xxx))


def circle_quote():
    # 循环引用
    class Dog:
        pass

    class Person():
        pass

    p = Person()
    d = Dog()

    print(objgraph.count("Person"))
    print(objgraph.count("Dog"))

    p.pet = d
    d.master = p

    # 删除 p, d之后, 对应的对象是否被释放掉
    del p
    del d

    print(objgraph.count("Person"))
    print(objgraph.count("Dog"))


def solve_cirecle_quote():
    # 1. 定义了两个类
    class Person:
        def __del__(self):
            print("Person对象, 被释放了")

        pass

    class Dog:
        def __del__(self):
            print("Dog对象, 被释放了")

        pass

    p = Person()
    d = Dog()

    p.pet = d
    d.master = p

    p.pet = None  # 强制置 None
    del p
    del d

    gc.collect()

    print(objgraph.count("Person"))
    print(objgraph.count("Dog"))


def sovle_circle_quote_with_weak_ref():
    # 1. 定义了两个类
    class Person:
        def __del__(self):
            print("Person对象, 被释放了")

        pass

    class Dog:
        def __del__(self):
            print("Dog对象, 被释放了")

        pass

    p = Person()
    d = Dog()

    p.pet = d
    d.master = weakref.ref(p)

    del p
    del d

    gc.collect()

    print(objgraph.count("Person"))
    print(objgraph.count("Dog"))


if __name__ == "__main__":
    # quote_demo()
    # circle_quote()
    # solve_cirecle_quote()
    # sovle_circle_quote_with_weak_ref()



    url = 'https%3A//oss.100bsh.com/63/8b/813f3c748101.jpg'
    import urllib.parse
    print(urllib.parse.unquote(url))
