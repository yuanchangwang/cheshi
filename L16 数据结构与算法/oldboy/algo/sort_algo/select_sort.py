# coding=utf-8
"""
author = jamon
"""


def select_sort(alist):
    n = len(alist)
    # 外层控制比较几轮
    for j in range(n - 1):
        min_index = j
        # 内层控制元素比较和更新索引
        for i in range(j + 1, n):
            # 进行比较
            if alist[min_index] > alist[i]:
                # 更新索引
                min_index = i
        # 退出循环后，交换数据
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
    li = [3, 11, 26, 26, 7, 3, 9, 4]
    print(li)
    select_sort(li)
    print(li)