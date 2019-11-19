# coding=utf-8

"""

"""

import json
import traceback

from controller import localServiceHandle
from game.logic import *
from share.message_id import *


@localServiceHandle
def login_5000(key, session_id, request_proto={}):
    """
    用户登录消息处理
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """
    print "login_5000 session_id=", session_id
    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)
        logger.info("login_5000:{0}".format(str(request_proto)))
        user_name = request_proto.get("user_name", "")
        passwd = request_proto.get("passwd", "")
        if not user_name or not passwd:
            ret = {"command": KEY_GAME_LOGIN, "code": 0, "info": {"desc": "Param error!"}}
            return json.dumps(ret)
        result, info = login(session_id, user_name, passwd)
        ret = {"command": KEY_GAME_LOGIN, "code": result, "info": info}
        return json.dumps(ret)
    except Exception, e:
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_LOGIN, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def register_5001(key, session_id, request_proto={}):
    """
    用户注册消息处理
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """
    print u"bbbbbbbbbb:", key, session_id, request_proto
    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)
        logger.info("login_5000:{0}".format(str(request_proto)))
        user_name = request_proto.get("user_name", "")
        passwd = request_proto.get("passwd", "")
        if not user_name or not passwd:
            ret = {"command": KEY_GAME_REGISTER, "code": 0, "info": {"desc": "Param error!"}}
            return json.dumps(ret)

        result, info = register(session_id, user_name, passwd, user_name)
        ret = {"command": KEY_GAME_REGISTER, "code": result, "info": info}
        return json.dumps(ret)
    except Exception, e:
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_REGISTER, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def register_5003(key, session_id, request_proto={}):
    ret = get_rooms_people()
    return ret


@localServiceHandle
def enter_10000(key, session_id, request_proto={}):
    """
    用户进入游戏
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """
    print u"enter_10000:", key, session_id, request_proto
    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)

        user_id = request_proto.get("user_id")
        print "enter_1000 user_id", user_id
        ret, info = enter(session_id)
        ret = {"command": KEY_GAME_ENTER, "code": ret, "info": info}
        return json.dumps(ret)
    except Exception, e:
        print "exception=", e
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_ENTER, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def exit_10001(key, session_id, request_proto={}):
    """
    用户退出
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """
    print "exit_10001 : ", session_id
    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)

        ret, info = exit_classic_wx(session_id)
        ret = {"command": KEY_GAME_EXIT, "code": ret, "info": info}
        return json.dumps(ret)
    except Exception, e:
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_CLASSIC_WX_EXIT, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def exit_10004(key, session_id, request_proto={}):
    """
    用户退出整个游戏
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """
    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)

        ret, info = exit(session_id)
        ret = {"command": KEY_GAME_EXIT, "code": ret, "info": info}
        return json.dumps(ret)
    except Exception, e:
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_EXIT, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def bet_10002(key, session_id, request_proto={}):
    """
    用户下注
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """
    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)
        logger.info("login_5000:{0}".format(str(request_proto)))
        user_id = int(request_proto.get("user_id", -1))
        bet_num = int(request_proto.get("num", -1))
        bet_card_type = int(request_proto.get("card_type", -1))
        if -1 == user_id or -1 == bet_num or -1 == bet_card_type:
            ret = {"command": KEY_GAME_BET, "code": 0, "info": {"desc": "Param error!"}}
            return json.dumps(ret)
        result, info = bet(session_id, bet_num, bet_card_type)
        ret = {"command": KEY_GAME_BET, "code": result, "info": info}
        return json.dumps(ret)
    except Exception, e:
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_BET, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def bet_10005(key, session_id, request_proto={}):
    """
    用户下注
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """

    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)
        logger.info("login_5000:{0}".format(str(request_proto)))
        user_id = int(request_proto.get("user_id", -1))
        bet_list = request_proto.get("bet_list", [])
        if not isinstance(bet_list, list):
            return json.dumps({"command": KEY_GAME_BET_BATCH, "code": 0, "info": {"desc": "Param error!"}})
        if -1 == user_id or not isinstance(bet_list,list) or len(bet_list) != 5:
            ret = {"command": KEY_GAME_BET, "code": 0, "info": {"desc": "Param error!"}}
            return json.dumps(ret)
        result, info = bet_batch(session_id, bet_list)
        ret = {"command": KEY_GAME_BET, "code": result, "info": info}
        return json.dumps(ret)
    except Exception, e:
        print "bet_10005 error:", e
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_BET_BATCH, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def cancelbet_10006(key, session_id, request_proto={}):
    """
    玩家取消下注
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """

    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)
        logger.info("cancelbet_10006:{0}".format(str(request_proto)))
        result, info = cancel_bet(session_id)
        ret = {"command": KEY_GAME_CANCEL_BET, "code": result, "info": info}
        return json.dumps(ret)
    except Exception, e:
        print "cancelbet_10006 error:", e
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_CANCEL_BET, "code": 0, "info": {"desc": "Unknown error!"}})


@localServiceHandle
def getRecord_10003(key, session_id, request_proto={}):
    """
    获取某一页的开奖结果
    :param key:
    :param session_id:
    :param request_proto:
    :return:
    """
    try:
        if isinstance(request_proto, str):
            request_proto = json.loads(request_proto)
        logger.info("getRecord_10003:{0}".format(str(request_proto)))
        user_id = int(request_proto.get("user_id", -1))
        page_num = int(request_proto.get("num", 1))
        if -1 == user_id or 0 >= page_num:
            ret = {"command": KEY_GAME_GET_RECORD, "code": 0, "info": {"desc": "Param error!"}}
            return json.dumps(ret)
        result, info = get_record(page_num)
        ret = {"command": KEY_GAME_GET_RECORD, "code": result, "info": info}
        return json.dumps(ret)
    except Exception, e:
        logger.error(traceback.format_exc())
        return json.dumps({"command": KEY_GAME_GET_RECORD, "code": 0, "info": {"desc": "Unknown error!"}})
