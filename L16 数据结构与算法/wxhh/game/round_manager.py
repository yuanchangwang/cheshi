# coding=utf-8

"""

"""

from firefly.utils.singleton import Singleton

from game.card_manager import CardManager
from game_config import Config
from models.model_award_pool import MAwardPool
from models.model_round_record import MRoundRecord
from share.ibbgame_log import logger


class RoundManager(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.cur_award_pool_gold = 0    #当前系统奖池
        self.cur_round_id = 0

        # 最近n局开奖花色统计
        self.cur_award_card_static = {
            "spade": 0, "heart": 0, "club": 0, "diamond": 0, "joker": 0, "total": 0
        }
        # 最近n局开奖结果
        self.last_n_round_card_type = []

        self.init_from_db()

        self.cur_round_spade_num = 0  # 当局黑桃投注总额
        self.cur_round_heart_num = 0  # 当前红桃投注总额
        self.cur_round_club_num = 0  # 当前梅花投注总额
        self.cur_round_diamond_num = 0 # 当前方片投注总额
        self.cur_round_joker_num = 0 # 当前皇冠投注总额
        self.cur_round_total = 0  # 当局投注总额
        self.cur_award_card = -1  # 当局开奖卡牌

        self.cur_round_consume_gold = 0  # 当局系统消耗金币

        self.cur_user_bet_info = {}  # 当局玩家投注信息

    def init_from_db(self):
        round_info = MAwardPool().get_award_info()
        print u"aaaaaaaaaaaa:", round_info
        self.cur_award_pool_gold = round_info.get("cur_award_pool", 0)
        self.cur_round_id = round_info.get("cur_round_id", 0)

        static, cardInfo = MRoundRecord.get_round_static()
        self.last_n_round_card_type = cardInfo
        self.cur_award_card_static.update(static)
        print u"cur_award_card_static:", self.cur_award_card_static

    def new_round(self):
        self.cur_round_id += 1

        self.cur_round_spade_num = 0
        self.cur_round_heart_num = 0
        self.cur_round_club_num = 0
        self.cur_round_diamond_num = 0
        self.cur_round_joker_num = 0
        self.cur_round_total = 0
        self.cur_round_consume_gold = 0

        self.cur_award_card = -1
        self.cur_user_bet_info = {}

    def update_bet_info(self, user_id, spade_change=0, heart_change=0, club_change=0, diamond_change=0, joker_change=0):
        """
        更新当局玩家投注统计信息
        """
        self.cur_round_spade_num += spade_change
        self.cur_round_heart_num += heart_change
        self.cur_round_club_num += club_change
        self.cur_round_diamond_num += diamond_change
        self.cur_round_joker_num += joker_change

        total_change = spade_change + heart_change + club_change + diamond_change + joker_change
        self.cur_round_total += total_change
        self.cur_round_consume_gold += total_change * Config().consume_ratio
        print "update_bet_info total=", self.cur_round_total
        if user_id in self.cur_user_bet_info.keys():
            self.cur_user_bet_info[user_id]["spade"] += spade_change
            self.cur_user_bet_info[user_id]["heart"] += heart_change
            self.cur_user_bet_info[user_id]["club"] += club_change
            self.cur_user_bet_info[user_id]["diamond"] += diamond_change
            self.cur_user_bet_info[user_id]["joker"] += joker_change
        else:
            self.cur_user_bet_info[user_id] = {
                "spade": spade_change, "heart": heart_change, "club": club_change,
                "diamond": diamond_change, "joker": joker_change
            }

    def update_award_info(self, pool_change, award_card):
        """
        结算后更新奖池及相关统计
        """
        self.cur_award_pool_gold += pool_change
        self.cur_award_card = award_card
        card_type, card_value = CardManager().get_type_and_val(award_card)
        if 0 == card_type:
            self.cur_award_card_static["spade"] += 1
        elif 1 == card_type:
            self.cur_award_card_static["heart"] += 1
        elif 2 == card_type:
            self.cur_award_card_static["club"] += 1
        elif 3 == card_type:
            self.cur_award_card_static["diamond"] += 1
        elif 4 == card_type:
            self.cur_award_card_static["joker"] += 1
        else:
            logger.error("update_award_info error!({0})".format(award_card))
            return {}
        self.cur_award_card_static["total"] += 1

        # 记录开奖花色详情
        # if Config().record_card_num <= len(self.last_n_round_card_type):
        #     self.last_n_round_card_type.pop(0)
        # 将开奖结果追加到内存记录中
        self.last_n_round_card_type.append(award_card)

        self.flush_record_to_db(pool_change)

    def flush_record_to_db(self, pool_change):
        MAwardPool.update_award_info(pool_change, self.cur_round_consume_gold, self.cur_round_id)
        ret = MRoundRecord.create(cur_award_pool=self.cur_award_pool_gold,
                                  consume_gold=self.cur_round_consume_gold, spade_bet_num=self.cur_round_spade_num,
                                  heart_bet_num=self.cur_round_heart_num, club_bet_num=self.cur_round_club_num,
                                  diamond_bet_num=self.cur_round_diamond_num, joker_bet_num=self.cur_round_joker_num,
                                  award_card=self.cur_award_card)
        logger.info("flush_record_to_db(result={0}): {1}, {2}".format(ret, self.cur_round_id, self.cur_award_card))


    def get_last_n_round_card_type(self):
        ret = []
        last_round_card = len(self.last_n_round_card_type)
        print self.last_n_round_card_type
        print "last_round_card=", last_round_card
        cur_page_show_card = self.last_n_round_card_type[-(last_round_card % 52):]
        print "cur_page_show_card= ",cur_page_show_card
        for i in cur_page_show_card:
            ret.append(CardManager().get_type_and_value(i))
        return ret