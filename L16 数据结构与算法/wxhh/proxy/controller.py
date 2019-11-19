# coding=utf-8
"""

"""

from firefly.utils.services import CommandService
from firefly.server.globalobject import GlobalObject, remoteserviceHandle

from twisted.internet import defer, reactor
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

import struct
from encode_util import AesEncoder
from share.ibbgame_log import logger

CLOSE_TIME_OUT = 4000
CLOSE_PROXY_FULL = 4001
CLOSE_COVER = 4002

server_name = "proxy"

class DataProtocol:

    def __init__(self):
        self.handfrt = "iii"
        self.identifier = 0
        self.aes_ins = AesEncoder()
        self.version = 0

    def _get_head_len(self):
        return struct.calcsize(self.handfrt)

    def _unpack(self, pack_data):
        head_len = self._get_head_len()
        print "head_len=", head_len
        print "pack_data=", len(pack_data)
        if head_len > len(pack_data):
            return None

        data_head = pack_data[0:head_len]
        list_head = struct.unpack(self.handfrt, data_head)
        data = pack_data[head_len:]
        result = self.aes_ins.encode(data)
        if not result:
            result = {}
            # return None
        return {'result': True, 'command': list_head[1], 'data': result}

    def _pack(self, data, command_id):
        """
        打包消息， 用於傳輸
        :param data:  傳輸數據
        :param command_id:  消息ID
        :return:
        """
        data = self.aes_ins.encode(data)
        data = "%s" % data
        length = data.__len__() + self._get_head_len()
        head = struct.pack(self.handfrt, length, command_id, self.version)
        return str(head + data)

class ProxyCommandService(CommandService):
    def callTargetSingle(self,targetKey,*args,**kw):
        """

        :param targetKey:
        :param args:
        :param kw:
        :return:
        """
        self._lock.acquire()
        try:
            target = self.getTarget(0)
            if not target:
                return None
            if targetKey not in self.unDisplay:
                pass
            defer_data = target(targetKey, *args, **kw)
            if not defer_data:
                return None
            if isinstance(defer_data, defer.Deferred):
                return defer_data
            d = defer.Deferred()
            d.callback(defer_data)
        finally:
            self._lock.release()
        return d


class WebSocketProtocol(WebSocketServerProtocol):

    def __init__(self):
        WebSocketServerProtocol.__init__(self)
        self.time_out_task = None
        self.connect_timeout = 30 * 60

    def add_new_time_task(self):
        if self.connect_timeout > 0:
            #超时断开连接
            self.close_time_task()
            self.time_out_task = reactor.callLater(self.connect_timeout, self.sendClose, CLOSE_TIME_OUT, "timeout".decode())

    def close_time_task(self):
        if self.time_out_task and self.time_out_task.active():
            self.time_out_task.cancel()
            self.time_out_task = None

    def onConnect(self, request):
        print u"onConnect:"

        self.factory.clients[self.transport.sessionno] = self
        self.add_new_time_task()

    def onOpen(self):
        print u"connect open~"


    def onMessage(self, data, *args):
        print u"onMessage:"
        # print data, args
        ret = self.factory._datapack._unpack(data)
        print u"ret=", ret
        if ret:
            self.add_new_time_task()
            d = proxy_service.callTarget(ret["command"], self, ret["data"])
            if d:
                d.addCallback(self.send_data_for_me, ret["command"])
                # d.addErrback(Defer)

    def onClose(self, *args):
        print u"onClose:", args
        self.close_time_task()
        self.factory.onClose(self)

    def send_data_for_me(self, data, commandID):
        send_data = self.factory.produce_result_for_me(commandID, data)
        self.sendMessage(send_data, isBinary=1)


class CustomWebProxyFactory(WebSocketServerFactory):
    protocol =  WebSocketProtocol

    def __init__(self):
        super(CustomWebProxyFactory, self).__init__()
        self.clients = {}
        self._datapack = DataProtocol()

    def build_protocol(self, addr):
        p = self.protocol()
        p.factory = self
        return p

    def push_object(self, send_list, data, is_binary):
        for sid, client in self.clients.items():
            if sid in send_list:
                client.sendMessage(data, is_binary)

    def onClose(self, close_client):
        print u"factory onClose:"
        for sid, client in self.clients.items():
            if sid == close_client.transport.sessionno:
                session_id = "%s, %d" % (server_name, sid)
                GlobalObject().remote["game"].callRemote("proxy_connect_lost", session_id)
                self.clients.pop(sid)

    def produce_result_for_me(self, command, data):
        print "send_for_player:", data
        send_data = self._datapack._pack(data, command)
        return send_data


websocket_factory = CustomWebProxyFactory()
reactor.listenTCP(10000, websocket_factory)

proxy_service = ProxyCommandService("WebProxyService")
def ProxyServiceHandle(target):
    proxy_service.mapTarget(target)

@ProxyServiceHandle
def forwarding_0(keyname, _conn, data):
    uid = "%s,%d" % (server_name, _conn.transport.sessionno)

    print u"hhhhhhhhhhh:", keyname, _conn
    return GlobalObject().remote["game"].callRemote("forwarding_game", keyname, uid, data)