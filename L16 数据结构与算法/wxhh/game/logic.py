# coding=utf-8

"""
"""

import math

from game.award_manager import AwardManager
from game.game_config import Config, CARD_SPADE, CARD_HEART, CARD_CLUB, CARD_DIAMOND, CARD_JOKER, PAGE_MAX_RECORD_NUM, CARD_DESC
from game.round_manager import RoundManager
from game.user_manager import UserManager
from models.model_user import MUser
from share.ibbgame_log import logger
from share.msg_desc import NEED_MORE_GOLD


def login(session_id, user_name, passwd):
    ret, info = MUser.validate_passwd(user_name, passwd)
    logger.info("login result: {0}, {1}".format(ret, str(info)))
    # 添加经典五星人数
    info["classic_wx_player_count"] = len(UserManager().get_classic_wx_session_list())
    info["big_away_wx_player_count"] = len(UserManager().get_classic_wx_session_list())
    info["mosaic_gold_wx_player_count"] = len(UserManager().get_classic_wx_session_list())
    if ret:
        UserManager().add_user(info.get("id"), session_id)
    return ret, info


def get_rooms_people():
    ret = {
        "classic_wx_player_count": len(UserManager().get_classic_wx_session_list()),
        "big_away_wx_player_count": len(UserManager().get_classic_wx_session_list()),
        "mosaic_gold_wx_player_count": len(UserManager().get_classic_wx_session_list())
    }
    return ret


def register(session_id, user_name, passwd, nick_name):
    ret = MUser.create(passwd, user_name, nick_name)
    logger.info("register result:{0}".format(ret))
    if ret:
        return 1, {"user_id": ret}
    else:
        return 0, {"desc": "username or password error"}


def enter(session_id):
    """
    进入经典五星
    :param session_id: 用户会话ID ("proxy,1")
    :return:
    """
    user = UserManager().get_user_by_sessionid(session_id)

    if user is None:
        return 0, {"info": "user is none"}
    user_id = UserManager().get_user_by_sessionid(session_id).user_id
    UserManager().add_session_to_classic_wx(session_id)  # 将用户会话加入经典五星会话列表便于全局推送
    cur_round_bet_info = {
        "own_bet": RoundManager().cur_user_bet_info.get(user_id, {}),
        "bet_static": [RoundManager().cur_round_spade_num, RoundManager().cur_round_heart_num,
                       RoundManager().cur_round_club_num, RoundManager().cur_round_diamond_num,
                       RoundManager().cur_round_joker_num]
    }
    return 1, {"max_bet_num": Config().max_bet_num,
               "min_bet_num": Config().min_bet_num,
               "max_bet_time": Config().max_bet_time,
               "max_show_time": Config().max_show_time,
               "last_records": RoundManager().get_last_n_round_card_type(),
               "gold": user.gold,
               "bet_info": cur_round_bet_info,
               "remain_bet_time": AwardManager().get_remain_bet_time(),
               "remain_show_time": AwardManager().get_remain_show_time(),
               "is_can_bet": AwardManager().get_is_can_bet()
               }


def exit(session_id):
    UserManager().offline_user(session_id)  # 当前玩家退出和掉线时处理逻辑相同
    UserManager().exit_classic_wx_session_list(session_id)  # 当前玩家退出和掉线时处理逻辑相同
    return 1, {}


def exit_classic_wx(session_id):
    UserManager().exit_classic_wx_session_list(session_id)  # 当前玩家退出和掉线时处理逻辑相同
    return 1, {}


def bet(session_id, bet_num, bet_card_type):
    cur_user = UserManager().get_user_by_sessionid(session_id)
    cur_gold = cur_user.gold
    info = RoundManager().cur_user_bet_info.get(cur_user.user_id, None)
    if info is None:
        info = {"spade": 0, "heart": 0,
                "club": 0, "diamond": 0,
                "joker": 0, "gold": cur_gold}

    if not cur_user:
        info["desc"] = "user not exist!"
        return 0, info

    if bet_card_type not in [CARD_SPADE, CARD_HEART, CARD_CLUB, CARD_DIAMOND, CARD_JOKER]:
        info["desc"] = "invalid bet card type!"
        return 0, info

    total_bet_num = info.get(CARD_DESC[bet_card_type]) + bet_num

    if total_bet_num < Config().min_bet_num or total_bet_num > Config().max_bet_num:
        info["desc"] = "invalid bet num!"
        info["gold"] = cur_gold
        return 0, info


    if cur_user.gold < bet_num:
        info["desc"] = NEED_MORE_GOLD
        return 0, info
    # 押注时先更改内存中的金币数量, 在结算的时候写入数据库
    cur_user.gold -= bet_num
    # 押注时更改数据金币数量 TODO 此时需要将金币梳理储存在内存,在结算时统一更改
    # cur_gold = cur_user.set_user_gold(-1 * bet_num)
    bet_spade = 0
    bet_heart = 0
    bet_club = 0
    bet_diamond = 0
    bet_joker = 0
    if CARD_SPADE == bet_card_type:
        bet_spade += bet_num
    elif CARD_HEART == bet_card_type:
        bet_heart += bet_num
    elif CARD_CLUB == bet_card_type:
        bet_club += bet_num
    elif CARD_DIAMOND == bet_card_type:
        bet_diamond += bet_num
    else:
        bet_joker += bet_num

    RoundManager().update_bet_info(cur_user.user_id, spade_change=bet_spade, heart_change=bet_heart,
                                   club_change=bet_club, diamond_change=bet_diamond, joker_change=bet_joker)
    # 获取当局用户押注信息
    player_bet_info = {"spade": RoundManager().cur_user_bet_info[cur_user.user_id]["spade"],
                       "heart": RoundManager().cur_user_bet_info[cur_user.user_id]["heart"],
                       "club": RoundManager().cur_user_bet_info[cur_user.user_id]["club"],
                       "diamond": RoundManager().cur_user_bet_info[cur_user.user_id]["diamond"],
                       "joker": RoundManager().cur_user_bet_info[cur_user.user_id]["joker"]}
    return 1, {"spade": RoundManager().cur_round_spade_num, "heart": RoundManager().cur_round_heart_num,
               "club": RoundManager().cur_round_club_num, "diamond": RoundManager().cur_round_diamond_num,
               "joker": RoundManager().cur_round_joker_num, "gold": cur_user.gold, "player_bet_info": player_bet_info}


