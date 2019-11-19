# coding=utf-8
"""
author = jamon
"""


# 快排
# first理解为第一个位置的索引，last是最后位置索引
def quick_sort(alist, first, last):
    # 递归终止条件
    if first >= last:
        return

        # 设置第一个元素为中间值
    mid_value = alist[first]
    # low指向
    low = first
    # high
    high = last
    # 只要low小于high就一直走
    while low < high:
        # high大于中间值，则进入循环
        while low < high and alist[high] >= mid_value:
            # high往左走
            high -= 1
        # 出循环后，说明high小于中间值,low指向该值
        alist[low] = alist[high]
        # high走完了，让low走
        # low小于中间值，则进入循环
        while low < high and alist[low] < mid_value:
            # low向右走
            low += 1
        # 出循环后，说明low大于中间值,high指向该值
        alist[high] = alist[low]
    print(alist)
    # 退出整个循环后，low和high相等
    # 将中间值放到中间位置
    alist[low] = mid_value
    # 递归
    # 先对左侧快排
    quick_sort(alist, first, low - 1)
    # 对右侧快排
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)