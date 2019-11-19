# coding=utf-8

"""
author: jamon
"""

import hashlib
import os
import re
import sys
import traceback
import time
import ujson
import uuid
from functools import wraps


MAX_EXCEED_TIME = 10


def contain_dangerous_char(s):
    """
    检查字符串中是否包括危险字符
    :param s: string
    :return: True/False
    """
    p = re.compile('[\&\<\>\"\'\/\(\)]')
    l = p.findall(str(s))
    if len(l) > 0:
        return True
    else:
        return False


def get_md5(content):
    """
    获取md5
    :param content: string
    :return: string
    """
    c_md5 = hashlib.md5()
    c_md5.update(content.encode("utf-8"))
    return c_md5.hexdigest()


def get_rand_16():
    """
    获取随机的16位字符串
    :return: string
    """
    return get_md5_16(uuid.uuid1().hex)


def get_md5_16(content):
    """
    获取16位的md5串
    :param content: string
    :return: string
    """
    return get_md5(content)[8:-8]


def record_spent_time(funcname):
    """
    每个handler请求时间的装饰器
    :param funcname:
    :return: function return
    """

    def record_spent(func):
        @wraps(func)
        def handler_func(*args, **kwargs):
            start_time = time.time()
            print("start " + str(funcname) + " time: " + str(start_time))

            res = func(*args, **kwargs)

            end_time = time.time()
            print("end " + str(funcname) + " time: " + str(end_time))

            spent_time = end_time - start_time
            if spent_time > MAX_EXCEED_TIME:
                print("handler " + str(funcname) + " spent time: " + str(spent_time) + ",exceed time!")
            else:
                print("handler " + str(funcname) + " spent time: " + str(spent_time) + ",ok.")
            return res

        return handler_func

    return record_spent


def rlock(lock):
    """
    每个handler请求时间的装饰器
    :param lock:
    :return: function return
    """

    def on_lock(func):
        @wraps(func)
        def handler_func(*args, **kwargs):
            lock.acquire()
            res = func(*args, **kwargs)
            lock.release()
            return res

        return handler_func

    return on_lock


def convert_to_json(data):
    """
    字符串转换为dict
    :param data: string or dict
    :return: dict
    """
    if isinstance(data, dict):
        return data

    if isinstance(data, str):
        return ujson.loads(data)

    return {}


def is_ip(ipstr):
    """
    判断字符串是否为IPv4地址
    :param ipstr: string
    :return: True/False
    """
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ipstr):
        return True
    else:
        return False


def is_ip_in_range(ip, range_list=[]):
    """
    判断ip是否在指定区间的ip段内
    :param ip:
    :param range_list: [[start_ip, end_ip], [], ...]
    :return: 0/1
    """
    ip2int = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
    compare_ip = ip2int(ip)
    for r in range_list:
        start_ip = ip2int(r[0])
        end_ip = ip2int(r[1])
        if compare_ip>=start_ip and compare_ip<=end_ip:
            return 1

    return 0


def safe_rm_dir(need_del_dir='aaaaaaaaaaaaaaaaaaa'):
    """
    安全删除目录(只能删除两级子目录下数据)，防误删
    :param need_del_dir:
    :return:
    """
    if 2 >= len(need_del_dir.strip('/').split('/')):
        print("rm_dir error!")
        return
    os.system("rm -rf {0}".format(need_del_dir))


def time_refresh(interval):
    """
    作用：每隔指定间隔执行某函数, 目前支持Python3
    使用场景：当需要间隔一定时间执行某函数，但又不希望过重的启动一个定时器来控制，如某些较少发生变化的配置信息，我们不希望
            每次使用时都重新从数据库或配置文件读取，但又希望能够周期性的刷新配置，此时便可用到该装饰器；
    :param interval: int, 执行间隔（s）
    :return: function return
    """
    last_refresh_time = 0

    def refresh(func):
        @wraps(func)
        def handler_func(*args, **kwargs):
            nonlocal last_refresh_time
            cur_time = time.time()
            if interval < cur_time-last_refresh_time:
                res = func(*args, **kwargs)
                last_refresh_time = cur_time
                return res
            else:
                return

        return handler_func

    return refresh

