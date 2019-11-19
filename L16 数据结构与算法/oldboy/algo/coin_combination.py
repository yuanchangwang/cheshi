# coding=utf-8
"""
author = jamon
"""

import copy
import time


def _cal_min_common_multiple(x, y):
    """
    求最小公倍数
    :param x: int
    :param y: int
    :return: int
    """
    greater = x if x > y else y

    while 1:
        if (greater % x == 0) and (greater % y == 0):
            result = greater
            break
        greater += 1

    return result


def cal_min_common_multiple(digit_list=[]):
    """
    求最小公倍数
    :param digit_list: [int, int, ...]
    :return: int
    """

    if 2 > len(digit_list):
        return 0
    temp = digit_list[0]
    for i in range(len(digit_list)-1):
        temp = _cal_min_common_multiple(temp, digit_list[i+1])
    return temp


def _get_a_combination(min_multiple, target_num, origin_coins={}):
    """
    根据指定的硬币种类和个数推导判断是否能够组成指定的硬币数字总价
    :param min_multiple: int, 硬币种类的最小公倍数
    :param target_num: int， 待组合的目标硬币总额，需为min_multiple倍数， 如八块七，则算为87
    :param origin_coins: dictionary, {key: num, key2:num2, ...} 即 {一分：一分硬币个数，二分：二分硬币个数，...}
    :return: {}, 返回一个成功的组合
    """
    if 0 != target_num % min_multiple or 0 > target_num:
        return {}
    # print("_get_a:", target_num, origin_coins)
    temp1 = int(target_num/min_multiple)
    result = {}
    for v in origin_coins.values():
        if 0 > v:
            return {}
    for k, v in origin_coins.items():
        temp2 = int(v/(min_multiple/k))
        if temp2 >= temp1:
            result[k] = temp1
            return result
        else:
            result[k] = temp2
            temp1 = temp1 - temp2

    return {}


def compute_array_left(min_multiple, digit_list=[]):
    """
    计算数组内最小公倍数下的余数
    :param min_multiple: 最小公倍数
    :param digit_list: [int, int, ...]
    :return: {和1：[{int: num, int2: num2}, {}, ...]}
    """
    if not digit_list:
        return {}
    temp_dict = {}  # {87: [{2:10, 5:6, ...}, ...]}
    n = 0
    for k in digit_list:
        for _ in range(int(min_multiple / k) - 1):
            if not temp_dict:
                temp_dict[k] = [{k: 1}]  # 控制后第一次遍历初始化
            temp_dict2 = copy.deepcopy(temp_dict)
            # print("bbbbbb:", n)
            n += 1
            for x, y in temp_dict.items():
                temp = copy.deepcopy(y)  # temp=[{2:5}, ...]
                # 原有的值内容个数累加1，没有则新键内容个数置为1

                for i, t in enumerate(temp):
                    temp[i][k] = 1 if k not in temp[i].keys() else temp[i][k] + 1
                if x + k not in temp_dict.keys():  # 判断新和key是否已存在，不存在则新建，存在则添加到列表末尾
                    temp_dict2[x + k] = temp
                else:
                    for t in temp:
                        if t not in temp_dict2[x + k]:
                            temp_dict2[x + k].append(t)
                temp_dict = temp_dict2
    return temp_dict


def find_coin_combination(target_num, origin_coins={}):
    """
    根据指定的硬币种类和个数推导判断是否能够组成指定的硬币数字总价
    算法思路：该类问题实际上可以转化为三个问题：
        1. 求指定硬币种类的最小公倍数；
        2. 在硬币个数充足的情况下不同类型硬币相加的余数的组合；
        3. 逐步考虑部分硬币类型个数不足情况下组合；
    :param target_num: int， 待组合的目标硬币总额，如八块七，则算为87
    :param origin_coins: dictionary, {key: num, key2:num2, ...} 即 {一分：一分硬币个数，二分：二分硬币个数，...}
    :return: dictionary, 返回组合的情况,{key: use_num, key2: use_num2, ...}
    """
    min_multiple = cal_min_common_multiple(list(origin_coins.keys()))
    # print("最小公倍数为:", min_multiple)
    left_num = target_num % min_multiple

    # 计算各硬币组成的最小公倍数之外的余数数值（余数组合范围在0-硬币类型数*最小公倍数之间）
    # 此部分一但硬币类型确定后，该部分可以预处理，一次计算，多次复用该结果，所以在计算复杂度时可忽略
    left_key = ",".join([str(i) for i in origin_coins.keys()])
    if not hasattr(find_coin_combination, "left_cache"):
        find_coin_combination.left_cache = {}
    if left_key not in find_coin_combination.left_cache.keys():
        find_coin_combination.left_cache[left_key] = compute_array_left(min_multiple, list(origin_coins.keys()))
        # print("预处理的余数数值为：")
        # for k, v in find_coin_combination.left_cache[left_key].items():
        #     print(" ", k, v)
    temp_dict = find_coin_combination.left_cache[left_key]

    # 判断余数是否在预计算的数值集合中（余数组合范围在0-硬币类型数*最小公倍数之间）
    # 余数相加的范围是固定的，不随着target的变化而变化，所以时间复杂度还是O(1)
    # print("硬币数值类型为{0}, 相应类型的原始硬币个数为{1}, 欲拼凑的数字总额为 {2}".format(left_key, str(origin_coins), target_num))
    result = {}
    for i in range(len(origin_coins)):
        left = left_num + min_multiple * i

        if left in temp_dict.keys():
            left_result = temp_dict[left]  # left_result: [{2:10, 5:6, ...}, ...]
            for t in left_result:
                temp_coins = copy.deepcopy(origin_coins)
                for k, v in t.items():
                    temp_coins[k] = temp_coins[k] - v
                temp = _get_a_combination(min_multiple, target_num-left, temp_coins)
                if not temp:
                    # print("bbbbbb:",  temp, min_multiple, target_num, left, temp_coins)
                    continue
                # print("aaaaaa:", temp, min_multiple, target_num, left, temp_coins)
                # 找到一个组合，返回
                result.update(temp)
                for k, v in t.items():
                    result[k] = v if k not in result.keys() else result[k]+v
                print("答案为：{0}\n".format(result))
                return result

    print("未能计算得到答案\n")
    return {}


if __name__ == "__main__":
    find_coin_combination(87, origin_coins={10: 9, 5: 3, 2: 6})
    find_coin_combination(93, origin_coins={10: 9, 5: 3, 2: 6})

    #find_coin_combination(111, origin_coins={10: 9, 5: 3, 2: 6})

    find_coin_combination(29, origin_coins={7: 19, 5: 3, 3: 6})
    find_coin_combination(83, origin_coins={7: 19, 5: 3, 3: 6})