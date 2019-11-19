# coding=utf-8
"""
author = jamon
"""


def bubble_sort(alist):
    # 外层循环控制比较几轮
    n = len(alist)
    for j in range(n - 1):
        # 内存循环控制交换
        # -j是不再换已经排好的
        for i in range(n - 1 - j):
            # 若前一个比后一个大，则换
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def bubble_sort2(alist):
    # 外层循环控制比较几轮
    n = len(alist)
    for j in range(n - 1):
        # 定义计数器
        count = 0
        # 内存循环控制交换
        # -j是不再换已经排好的
        for i in range(n - 1 - j):
            # 若前一个比后一个大，则换
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # 计数器
                count += 1
        if count == 0:
            return


if __name__ == '__main__':
    li = [33, 11, 26, 78, 3, 9, 40]
    print(li)
    bubble_sort(li)
    print(li)
