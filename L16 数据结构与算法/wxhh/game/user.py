# coding=utf-8

"""

"""
from models.model_user import MUser
from share.ibbgame_log import logger


class User(object):
    def __init__(self, user_id, session_id=""):
        self.user_id = user_id
        self.session_id = session_id

        self.is_playing = True

        self.gold = 0
        self.update()

    def update(self):
        ret, info = MUser.get_user_info_by_id(self.user_id)
        if ret:
            self.gold = info.get("gold", 0)
        else:
            logger.warning("update user({0}) error!".format(self.user_id))

    def set_user_gold(self, change_num):
        self.gold += change_num
        ret, info = MUser.update_user_gold(self.user_id, change_num)

        if self.gold != info.get("gold", ""):
            logger.error("set_user_gold error! ({0}, {1})".format(self.user_id, change_num))
        return self.gold

    def set_user_gold_for_settle(self, user_gold):
        ret, info = MUser.set_user_gold(self.user_id, user_gold)
        return user_gold