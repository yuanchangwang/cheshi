# coding=utf-8

"""

"""

from firefly.utils.singleton import Singleton


class CardManager(object):
    __metaclass__ = Singleton

    def __init__(self):
        pass

    def get_type_and_val(self, card):
        type = card >> 4
        value = card & 0x0f
        return type, value

    def cal_card(self, card_type, card_value):
        return (card_type << 4) + (card_value & 0x0f)

    def get_type_and_value(self, cal_card):
        return [cal_card >> 4, cal_card & 0x0f]



if __name__ == "__main__":
    c = CardManager()
    a,b =c.get_type_and_value(51)
    print a