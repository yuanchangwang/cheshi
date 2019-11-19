# coding=utf-8

"""

"""

from firefly.server.globalobject import GlobalObject, remoteserviceHandle
from twisted.internet import reactor
from controller import websocket_factory

DISCONNECT_CLIENT_INTERVAL = 0.5
CLOSE_NORMAL = 1000
CLOSE_SOCKET_CODE = 10000

@remoteserviceHandle("game")
def push_object(msgid, msg, send_list):
    print "push_object:", msgid, msg, send_list
    data = websocket_factory._datapack._pack(msg, msgid)
    websocket_factory.push_object(send_list, data, True)

@remoteserviceHandle("game")
def disconnect_client(sessionid):
    reactor.callLater(DISCONNECT_CLIENT_INTERVAL, websocket_factory._clients[sessionid].sendClose, CLOSE_NORMAL, "task over".decode())
