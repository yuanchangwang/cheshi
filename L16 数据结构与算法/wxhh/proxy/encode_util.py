# coding=utf-8

"""

"""

from Crypto.Cipher import AES
from firefly.utils.singleton import Singleton

import json

class AesEncoder:
    __metaclass__ = Singleton

    NONE_TYPE = 0
    AES_TYPE = 1

    def __init__(self, password='@ZYHD#GDMJ!112233!love**foreverX', encode_type=0):
        self.aes_obj = AES.new(password)
        self.encode_type = encode_type

    def encode(self, msg):
        if self.encode_type == self.NONE_TYPE:
            return msg
        elif self.encode_type == self.AES_TYPE:
            return self.encode_aes(msg)

    def encode_aes(self, msg):
        msg_len = len(msg)
        need_len = msg_len % 16
        if need_len != 0:
            need_len = 16 - need_len
            msg += " " * need_len
        return self.aes_obj.encrypt(msg)

    def decode_aes(self, msg):
        try:
            decode_msg = self.aes_obj.decrypt(msg)
        except Exception, e:
            return None

        msg_len = len(decode_msg)
        if msg_len == 0:
            return decode_msg

        try:
            json.loads(decode_msg)
        except ValueError:
            return None
        return decode_msg

    def decode(self, msg):
        if self.encode_type == self.NONE_TYPE:
            return msg
        elif self.encode_type == self.AES_TYPE:
            return self.decode_aes(msg)