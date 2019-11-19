# coding=utf-8
"""
author = jamon
"""

import copy

from random import randint, randrange


def shuffle_card1(card_array=[]):
    """
     1. 从还没处理的数组（假如还剩k个）中，随机产生一个[0, k]之间的数字p（假设数组从0开始）；
     2. 从剩下的k个数中把第p个数取出；
     3. 重复步骤2和3直到数字全部取完；
     4. 从步骤3取出的数字序列便是一个打乱了的数列。
    """
    result = []
    while card_array:
        p = randrange(0, len(card_array))
        result.append(card_array[p])
        card_array.pop(p)
    return result


def shuffle_card2(card_array=[]):
    """
    每次从从处理的数据中随机取出一个数字，然后把该数字放在新的数组的头部，即数组头部存放的是已经处理过的数字
    :param card_array:
    :return:
    """
    result = copy.deepcopy(card_array)
    card_count = len(card_array)
    for j in range(0, card_count - 1):
        random_num = randint(j + 1, card_count - 1)
        result[j], result[random_num] = result[random_num], result[j]
    return result


def shuffle_card3(card_array=[]):
    """
    每次从从处理的数据中随机取出一个数字，然后把该数字放在数组的头部，即数组头部存放的是已经处理过的数字
    :param card_array:
    :return:
    """
    card_count = len(card_array)
    for j in range(0, card_count - 1):
        random_num = randint(j + 1, card_count - 1)
        card_array[j], card_array[random_num] = card_array[random_num], card_array[j]


if __name__ == "__main__":
    cards = [i for i in range(1, 54)]
    print("原始牌为：", cards)
    shuffle_card1(cards)
    shuffle_card2(cards)
    shuffle_card1(cards)
    print("洗牌后为：", cards)