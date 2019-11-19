#coding:utf-8


from sqlalchemy import Column, func, not_, desc, asc, extract, and_
from sqlalchemy.types import CHAR, Integer, VARCHAR, DATETIME, SMALLINT, BIGINT
from models.base import Base
from models.session import sessionCM
import datetime
import copy
import json
from share.common_tool import get_md5, get_date_time
from share.ibbgame_log import logger

class MRoundRecord(Base):
    __tablename__ = 'ibb_roundrecord'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    cur_award_pool = Column(BIGINT, default=0)
    consume_gold = Column(BIGINT, default=0)
    spade_bet_num = Column(Integer, default=0)
    heart_bet_num = Column(Integer, default=0)
    club_bet_num = Column(Integer, default=0)
    diamond_bet_num = Column(Integer, default=0)
    joker_bet_num = Column(Integer, default=0)
    award_card = Column(Integer)

    def __init__(self, cur_award_pool, consume_gold, spade_bet_num, heart_bet_num, club_bet_num, diamond_bet_num,
                 joker_bet_num, award_card):
        # self.id = mid
        self.cur_award_pool = cur_award_pool
        self.consume_gold = consume_gold
        self.spade_bet_num = spade_bet_num
        self.heart_bet_num = heart_bet_num
        self.club_bet_num = club_bet_num
        self.diamond_bet_num = diamond_bet_num
        self.joker_bet_num = joker_bet_num
        self.award_card = award_card

    @classmethod
    def create(cls, cur_award_pool, consume_gold, spade_bet_num, heart_bet_num, club_bet_num, diamond_bet_num,
               joker_bet_num, award_card):
        new_record = cls(cur_award_pool, consume_gold, spade_bet_num, heart_bet_num, club_bet_num, diamond_bet_num,
                         joker_bet_num, award_card)
        with sessionCM() as session:
            session.add(new_record)
            session.commit()
            return new_record.id

    def to_dict(self):
        return {"id": self.id,"cur_award_pool": self.cur_award_pool, "consume_gold": self.consume_gold,
                "spade_bet_num": self.spade_bet_num, "heart_bet_num": self.heart_bet_num,
                "club_bet_num": self.club_bet_num, "diamond_bet_num": self.diamond_bet_num,
                "joker_bet_num": self.joker_bet_num, "award_card": self.award_card,
                "created_date": self.created_date, "modified_date": self.modified_date}

    @classmethod
    def get_round_record(cls, num=50):
        with sessionCM() as session:
            ret = session.query(MRoundRecord).order_by(desc(MRoundRecord.created_date)).limit(num).all()
            if ret:
                return [{"award_card":r.award_card, "modified_date":r.modified_date} for r in ret]
            return []

    @classmethod
    def get_max_round_id(cls):
        with sessionCM() as session:
            ret = session.query(MRoundRecord).order_by(desc(MRoundRecord.created_date)).limit(1).first()
            if ret:
                return ret.id
            return -1

    @classmethod
    def update_award_info(cls, award_pool_change, consume_gold_change):
        """

        """
        with sessionCM() as session:
            ret = session.query(MRoundRecord).first()
            if ret:
                ret.cur_award_pool += award_pool_change
                ret.all_consume_gold += consume_gold_change
                session.commit()
                return 1, ret.to_dict

            return 0, {}

    @classmethod
    def get_round_static(cls, passed_day=0):
        '''
        获取指定日期的统计数据
        :param passed_day: 过去第几天的数据，0表示当天
        :return:
        '''
        with sessionCM() as session:
            start_day = get_date_time(passed_day=passed_day)
            end_day = get_date_time(passed_day=passed_day-1)
            # ret = session.query(MRoundRecord).order_by(desc(MRoundRecord.created_date)).limit(1000).all()
            ret = session.query(MRoundRecord).order_by(asc(MRoundRecord.created_date)) \
                .filter(and_(MRoundRecord.created_date>=start_day, MRoundRecord.created_date<end_day)).all()
            static = {
                "spade": 0, "heart": 0, "club":0, "diamond":0, "joker":0, "total": 0
            }

            card_info = []
            if ret:
                for r in ret:
                    # print u"t=", r, r.award_card
                    card_type = r.award_card >> 4
                    card_info.append(r.award_card)
                    if 0 == card_type:
                        static["spade"] += 1
                    elif 1 == card_type:
                        static["heart"] += 1
                    elif 2 == card_type:
                        static["club"] += 1
                    elif 3 == card_type:
                        static["diamond"] += 1
                    elif 4 == card_type:
                        static["joker"] += 1
                    else:
                        logger.error("get_round_static error!({0})".format(str(r.to_dict)))
                        return {}, []
                    static["total"] += 1
            print u"get_round_static", static
            return static, card_info




