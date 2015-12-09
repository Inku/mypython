#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: stringIODemo.py
@time: 2015/12/9 14:24
"""

from io import StringIO, BytesIO

f = StringIO('Hello!\nHi\n')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())