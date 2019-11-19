# coding=utf-8

import json

from firefly.server.globalobject import rootserviceHandle, GlobalObject
from firefly.utils.services import CommandService
from twisted.internet import defer

SESSION_SERVER_DICT = {}
print "controller init!"

class LocalService(CommandService):
    def callTargetSingle(self, targetKey, *args, **kw):
        self._lock.acquire()
        try:
            target = self.getTarget(targetKey)
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


local_service = LocalService("local_service")


def localServiceHandle(target):
    local_service.mapTarget(target)


@rootserviceHandle
def forwarding_game(key, sessionid, request_proto):
    print u"forwarding_game:", key, sessionid
    if local_service._targets.has_key(key):
        return local_service.callTarget(key, sessionid, request_proto)


def get_server_name(sessionid):
    global SESSION_SERVER_DICT
    server_name = SESSION_SERVER_DICT.get(sessionid, None)
    if not server_name:
        childs = GlobalObject().root.childsmanager._childs
        game_child_list = filter(lambda x: x.find("game") >= 0, childs)
        server_name = game_child_list[0]
        SESSION_SERVER_DICT[sessionid] = server_name

    return server_name


@rootserviceHandle
def proxy_connect_lost(sessionid):
    if sessionid in SESSION_SERVER_DICT.keys():
        del SESSION_SERVER_DICT[sessionid]




