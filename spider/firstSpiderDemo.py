#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: firstSpiderDemo.py
@time: 2015/10/22 14:50
"""

from urllib import parse, request

data = {'word': 'Jecvay Notes'}

url_values = parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values
print(full_url)

data = request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)
