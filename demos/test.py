#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: test.py
@time: 2015/12/7 10:11
"""


def count():
    f = lambda j: lambda: j * j

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
