# coding=utf-8
"""
author = jamon
"""


# 插入排序
def insert_sort(alist):
    n = len(alist)
    # 外层循环控制从右边取多少元素
    for j in range(1, n):
        # i = [1，2，3...]
        i = j
        # 内存循环
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                # 控制循环结束
                i -= 1
            else:
                break


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    insert_sort(li)
    print(li)