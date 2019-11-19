# coding=utf-8
"""
author = jamon
"""

# 归并排序
def merge_sort(alist):
    n = len(alist)

    # 递归结束条件
    if n <= 1:
        return alist

    # 中间位置
    mid = n // 2
    # 递归拆分左侧
    left_li = merge_sort(alist[:mid])
    # 递归拆分右侧
    right_li = merge_sort(alist[mid:])
    # 需要2个游标，分别指向左列表和右列表第一个元素
    left_point, right_point = 0, 0
    # 定义最终返回的结果集
    result = []
    # 循环合并数据
    while left_point < len(left_li) and right_point < len(right_li):
        # 谁小谁放前面
        if left_li[left_point] <= right_li[right_point]:
            # 放进结果集
            result.append(left_li[left_point])
            # 游标移动
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1
    # 退出循环时，形成左右两个序列
    result += left_li[left_point:]
    result += right_li[right_point:]
    return result


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    sort_li = merge_sort(li)
    print(li)
    print(sort_li)