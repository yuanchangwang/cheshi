# coding=utf-8

"""

"""

from firefly.utils.singleton import Singleton

from game.user import User
from game.push_service import send_one
from share.message_id import KEY_PUSH_OTHER_LOGIN

class UserManager(object):
    __metaclass__ = Singleton

    def __init__(self):
        self._session_user_dict = {}
        self._id_user_dict = {}  # user_id -> session_id
        self._classic_wx_session_list = []  # 当前在经典五星场的所有用户
        self._big_away_wx_session_list = []  # 当前在大奖五星场的所有用户  TODO 未启用
        self._mosaic_gold_wx_session_list = []  # 当前在彩金五星场的所有用户  TODO 未启用

    def add_user(self, user_id, session_id):
        if self._id_user_dict.get(user_id, None):
            # 断线重连, 更新session_id
            old_session_id = self._id_user_dict[user_id].session_id
            # 处理异地登录
            self.another_side_login(old_session_id)
            self._id_user_dict[user_id].session_id = session_id
            if old_session_id in self._session_user_dict.keys():
                self._session_user_dict.pop(old_session_id)
            # 移除经典五星原session
            if old_session_id in self._classic_wx_session_list:
                self._classic_wx_session_list.remove(old_session_id)
            self._session_user_dict[session_id] = self._id_user_dict[user_id]
            return 0
        else:
            user = User(user_id, session_id)
            user.user_id

            self._id_user_dict[user_id] = user
            if session_id not in self._session_user_dict.keys():
                self._session_user_dict[session_id] = user

    def another_side_login(self, session_id):
        """
        向原session 推送抢登信息
        :param session_id:
        :return:
        """
        data = {"desc": u"账号在别处登录"}
        send_one(session_id, KEY_PUSH_OTHER_LOGIN, data)


    def offline_user(self, session_id):
        if session_id in self._session_user_dict.keys():
            self._id_user_dict[self._session_user_dict[session_id].user_id].session_id = None
            self._session_user_dict.pop(session_id)


    def exit_user(self, user_id):
        if user_id in self._id_user_dict.keys():
            session_id = self._id_user_dict[user_id].session_id
            if session_id in self._session_user_dict.keys():
                self._session_user_dict.pop(session_id)
            self._id_user_dict.pop(user_id)

    def get_user_by_id(self, user_id):
        return self._id_user_dict.get(user_id, None)

    def get_user_by_sessionid(self, session_id):
        return self._session_user_dict.get(session_id, None)

    def get_session_list(self):
        """
        获取当前游戏在线用户会话列表
        """
        session_list = []
        for k, v in self._id_user_dict.items():
            session_list.append(v.session_id)
        return session_list

    def add_session_to_classic_wx(self, session):
        """
        玩家进入经典五星,将session 加入经典五星用户会话列表用于房间推送
        :return:
        """
        self._classic_wx_session_list.append(session)
        return

    def get_classic_wx_session_list(self):
        """
        获取当前在经典五星,会用回话列表
        :return:
        """
        return self._classic_wx_session_list

    def exit_classic_wx_session_list(self, session_id):
        """
        玩家退出经典五星
        """
        print "exit__classic_wx_session_list=", self._classic_wx_session_list
        self._classic_wx_session_list.remove(session_id)

    def get_session_id_user_id_list(self):
        """
        获取当前用户session userid username list表
        :return:
        """
        session_list = []
        for k, v in self._id_user_dict.items():
            session_list.append(str(k)+":"+v.session_id)
        return session_list