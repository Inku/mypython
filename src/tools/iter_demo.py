#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: iter_demo.py
@time: 2015/12/14 14:46
"""

import itertools

iterable = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 10, iterable)
for n in ns:
    print(n)
