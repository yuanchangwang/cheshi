# coding=utf-8

"""

"""

import copy
import json
import random
import time

from firefly.utils.singleton import Singleton
from firefly.server.globalobject import GlobalObject
from twisted.internet import reactor

from game.card_manager import CardManager
from game.game_config import Config, CARD_DESC,CARD_JOKER
from game.push_service import send_one, send_all
from game.round_manager import RoundManager
from game.user_manager import UserManager
from share.common_tool import weight_choice
from share.ibbgame_log import logger
from share.message_id import *


print "AwardManager init!!"

class AwardManager(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.is_can_bet = True
        self.remain_bet_time = 0
        self.remain_show_time = 0

        self.is_stop = 0
        self.stop_time = 0
        self.stop_content = ""
        self.test_next_color = []   # 用于测试:下一个开出指定花色

    def call_Later(self, delay, callbackFunc, *args, **kw):
        return reactor.callLater(delay, callbackFunc, *args, **kw)

    def start_bet(self):
        """
        游戏开始,可以押注
        :return:
        """
        if self.stop_time and self.stop_time <= time.time():
            self.is_stop = 1
            logger.debug(u"维护中，游戏暂停")
            send_all(UserManager().get_session_list(), KEY_PUSH_SYSTEM_NOTICE, self.stop_content)
            self.call_Later(10, self.start_bet)
            return
        else:
            self.is_stop = 0
        print u"开始投注"
        self.is_can_bet = True
        self.remain_bet_time = Config().max_bet_time
        self.remain_show_time = Config().max_show_time
        self.call_Later(Config().interval_one_round, self.update_remain_bet_time)

        RoundManager().new_round()
        self.notify_user_game_start()

    def notify_user_game_start(self):
        notify_content = {"round_id": RoundManager().cur_round_id,
                          "cur_award_pool_gold": RoundManager().cur_award_pool_gold}
        send_all(UserManager().get_session_list(), KEY_PUSH_GAME_START, notify_content)

    def update_remain_bet_time(self):
        """
        更新当局游戏剩余时间
        :return:
        """
        self.remain_bet_time -= 1

        if self.remain_bet_time > 0:
            self.call_Later(Config().interval_one_round, self.update_remain_bet_time)
            notice_cotent = json.dumps({
                "spade": RoundManager().cur_round_spade_num, "heart": RoundManager().cur_round_heart_num,
                "club": RoundManager().cur_round_club_num, "diamond": RoundManager().cur_round_diamond_num,
                "joker": RoundManager().cur_round_joker_num, "remain_bet_time": self.remain_bet_time
            })
            print "update_remain_bet_time notice_cotent=", notice_cotent
            if UserManager().get_classic_wx_session_list():
                # 向经典五星场内所有玩家推送信息
                send_all(UserManager().get_classic_wx_session_list(), KEY_PUSH_CURRENT_BET_INFO, notice_cotent)
        else:
            self.call_Later(1, self.settle)

    def settle(self):
        """
        结算

        :return:
        """
        self.is_can_bet = False  # 调整押注状态为 False
        print u"开始结算"
        card_type, card_value = self.get_random_card()
        print u"随机卡牌：", card_type, card_value
        # 计算开不同花色时系统输赢情况
        print "RoundManager().cur_round_total =", RoundManager().cur_round_total
        print "RoundManager().cur_round_spade_num =", -RoundManager().cur_round_spade_num * Config().odds[0]
        print "RoundManager().cur_round_heart_num =", -RoundManager().cur_round_heart_num * Config().odds[0]
        print "RoundManager().cur_round_club_num =", -RoundManager().cur_round_club_num * Config().odds[0]
        print "RoundManager().cur_round_diamond_num =", -RoundManager().cur_round_diamond_num * Config().odds[0]
        print "RoundManager().cur_round_joker_num =", RoundManager().cur_round_joker_num * (1 - Config().odds[4])
        print "RoundManager().cur_round_consume_gold =", -RoundManager().cur_round_consume_gold
        # 计算出开每个点数时候庄家的输赢情况
        diff_card_award_change = [
            RoundManager().cur_round_total - RoundManager().cur_round_spade_num * Config().odds[
                0] - RoundManager().cur_round_consume_gold,
            RoundManager().cur_round_total - RoundManager().cur_round_heart_num * Config().odds[
                1] - RoundManager().cur_round_consume_gold,
            RoundManager().cur_round_total - RoundManager().cur_round_club_num * Config().odds[
                2] - RoundManager().cur_round_consume_gold,
            RoundManager().cur_round_total - RoundManager().cur_round_diamond_num * Config().odds[
                3] - RoundManager().cur_round_consume_gold,
            RoundManager().cur_round_joker_num * (1 - Config().odds[4]) - RoundManager().cur_round_consume_gold
        ]
        print "diff_card_award_change;", diff_card_award_change
        # 当前开出的花色, 输的点数+ 奖池现有金额, 为负数时 出发作弊开奖流程
        if 0 > RoundManager().cur_award_pool_gold + diff_card_award_change[card_type]:
            # 奖池不够扣，重新随机
            temp = []
            for i in range(0, 4):
                if diff_card_award_change[i] < 0:
                    temp.append(0)
                else:
                    temp.append(1)

            card_type = weight_choice(temp)
            card_value = random.randint(1, 13)
        print "card_type=", card_type, "card_value=", card_value
        # 增加作测试能开出指定花色
        is_debug = GlobalObject().json_config.get("debug", 0)
        if is_debug and self.test_next_color:
            card_type = self.test_next_color.pop()
            if card_type == 4:
                card_value = random.randint(1, 2)
            logger.info("debug test next color is :{0}".format(card_type))
        # 测试功能完毕************
        show_card = CardManager().cal_card(card_type, card_value)
        logger.info("settle random card:{0}, {1}, {2}".format(show_card, card_type, card_value))

        self.record_round_info(diff_card_award_change[card_type], show_card)
        self.give_award_to_user(show_card)

        self.call_Later(1, self.update_remain_show_time)

    def record_round_info(self, pool_change, show_card):
        RoundManager().update_award_info(pool_change=pool_change, award_card=show_card)

    def give_award_to_user(self, card):
        """
        发放奖励
        """
        print u"进入推送流程"
        card_type, card_val = CardManager().get_type_and_val(card)
        print "cur_user_bet_info=", RoundManager().cur_user_bet_info
        card_list = CardManager().get_type_and_value(card)
        max_award_info = {"max_award": 0, "max_player_tel": None, "max_player_name": None}  # 用于存储或高得奖者信息
        for session_id in UserManager().get_classic_wx_session_list():
            user = UserManager().get_user_by_sessionid(session_id)
            if user:
                info = RoundManager().cur_user_bet_info.get(user.user_id, None)

                if info:
                    # 计算出每个用户当前的获奖结果
                    user_cur_award = AwardManager.calculate_away_info(info, card_type)
                    user.gold += user_cur_award
                    user.set_user_gold_for_settle(int(user.gold))
                else:
                    user_cur_award = 0
                    info = {}

                notice_content = {
                    "card": card_list,
                    "award": user_cur_award,
                    "bet_info": info,
                    "gold": user.gold,
                    "max_award_info": max_award_info}
                send_one(session_id, KEY_PUSH_AWARD_RESULT, notice_content)

    def update_remain_show_time(self):
        self.remain_show_time -= 1

        if self.remain_show_time > 0:
            self.call_Later(1, self.update_remain_show_time)
            notice_cotent = ''
            # send_all()
        else:
            self.call_Later(1, self.start_bet)

    def get_random_card(self):
        """
        返回   （花色，牌点数）
        """
        card_probabilitys = list(copy.deepcopy(Config().card_probability))
        cur_award_pool = RoundManager().cur_award_pool_gold

        # 普通牌中各花色占比
        common_card_weight_ratio = []
        # 黑红梅方（普通牌）总概率和
        common_probabilitys = card_probabilitys[0] + card_probabilitys[1] + card_probabilitys[2] + card_probabilitys[3]
        for i in range(0, 4):
            ratio = 1.0 * card_probabilitys[i] / common_probabilitys
            common_card_weight_ratio.append(ratio)

        if cur_award_pool > Config().add_base_min_gold:
            # 触发大小王概率增益
            if cur_award_pool < Config().add_base_max_gold:
                add_probability = 1.0 * (cur_award_pool - Config().add_base_min_gold) / Config().base_ratio \
                                  * Config().add_ratio
            else:
                add_probability = 1.0 * (Config().add_base_max_gold - Config().add_base_min_gold) / Config().base_ratio \
                                  * Config().add_ratio
            card_probabilitys[4] += add_probability
            for i in range(0, 4):
                card_probabilitys[i] -= add_probability * common_card_weight_ratio[i]
        elif cur_award_pool < Config().deduce_base_max_gold:
            # 触发大小王概率减益
            if cur_award_pool > Config().deduce_base_min_gold:
                deduce_probability = 1.0 * (cur_award_pool - Config().deduce_base_min_gold) / Config().base_ratio \
                                     * Config().deduce_ratio
            else:
                deduce_probability = 1.0 * (
                    Config().deduce_base_max_gold - Config().deduce_base_min_gold) / Config().base_ratio \
                                     * Config().deduce_ratio
            card_probabilitys[4] -= deduce_probability
            for i in range(0, 4):
                card_probabilitys[i] += deduce_probability * common_card_weight_ratio[i]
        # 将开奖概率装进单例中, 用于查询调用
        Config().card_probabilitys = card_probabilitys
        logger.info("random card probability : {0}".format(str(card_probabilitys)))

        random_card_type = weight_choice(card_probabilitys)
        if 4 == random_card_type:
            return random_card_type, random.randint(1, 2)
        else:
            return random_card_type, random.randint(1, 13)

    def get_remain_bet_time(self):
        """
        获取押注剩余时间
        :return:
        """
        return self.remain_bet_time

    def get_remain_show_time(self):
        """
        获取开奖展示剩余时间
        :return:
        """
        return self.remain_show_time

    def get_is_can_bet(self):
        """
        获取当前是否可以押注
        :return:
        """
        return self.is_can_bet

    @staticmethod
    def calculate_away_info(info, card_type):
        """
        根据每个人压住,计算开奖时的返回分数,包含开王时的特殊处理
        :param info: 个人押注信息
        :param card_type: 开奖花色
        :return: 个人中奖具体分数
        """
        bet_sum = 0  # 用于记录非王 压住总点数
        user_cur_award = info[CARD_DESC[card_type]] * Config().odds[card_type]
        if card_type == CARD_JOKER:
            bet_sum += info[CARD_DESC[0]]
            bet_sum += info[CARD_DESC[1]]
            bet_sum += info[CARD_DESC[2]]
            bet_sum += info[CARD_DESC[3]]
            user_cur_award += bet_sum
        return user_cur_award


AwardManager().start_bet()
