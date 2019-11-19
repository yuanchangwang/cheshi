# coding=utf-8
"""
author = jamon
"""
import bitarray
import sys


class BitArray(object):

    def __init__(self):
        self.array = [0 for i in range(1024*1024*1024)]

    def set_bit(self, digit):
        i = digit >> 5
        d_mod = digit & 0xffff
        self.array[i] = self.array[i] | d_mod

    def get_bit(self, digit):
        i = digit >> 5
        d_mod = digit & 0xffff
        return self.array[i]
