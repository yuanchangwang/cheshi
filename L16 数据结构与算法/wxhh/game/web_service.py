# coding=utf8

from firefly.server.globalobject import webserviceHandle
from twisted.web import resource
from game.user_manager import UserManager
from game.award_manager import AwardManager
from game.game_config import Config, CARD_DESC
from game.user import MUser
from twisted.internet import defer, reactor
from models.model_game_config import GameConfig
from game.push_service import send_one, send_all
from share.message_id import KEY_PUSH_SYSTEM_NOTICE
import json


@webserviceHandle("get_cur_player")
class GetCurPlayer(resource.Resource):
    def render(self, request):
        players = UserManager().get_session_id_user_id_list()
        return json.dumps(players)


@webserviceHandle("get_cur_game_status")
class GetCurGameStatus(resource.Resource):
    def render(self, request):
        data = {
            "is_can_bet": AwardManager().is_can_bet
        }
        return json.dumps(data)


@webserviceHandle("update_user_gold")
class UpdateUserGold(resource.Resource):
    def render(self, request):
        print "UpdateUserGold!"
        data = {"code": 0}
        try:
            user_tel = request.args.get("tel", None)[0]
            if not user_tel:
                return "need user_tel!"
            gold = int(request.args.get("gold", 0)[0])
        except Exception, e:
            print e
            return "params error!"
        user = MUser.get_user_by_name(user_tel)
        print "Muser=", dir(user)
        if not user:
            data["desc"] = "not have this user!"
            return -1

        if not AwardManager().is_can_bet:
            user_gold = update_user_gold(user_tel, gold)
            data["code"] = 200
            data["desc"] = "pay Success!"
            return json.dumps(data)
        else:
            remain_time = AwardManager().remain_bet_time
            print "callLater after %s second !" % remain_time
            reactor.callLater(remain_time + 1, update_user_gold, user_tel=user_tel, gold=gold)
            data["code"] = 200
            data["desc"] = "current can't add gold ! wait %s second!" % remain_time
            return json.dumps(data)


@webserviceHandle("update_game_config")
class UpdateGameConfig(resource.Resource):
    def render(self, request):
        # 从数据库获取概率相关数据
        game_config = GameConfig.get_game_config_info()
        Config().add_base_max_gold = game_config["add_base_max_gold"]
        # self.card_probability = (2439, 4878, 7195, 9512, 10000)         # 各种花色开奖概率
        Config().card_probability = game_config["card_probability"]  # 各种花色开奖概率
        Config().consume_ratio = game_config["consume_ratio"]  # 抽成比例

        # 大小王概率调整规则
        Config().add_base_min_gold = game_config["add_base_min_gold"]  # 触发概率增益金币数额下限
        Config().add_base_max_gold = game_config["add_base_max_gold"]  # 触发概率增益金币数额上限
        Config().deduce_base_min_gold = game_config["deduce_base_min_gold"]  # 触发概率减益金币数额下限
        Config().deduce_base_max_gold = game_config["deduce_base_max_gold"]  # 触发概率减益金币数额上限
        Config().base_ratio = game_config["base_ratio"]  # 每多少数额金币变化触发增减益
        Config().add_ratio = game_config["add_ratio"]  # 每次增益概率幅度（万分比）
        Config().deduce_ratio = game_config["deduce_ratio"]  # 每次减益概率幅度（万分比）

        Config().max_bet_num = game_config["max_bet_num"]  # 最大投注
        Config().min_bet_num = game_config["min_bet_num"]  # 最小投注

        Config().record_card_num = game_config["record_card_num"]  # 最多显示多少局开奖花色详情

        Config().interval_one_round = game_config["interval_one_round"]  # 秒为单位记录广播间隔
        return "ok"


@webserviceHandle("get_game_config")
class GetGameConfig(resource.Resource):
    def render(self, request):
        return json.dumps(Config().game_config_to_dict())


@webserviceHandle("system_notice")
class SystemNotice(resource.Resource):
    def render(self, request):
        try:
            stop_time = int(request.args.get("time", None)[0])
            if not stop_time:
                return "need begin_time!"
            content = request.args.get("content", 0)[0]

            AwardManager().stop_time = stop_time
            AwardManager().stop_content = content
            send_all(UserManager().get_session_list(), KEY_PUSH_SYSTEM_NOTICE, self.stop_content)
            return "ok"
        except Exception, e:
            print e
            return "params error!"


@webserviceHandle("test_next_color")
class TestNextColor(resource.Resource):
    def render(self, request):
        data = {"code": 0}
        try:
            print request.args
            next_color = int(request.args.get("next_color", None)[0])
            if next_color not in CARD_DESC.keys():
                return "params only 0,1,2,3,4"
            AwardManager().test_next_color.append(next_color)
            data["code"] = 200
            data["desc"] = "Success!! test value put in list!!"
            data["test_next_color_list"]=AwardManager().test_next_color
            return json.dumps(data)
        except Exception, e:
            print e
            data["code"] = 0
            data["desc"] = "params error!!"
            data["test_next_color_list"] = []
            return json.dumps(data)



def update_user_gold(user_tel, gold):
    print "update_user_gold!!!"
    user = MUser.get_user_by_name(user_tel)
    MUser.update_user_gold(user.id, gold)
    user1 = UserManager().get_user_by_id(user.id)
    if user1:
        user1.gold += gold
    return user.gold