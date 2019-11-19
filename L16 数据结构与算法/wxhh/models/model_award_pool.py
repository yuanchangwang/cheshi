#coding:utf-8


from sqlalchemy import Column,func,not_
from sqlalchemy.types import CHAR, Integer, VARCHAR, DATETIME, SMALLINT, BIGINT
from models.base import Base
from models.session import sessionCM
import datetime
import copy
import json
from share.common_tool import get_md5

class MAwardPool(Base):
    __tablename__ = 'ibb_awardpool'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    cur_award_pool = Column(BIGINT, default=0)
    all_consume_gold = Column(BIGINT, default=0)
    cur_round_id = Column(Integer)

    def to_dict(self):
        return {"cur_round_id": self.cur_round_id, "cur_award_pool":self.cur_award_pool,
                "all_consume_gold":self.all_consume_gold}

    @classmethod
    def get_award_info(cls):
        with sessionCM() as session:
            ret = session.query(MAwardPool).first()
            if ret:
                return ret.to_dict()
            return {}

    @classmethod
    def update_award_info(cls, award_pool_change, consume_gold_change, cur_round_id):
        """

        """
        with sessionCM() as session:
            ret = session.query(MAwardPool).first()
            if ret:
                ret.cur_award_pool += award_pool_change
                ret.all_consume_gold += consume_gold_change
                ret.cur_round_id = cur_round_id
                session.commit()
                return 1, ret.to_dict

            return 0, {}

    



