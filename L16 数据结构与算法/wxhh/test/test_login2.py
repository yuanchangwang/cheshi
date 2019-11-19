# coding=utf-8
from __init__ import BaseTestClient
from log import logger
from websocket import ABNF
# from utils import AesEncoder
from twisted.internet import reactor
import random
import Queue
import threading
import inspect
import ujson
import sys
import time

s_time = None
e_time = None
q = Queue.Queue()


def random_weighted_choice(weights):
    rnd = random.random() * sum(weights)
    for i, w in enumerate(weights):
        rnd -= w
        if rnd < 0:
            return i

"""
用于输入的线程
"""
class MyThread(threading.Thread):
    def __init__(self, q):
        super(MyThread, self).__init__()
        self.q = q

    def run(self):
        while True:
            try:
                input_str = input("Enter your bet num!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:")
                if isinstance(input_str, list) and len(input_str) == 5:
                    self.q.put(input_str)
                else:
                    print "input error!!"
            except Exception, e:
                print e
                print "input error"

input_thread = MyThread(q)


class RobotClient(BaseTestClient):
    def __init__(self, config_file, user_id=None, user_name=None):
        BaseTestClient.__init__(self, config_file=config_file)

        # super(RobotClient, self).__init__()
        self.response_seq = self.all_config.get("RESPONSE_SEQ")
        self.sendhandler = {
            5000: self.send_5000,
            5001: self.send_5001,
            10000: self.send_10000,
            10001: self.send_10001,
            10002: self.send_10002,
            10003: self.send_10003,
            10005: self.send_10005,
            999999: self.send_999999
        }
        # self.user_id = 9121
        self.user_id = user_id
        user_name = self.all_config.get("USER_NAME", "test2")
        self.user_name = user_name
        # self.user_id = self.all_config.get("USER_ID")

    def on_open(self, ws):
        print "on_open!!!"
        # self.send_data(100002, {"userid": self.user_id, "pass": self.all_config.get("USER_PASSWORD")}, ws)
        global s_time
        s_time = time.time()
        self.send_5000(ws)

    def on_message(self, ws, message):
        length = self.head_len
        unpackdata = self.unpack(message)
        print "接收数据：", unpackdata
        if unpackdata is None:
            print '!'*20, 'unpack_data is None!'
            return
        command = unpackdata.get('command')
        rlength = unpackdata.get('length')
        data = unpackdata.get("data")
        n = random.randint(1, 3)

        # print "#"*88
        # print u"接收数据:", n, data, command
        # reactor.callLater(n, self.receivehandler, command, data)
        self.receivehandler(ws, command, data)

    def receivehandler(self, ws, key, params):
        if params and isinstance(params, str):
            params = ujson.loads(params)
        global responseConfig
        # print u"接收处理:", key, [params]
        # print "@"*88,'str(key)=', str(key)
        rconfig = self.response_seq.get(str(key), None)
        if not rconfig:
            logger.error("index(%s):Error: response config error! key=%s", 1, str(key))
            # print "@"*88, "rconfig is none"
            return

        if not rconfig.get("msg", None):
            # logger.warning("response has not receiver msg handler")F
            return
        # if key == 100002 and params.get("info"):
        #     return self.send_100801(ws, params)
        random_index = random_weighted_choice(rconfig.get("weight"))
        # print "@"*20, random_index, key, params, rconfig.get("msg")
        return self.sendhandler.get(rconfig.get("msg")[random_index])(ws, params)

    def send_data(self, commandID, data, ws):
        print u"*******发送数据*********：", commandID, data, ws, "||"
        s = self.pack(data, commandID)
        ws.send(s, opcode=ABNF.OPCODE_BINARY)

    def send_5000(self, ws, params={}):
        '''  登录
        '''
        print "@" * 33, 'this is %s' % inspect.stack()[1][3]
        passwd = self.all_config.get("PASSWORD")
        data = {"user_name": self.user_name, "passwd":passwd}
        self.send_data(5000, data, ws)


    def send_5001(self, ws, params={}):
        '''  注册
        '''
        print "@" * 33, 'this is %s' % inspect.stack()[1][3]
        data = {"user_name": self.user_name, "passwd":"8222b2020c704671b9c51d6fdcfe776c"}
        self.send_data(5001, data, ws)

    def send_10000(self, ws, params={}):
        data = {"user_id": self.user_id, "command_id": 10000}
        self.send_data(10000, data, ws)

    def send_10001(self, ws, params={}):
        """
        退出房间请求
        """
        self.send_data(10001, params, ws)

    def send_10002(self, ws, params={}):
        '''  进入快速匹配场坐下
        '''
        data = {"user_id": self.user_id, "command_id": 10002, "num": 1000, "card_type": 0}
        self.send_data(10002, data, ws)

    def send_10003(self, ws, params={}):
        data = {"user_id": self.user_id, "num":10}
        self.send_data(10003, data, ws)


    def send_10005(self, ws, params={}):
        print "is_alive = ", input_thread.is_alive
        if not input_thread.is_alive:
            input_thread.start()
        if not q.empty():
            bet_list = q.get()
            data = {"user_id": self.user_id, "bet_list": bet_list}
            self.send_data(10005, data, ws)
        else:
            print "q is empty!!!"

    def send_999999(self, ws, params={}):
        pass
        # print "stop..."

if __name__ == '__main__':
    input_thread.start()
    reactor.suggestThreadPoolSize(100)
    for i in range(0, 1):
        user_id = 2
        robot = RobotClient("config.ini", user_id=user_id, user_name="15012822291")
        reactor.callInThread(robot.run)
    reactor.run()
    # config_dict= {
    #     "1": "config1.ini",
    #     "2": "config2.ini",
    #     "3": "config3.ini",
    #     "4": "config4.ini"
    # }
    # config_index = None
    # try:
    #     config_index = sys.argv[1]
    #     print config_index in config_dict.keys()
    # except IndexError,e:
    #     print u"请输入config_index (1,2,3,4)"
    # if config_index is not None and config_index in config_dict.keys():
    #     robot = RobotClient(config_dict[config_index])
    #     print "robot config%s start!!!!!"%config_index
    #     reactor.callInThread(robot.run)
    #     reactor.run()
