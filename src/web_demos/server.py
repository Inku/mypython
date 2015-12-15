#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: server.py
@time: 2015/12/14 17:19
"""

from wsgiref.simple_server import make_server
from web_demos.wsgi_demo import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
