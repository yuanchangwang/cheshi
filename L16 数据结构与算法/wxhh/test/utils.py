# coding=utf-8
from Crypto.Cipher import AES
import json
import types
from firefly.utils.singleton import Singleton

class AesEncoder:
    __metaclass__ = Singleton

    NONE_TYPE = 0
    AES_TYPE = 1

    def __init__(self, password='@ZYHD#GDMJ!112233!love**foreverX', encode_type=1):
        self.aes_obj = AES.new(password)
        self.encode_type = encode_type

    def encode(self, msg):
        print "encode msg:", msg, self.encode_type
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


class ConfigParser(dict):
    def __init__(self, path):
        self.path = path
        super(dict, self).__init__()

        d = types.ModuleType('config')
        d.__file__ = self.path
        try:
            with open(self.path) as config_file:
                exec(compile(config_file.read(), self.path, 'exec'), d.__dict__)
        except IOError as e:
            raise e

        for key in dir(d):
            if key.isupper():
                self[key] = getattr(d, key)

if __name__ == '__main__':
    encoder = AesEncoder()
    from hashlib import md5
    print md5(encoder.encode_aes('test')).hexdigest()
