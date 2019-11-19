# coding=utf-8
"""
author = jamon

参考博客：https://www.cnblogs.com/SuKiWX/p/8804974.html
"""

if __name__ == "__main__":
    import sys
    sys.path.append("../")

from threading import Thread
import time


def my_counter():
    i = 0
    for _ in range(10000000):
        i = i + 1
    return True


def single_thread():
    """
    单线程测试
    :return:
    """
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        t.join()
    end_time = time.time()
    print("单线程花费时间: {}".format(end_time - start_time))


def multi_thread():
    """
    多线程测试
    :return:
    """
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_array[tid] = t
    for i in range(2):
        thread_array[i].join()
    end_time = time.time()
    print("多线程花费时间: {}".format(end_time - start_time))


if __name__ == "__main__":
    single_thread()
    multi_thread()