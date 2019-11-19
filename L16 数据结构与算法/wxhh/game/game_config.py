# coding=utf-8

from firefly.utils.singleton import Singleton

CARD_SPADE = 0  # 黑桃
CARD_HEART = 1  # 红桃
CARD_CLUB = 2  # 梅花
CARD_DIAMOND = 3  # 方块
CARD_JOKER = 4  # 大小王

CARD_DESC = {CARD_SPADE: "spade", CARD_HEART: "heart", CARD_CLUB: "club", CARD_DIAMOND: "diamond", CARD_JOKER: "joker"}
CARD_DESC_REVERSE = {"spade": CARD_SPADE,  "heart": CARD_HEART, "club": CARD_CLUB, "diamond": CARD_DIAMOND, "joker":CARD_JOKER}

PAGE_MAX_RECORD_NUM = 52  # 一页记录中最多存放的游戏记录数


class Config(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.award_pool_gold = 0
        self.total_consume_gold = 0

        self.max_bet_time = 20
        self.max_show_time = 10

        self.odds = [3.8, 3.8, 4, 4, 20]

        self.cards = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,  # 黑桃1-K
            17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,  # 红桃1-K
            33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,  # 梅花1-K
            49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61,  # 方块1-K
            65, 66  # 大小王
        ]

        # self.card_probability = (2439, 4878, 7195, 9512, 10000)         # 各种花色开奖概率
        self.card_probability = [2439, 2439, 2317, 2317, 488]  # 各种花色开奖概率
        # self.card_probability = [9996, 1, 1, 1, 1]  # 各种花色开奖概率
        self.consume_ratio = 0.02  # 抽成比例

        # 大小王概率调整规则
        self.add_base_min_gold = 11000000  # 触发概率增益金币数额下限
        self.add_base_max_gold = 21000000  # 触发概率增益金币数额上限
        self.deduce_base_min_gold = 5000000  # 触发概率减益金币数额下限
        self.deduce_base_max_gold = 10000000  # 触发概率减益金币数额上限
        self.base_ratio = 100000  # 每多少数额金币变化触发增减益
        self.add_ratio = 5  # 每次增益概率幅度（万分比）
        self.deduce_ratio = 5  # 每次减益概率幅度（万分比）

        self.max_bet_num = 100000  # 最大投注
        self.min_bet_num = 100  # 最小投注

        self.record_card_num = 100  # 最多显示多少局开奖花色详情

        self.interval_one_round = 1  # 秒为单位记录广播间隔
        self.card_probabilitys = None  # 永存当前游戏开奖比例, 用于web 接口查询

    def game_config_to_dict(self):
        ret = {
            "award_pool_gold ": self.award_pool_gold,
            "total_consume_gold ": self.total_consume_gold,
            "max_bet_time ": self.max_bet_num,
            "max_show_time ": self.max_show_time,
            "odds ": self.odds,
            "cards ": self.cards,
            "card_probability ": self.card_probability,
            # "card_probability ":[9996, 1, 1, 1, 1]  # 各种花色开奖概率
            "consume_ratio ": self.consume_ratio,
            # 大小王概率调整规则
            "add_base_min_gold ": self.add_base_min_gold,  # 触发概率增益金币数额下限
            "add_base_max_gold ": self.add_base_max_gold,  # 触发概率增益金币数额上限
            "deduce_base_min_gold ": self.deduce_base_min_gold,  # 触发概率减益金币数额下限
            "deduce_base_max_gold ": self.deduce_base_max_gold,  # 触发概率减益金币数额上限
            "base_ratio ": self.base_ratio,  # 每多少数额金币变化触发增减益
            "add_ratio ": self.add_ratio,  # 每次增益概率幅度（万分比）
            "deduce_ratio ": self.deduce_ratio,  # 每次减益概率幅度（万分比）
            "max_bet_num ": self.max_bet_num,  # 最大投注
            "min_bet_num ": self.min_bet_num,  # 最小投注
            "record_card_num ": self.record_card_num,  # 最多显示多少局开奖花色详情
            "interval_one_round ": self.interval_one_round,  # 秒为单位记录广播间隔
            "card_probabilitys":self.card_probabilitys  # 当前开奖概率
        }

        return ret
