# coding=utf-8
"""
author = jamon
"""

import json
import requests


def request_tornado():
    url = "http://localhost:8888/login"
    ret = requests.post(url, data=json.dumps({"token": "19778225bc81894d8a6465c93542c0",
                                               "phone": "13612345678", "content": "test"
                                               }))
    print("test_login:", ret.status_code, ret.text)


def request_flask():
    url = "http://localhost:8888/flask/login"
    ret = requests.post(url, data={"token": "19778225bc81894d8a6465c93542c0",
                                               "phone": "13612345678", "content": "test"
                                               })
    print("test_login:", ret.status_code, ret.text)


def request_sanic():
    url = "http://localhost:8888/sanic/login"
    ret = requests.post(url, data={"token": "19778225bc81894d8a6465c93542c0",
                                               "phone": "13612345678", "content": "test"
                                               })
    print("test_login:", ret.status_code, ret.text)


if __name__ == "__main__":
    request_tornado()
    # request_flask()
    # request_sanic()
