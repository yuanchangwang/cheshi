# coding=utf-8
__author__ = 'songchao'
import requests


def set_next_color(color, target=None):
    """
    :param target 目标服务器, 表示
    @params 是一个dict, 用于存放花色参数 next_color
    next_color 是下一个即将开出的花色, 范围 [0,1,2,3,4]
    """
    if target:
        url = 'http://47.52.58.220:30001/test_next_color'
    else:
        url = 'http://127.0.0.1:30001/test_next_color'

    params = {"next_color": color}
    r = requests.post(url, data=params)
    print r.text


def add_gold_for_user(user, gold=0):
    """
    用于通知服务器上分
    :param user: 目标用户, 实际为用户的电话号码即用户名
    :param gold: 充值金币数量
    :return:
    """
    url = 'http://47.52.58.220:30001/update_user_gold'
    params = {"tel": user, "gold": gold}
    r = requests.post(url, params)
    print r.text
    return r.text

def get_cur_player():

    url = 'http://47.52.58.220:30001/get_cur_player'
    r = requests.get(url)
    print r.text

# 向外网测试服 推送开王指令
# set_next_color(4, target=1)

# 测试给陈登顺增加金币
# add_gold_for_user("18869405100", 5000000)
# 测试用户1212 增加金币
# add_gold_for_user("1212", 50000)
# 获取当前用户

