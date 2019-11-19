#coding:utf-8


from sqlalchemy import Column,func,not_
from sqlalchemy.types import CHAR, Integer, VARCHAR, DATETIME, SMALLINT, BIGINT, FLOAT
from models.base import Base
from models.session import sessionCM
import datetime
import copy
import json
from share.common_tool import get_md5

class GameConfig(Base):
    __tablename__ = 'ibb_game_config'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)

    consume_ratio = Column(FLOAT, default=0.02)  # 抽成比例
    # 大小王概率调整规则
    add_base_min_gold = Column(BIGINT, default=11000000, doc=u"触发概率增益金币数额下限")  # 触发概率增益金币数额下限
    add_base_max_gold = Column(BIGINT, default=21000000, doc=u"触发概率增益金币数额上限")  # 触发概率增益金币数额上限
    deduce_base_min_gold = Column(BIGINT, default=5000000, doc=u"触发概率减益金币数额下限")  # 触发概率减益金币数额下限
    deduce_base_max_gold = Column(BIGINT, default=10000000, doc=u"触发概率减益金币数额上限")  # 触发概率减益金币数额上限
    base_ratio = Column(BIGINT, default=100000, doc=u"每多少数额金币变化触发增减益")  # 每多少数额金币变化触发增减益
    add_ratio = Column(BIGINT, default=5, doc=u"每次增益概率幅度（万分比）")  # 每次增益概率幅度（万分比）
    deduce_ratio = Column(BIGINT, default=5, doc=u"每次减益概率幅度（万分比）")  # 每次减益概率幅度（万分比）
    max_bet_num = Column(BIGINT, default=1000000, doc=u"最大投注")  # 最大投注
    min_bet_num = Column(BIGINT, default=100, doc=u'# 最小投注')  # 最小投注
    record_card_num = Column(BIGINT, default=100, doc=u'最多显示多少局开奖花色详情')  # 最多显示多少局开奖花色详情
    interval_one_round = Column(BIGINT, default=1, doc=u'秒为单位记录广播间隔')  # 秒为单位记录广播间隔
    card_spade = Column(BIGINT, default=2439, doc=u'黑桃')  # 黑桃
    card_heart = Column(BIGINT, default=2439, doc=u'红桃')  # 红桃
    card_club = Column(BIGINT, default=2317, doc=u'梅花')  # 梅花
    card_diamond = Column(BIGINT, default=2317, doc=u'方块')  # 方块
    card_joker = Column(BIGINT, default=488, doc=u'大小王')  # 大小王
    game_type = Column(Integer, doc=u"游戏类型")  # 标注具体游戏

    card_probability = [2439, 2439, 2317, 2317, 488]  # 各种花色开奖概率

    def to_dict(self):
        return {"consume_ratio": self.consume_ratio,
                "add_base_min_gold":self.add_base_min_gold,
                "add_base_max_gold":self.add_base_max_gold,
                "deduce_base_min_gold":self.deduce_base_min_gold,
                "deduce_base_max_gold":self.deduce_base_max_gold,
                "base_ratio":self.base_ratio,
                "add_ratio":self.add_ratio,
                "deduce_ratio":self.deduce_ratio,
                "max_bet_num":self.max_bet_num,
                "min_bet_num":self.min_bet_num,
                "record_card_num":self.record_card_num,
                "interval_one_round":self.interval_one_round,
                "card_probability": [self.card_spade, self.card_heart, self.card_club, self.card_diamond, self.card_joker],
                "game_type":self.game_type}

    @classmethod
    def get_card_probability(cls):
        with sessionCM() as session:
            ret = session.query(GameConfig).first()
            if ret:
                return [ret.card_spade, ret.card_heart, ret.card_club, ret.card_diamond, ret.card_joker]
            return []

    @classmethod
    def get_game_config_info(cls):
        with sessionCM() as session:
            ret = session.query(GameConfig).first()
            if ret:
                return ret.to_dict()
            return {}




