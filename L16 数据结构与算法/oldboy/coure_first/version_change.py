# coding=utf-8
"""
author = jamon
"""

if __name__ == "__main__":
    import sys
    sys.path.append("../")


'''
def run_on_python27():
    """
    Python27 代码示例
    :return:
    """
    print "老男孩"

'''


def run_on_python3():
    """
    Python3 代码示例
    :return: None
    """
    print("老男孩")

    a = "老男孩"
    b = a.encode("utf-8")
    c = b.decode("utf-8")
    print("a is {}, b is {}, c is {}".format(type(a), type(b), type(c)))


def python3_new_feature(a: "first param", b: "第二个参数", c: float = 10) -> int:
    print("函数注释新特性:", a, b, c)
    return 0


if __name__ == "__main__":
    run_on_python3()
    python3_new_feature("jiayou", "ok", ["test"])
    print(python3_new_feature.__annotations__)