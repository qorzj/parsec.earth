# -*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

import os

import leancloud
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from web.httpserver import StaticMiddleware

from app import app

APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])


leancloud.init(APP_ID, master_key=MASTER_KEY)

class RewritePathMiddleware:
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, startResponse):
        path = environ['PATH_INFO']
        if path == '/' or not path:
            environ['PATH_INFO'] = '/static/index.html'
        elif path.endswith('.html'):
            environ['PATH_INFO'] = '/static'+path
        return self._app(environ, startResponse)


engine = app.wsgifunc()
#engine = leancloud.HttpsRedirectMiddleware(engine)
engine = leancloud.Engine(engine)
engine = StaticMiddleware(engine)
engine = RewritePathMiddleware(engine)
application = engine


if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    app.debug = True
    server = WSGIServer(('localhost', PORT), application, handler_class=WebSocketHandler)
    #server = WSGIServer(('localhost', PORT), application)
    server.serve_forever()
