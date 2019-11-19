# coding=utf-8
"""
author = jamon
"""
import functools
import time


def calSubSet(sum_value, digit_list=[]):
    """
    求一个指定数组中等于和的所有子集
    （此处主要用到递归思路）
    :param sum_value: int
    :param digit_list: []
    :return: [[], [], [], ...]
    """
    result = []
    for i, d in enumerate(digit_list):
        if d == sum_value:
            result.append([d])
            continue
        if i == len(digit_list)-1:
            break
        #开始递归
        new_list = digit_list[i+1:]
        sub_result = calSubSet(sum_value-d, new_list)
        if sub_result:
            temp = []
            # 返回格式调整
            for t in sub_result:
                if t:
                    s = [d]
                    s.extend(t)
                    temp.append(s)
            result.extend(temp)

    # 此处有部分可优化空间，以空间换区时间的方法，将等于指定和的组合用字典缓存起来，下一次首先直接从字典取，会减少较大的重复计算，但内存空间增长较快
    return result


@functools.lru_cache(maxsize=512)
def calSubSet2(sum_value, digit_list=[]):
    """
    求一个指定数组中等于和的所有子集
    （此处主要用到递归思路）
    :param sum_value: int
    :param digit_list: []
    :return: [[], [], [], ...]
    """
    result = []
    for i, d in enumerate(digit_list):
        if d == sum_value:
            result.append([d])
            continue
        if i == len(digit_list)-1:
            break
        #开始递归
        new_list = digit_list[i+1:]
        sub_result = calSubSet(sum_value-d, tuple(new_list))
        if sub_result:
            temp = []
            # 返回格式调整
            for t in sub_result:
                if t:
                    s = [d]
                    s.extend(t)
                    temp.append(s)
            result.extend(temp)

    # 此处有部分可优化空间，以空间换区时间的方法，将等于指定和的组合用字典缓存起来，下一次首先直接从字典取，会减少较大的重复计算，但内存空间增长较快
    return result


if __name__ == "__main__":
    sum_value = 10
    # 正整数测试案例
    digit_list = [2, 3, 5, 7, 6, 8, 9, 4, 10]
    s1 = time.time()

    for i in range(1000):
        ret = calSubSet(sum_value, digit_list)
    s2 = time.time()
    for i in range(1000):
        ret2 = calSubSet2(sum_value, tuple(digit_list))
    s3 = time.time()
    print("origin took {}s, add lru_cache took {}s".format(s2-s1, s3-s2))

    # 带负数测试
    digit_list = [2, 3, 5, 7, 6, 8, 9, 4, 10, -7]
    ret = calSubSet(sum_value, digit_list)
    print(ret)
