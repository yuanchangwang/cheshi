#coding:utf-8


from sqlalchemy import Column,func
from sqlalchemy.types import CHAR, Integer, VARCHAR, DATETIME, SMALLINT, BIGINT
from models.base import Base
from models.session import sessionCM
import datetime
import copy
import json
from share.common_tool import get_md5

class MUser(Base):
    __tablename__ = 'ibb_user'

    id = Column(Integer, autoincrement=True, nullable=False, unique=True, primary_key=True)
    name = Column(VARCHAR(255),index=True) # or Column(String(30))
    nick_name = Column(VARCHAR(255), index=True)
    passwd = Column(CHAR(32))
    phone = Column(VARCHAR(20), index=True, default="")
    device_id = Column(VARCHAR(50))
    gold = Column(BIGINT)

    def __init__(self, passwd, name, nickname, device_id='',phone='', introduction=''):
        self.name = name
        self.nickname = nickname
        self.passwd = passwd
        self.phone = phone
        self.device_id = device_id
        self.gold = 0
        self.introduction = introduction

    def to_dict(self):
        return {"id": self.id, "name": self.name, "nick_name": self.nick_name,
                "gold": self.gold, "phone": self.phone}

    @classmethod
    def create(cls, passwd, name, nickname, device_id='',phone='', introduction=''):
        with sessionCM() as session:
            user = session.query(MUser).filter_by(name=name).first()
            if user:
                return 0
            new_user = cls(passwd, name, nickname, device_id, phone, introduction=introduction)
            session.add(new_user)
            session.commit()
            return new_user.id

    @classmethod
    def get_user_info_by_id(cls, user_id):
        with sessionCM() as session:
            user = session.query(MUser).filter_by(id=user_id).first()
            if user:
                return 1, user.to_dict()
            else:
                return 0, {}

    @classmethod
    def validate_passwd(cls, user_name, passwd):
        if not user_name or not passwd:
            return 0, {}
        with sessionCM() as session:
            user = session.query(MUser).filter_by(name=user_name).first()
            if user and user.passwd==passwd:
                return 1, user.to_dict()
            else:
                return 0, {}

    @classmethod
    def get_user_by_name(cls, user_name):
        with sessionCM() as session:
            user = session.query(MUser).filter_by(name=user_name).first()
            return user

    @classmethod
    def del_user(cls, user_id):
        """
        删除用户，慎用!!!!!!!!!!!!!!!
        :param accid:
        :return:
        """
        with sessionCM() as session:
            session.query(MUser).filter_by(id=user_id).delete()
            session.commit()
            return 0

    @classmethod
    def update_user_gold(cls, user_id, gold_change):
        with sessionCM() as session:
            user = session.query(MUser).filter_by(id=user_id).first()
            if user:
                user.gold += gold_change
                session.commit()
                return 1, {"gold":user.gold}
            return 0, {}
    
    @classmethod
    def set_user_gold(cls, user_id, user_gold):
        with sessionCM() as session:
            user = session.query(MUser).filter_by(id=user_id).first()
            if user:
                user.gold = user_gold
                session.commit()
                return 1, {"gold":user.gold}
            return 0, {}