def bet_batch(session_id, bet_list):
    """
    用户批量下注, 可用于徐亚
    :param session_id:
    :param bet_list: [0,0,0,0,0] 用户下注数量, [黑桃,红桃,梅花,方片,砖石] [CARD_SPADE, CARD_HEART, CARD_CLUB, CARD_DIAMOND, CARD_JOKER]
    :return:
    """
    if not len(bet_list) == 5:
        return 0, {"desc": "invalid bet card type!"}
    for card_type, bet_num in enumerate(bet_list):
        ret, info = bet(session_id, bet_num, card_type)
    if 0 == ret:
        return 0, {"desc": "invalid bet num!"}
    cur_user = UserManager().get_user_by_sessionid(session_id)
    if not cur_user:
        return 0, {"desc": "user not exist!"}
    # 获取当局用户押注信息
    player_bet_info = {"spade": RoundManager().cur_user_bet_info[cur_user.user_id]["spade"],
                       "heart": RoundManager().cur_user_bet_info[cur_user.user_id]["heart"],
                       "club": RoundManager().cur_user_bet_info[cur_user.user_id]["club"],
                       "diamond": RoundManager().cur_user_bet_info[cur_user.user_id]["diamond"],
                       "joker": RoundManager().cur_user_bet_info[cur_user.user_id]["joker"]}

    return 1, {"spade": RoundManager().cur_round_spade_num, "heart": RoundManager().cur_round_heart_num,
               "club": RoundManager().cur_round_club_num, "diamond": RoundManager().cur_round_diamond_num,
               "joker": RoundManager().cur_round_joker_num, "gold": cur_user.gold, "player_bet_info": player_bet_info}


def cancel_bet(session_id):
    cur_user = UserManager().get_user_by_sessionid(session_id)
    # 获取用户当前押注数量
    bet_spade = RoundManager().cur_user_bet_info[cur_user.user_id]["spade"]
    bet_heart = RoundManager().cur_user_bet_info[cur_user.user_id]["heart"]
    bet_club = RoundManager().cur_user_bet_info[cur_user.user_id]["club"]
    bet_diamond = RoundManager().cur_user_bet_info[cur_user.user_id]["diamond"]
    bet_joker = RoundManager().cur_user_bet_info[cur_user.user_id]["joker"]
    cur_user.gold += (bet_spade+bet_heart+bet_club+bet_diamond+bet_joker)
    # 更改全局押注总数
    RoundManager().update_bet_info(cur_user.user_id, spade_change=-bet_spade, heart_change=-bet_heart,
                                   club_change=-bet_club, diamond_change=-bet_diamond, joker_change=-bet_joker)
    # 归零个人押注记录
    RoundManager().cur_user_bet_info[cur_user.user_id]["spade"] = 0
    RoundManager().cur_user_bet_info[cur_user.user_id]["heart"] = 0
    RoundManager().cur_user_bet_info[cur_user.user_id]["club"] = 0
    RoundManager().cur_user_bet_info[cur_user.user_id]["diamond"] = 0
    RoundManager().cur_user_bet_info[cur_user.user_id]["joker"] = 0
    # 获取当局用户押注信息
    player_bet_info = {"spade": RoundManager().cur_user_bet_info[cur_user.user_id]["spade"],
                       "heart": RoundManager().cur_user_bet_info[cur_user.user_id]["heart"],
                       "club": RoundManager().cur_user_bet_info[cur_user.user_id]["club"],
                       "diamond": RoundManager().cur_user_bet_info[cur_user.user_id]["diamond"],
                       "joker": RoundManager().cur_user_bet_info[cur_user.user_id]["joker"]}
    return 1,  {"spade": RoundManager().cur_round_spade_num, "heart": RoundManager().cur_round_heart_num,
               "club": RoundManager().cur_round_club_num, "diamond": RoundManager().cur_round_diamond_num,
               "joker": RoundManager().cur_round_joker_num, "gold": cur_user.gold, "player_bet_info": player_bet_info}



def get_record(page_num=1):
    '''
    获取指定页数的游戏记录
    :param page_num:
    :return:
    '''
    record_num = len(RoundManager().last_n_round_card_type)
    page_total = math.ceil(record_num / PAGE_MAX_RECORD_NUM)
    if page_num > page_total:
        return 1, []

    index = (page_total - page_num) * PAGE_MAX_RECORD_NUM
    return 1, RoundManager().last_n_round_card_type[index:index + PAGE_MAX_RECORD_NUM]


def get_cur_game_status():
    """
    获取游戏当前状态, 确定是否可以下注,(只有在不能下注时,才可以进行金币充值)
    :return:
    """
    r = {
        "is_can_bet": AwardManager().is_can_bet
    }
    return r


def update_user_gold(user_name, gold):
    """
    此方法用于充值
    :param user_name:  用户账号
    :param gold:  充值金币数量
    :return:
    """
    user = MUser.get_user_by_name(user_name)
    user.set_user_gold(gold)
