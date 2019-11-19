# coding=utf-8
"""
author = jamon
"""

import tornado.ioloop
import tornado.web


class LoginHandler(tornado.web.RequestHandler):

    def post(self):
        sip = self.request.remote_ip
        content = self.request.body
        self.write("login success")


class TornadoServer(object):

    def __init__(self):
        # self.host = "localhost"
        self.port = 8888
        self.app = tornado.web.Application(
            [("/login", LoginHandler),],
        )

    def run(self):
        self.app.listen(self.port)
        tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    server_ins = TornadoServer()
    server_ins.run()