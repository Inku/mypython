#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: dumpDemo.py
@time: 2015/12/9 15:02
"""

import pickle

d = dict(name='Bob', age=20, score=88)

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    x = pickle.load(f)
    print(x)
