# coding=utf-8

"""

"""

from firefly.server.globalobject import GlobalObject
import json

def send_one(sessionid, message_id, data):
    x = sessionid.split(",")
    uid = [x[0], int(x[1])] if 2 == len(x) and x[1] else None
    pushmsg(message_id, data, [uid])


def send_all(sessionid_list, message_id, data):
    send_list = []
    for s in sessionid_list:
        if not s:  # 如果session 为空则跳过
            continue
        x = s.split(",")
        uid = [x[0], int(x[1])] if 2 == len(x) and x[1] else None
        send_list.append(uid)
    pushmsg(message_id, data, send_list)


def pushmsg(message_id, msg, send_list):
    if not isinstance(msg, str):
        if isinstance(msg, dict) or isinstance(msg, list):
            msg = json.dumps(msg)
        else:
            msg = str(msg)
    # print "pushmg:::::::::::::::::::", message_id, msg, send_list
    if 0 >= len(send_list):
        return
    server_name = set(p[0] for p in send_list)
    for s in server_name:
        session_uids = []
        for p in send_list:
            if s == p[0]:
                session_uids.append(p[1])
        GlobalObject().root.callChildByName(s, "push_object", message_id, msg, session_uids)
