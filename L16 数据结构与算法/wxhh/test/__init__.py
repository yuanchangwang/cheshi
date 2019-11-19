# coding=utf-8
import json
import websocket
import struct
from utils import AesEncoder, ConfigParser



class BaseTestClient(object):
    def __init__(self, config_file='config.ini'):
        self.all_config = ConfigParser(config_file)
        self.response_seq = self.all_config.get("RESPONSE_SEQ")
        self.encode_type = self.all_config.get("ENCODE_TYPE")
        # print "@"*88,"all_config=", self.all_config
        ip = self.all_config.get('IP')
        port = self.all_config.get('PORT')
        address = (ip, port)
        websocket.enableTrace(True)
        self.client = websocket.WebSocketApp(
            url='ws://%s:%s' % address,
            on_message=self.on_message,
            on_open=self.on_open,
            on_close=self.on_close,
            on_error=self.on_error
        )

        self.fmt = 'iii'
        self.version = 0
        self.head_len = struct.calcsize(self.fmt)
        print "encode_type=", self.encode_type
        self.aes_encoder = AesEncoder(encode_type=self.encode_type)

    def pack(self, data, command_id):
        """
        打包消息， 用於傳輸
        :param data:  傳輸數據
        :param command_id:  消息ID
        :return:
        """
        data = json.dumps(data)
        data = self.aes_encoder.encode(data)
        data = "%s" % data
        length = data.__len__() + self.head_len
        # head = struct.pack("", length, command_id, self.version)
        head = struct.pack(self.fmt, length, command_id, self.version)
        return str(head + data)

    def unpack(self, data):
        # print "!"*20,"data=",[data]
        if len(data) < self.head_len:
            return None

        head = data[0:self.head_len]
        list_head = struct.unpack(self.fmt, head)
        # print "-"*30,'return head is',list_head
        result = data[self.head_len:]
        if self.encode_type == 1:
            result = self.aes_encoder.decode_aes(result)
        if not result:
            result = {}
            # return None
        return {'result': True, 'command': list_head[1], 'data': result}

    def send(self, data):
        self.client.send(data, opcode=websocket.ABNF.OPCODE_BINARY)

    def on_message(self, ws, message):
        print "on_message:"

    def on_error(self, ws, error):
        print '====== ERROR ======'
        print error
        print '====== ERROR ======'

    def on_close(self, ws):
        print '### closed ###'

    def on_open(self, ws):
        print '### opened ###'
        raise NotImplementedError

    def run(self):
        # print "ccccccccccccccccccccccccccccclient:", self.client
        self.client.run_forever()


if __name__ == '__main__':
    client = BaseTestClient(config_file='config.ini')
    client.run()
