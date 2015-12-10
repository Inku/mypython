#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: deadloopDemo.py
@time: 2015/12/10 10:57
"""

import threading, multiprocessing


def loop():
    x = 0
    while True:
        x ^= 2


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
