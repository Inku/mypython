#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: prodDemo.py
@time: 2015/12/3 14:45
"""

from functools import reduce


def prod(iteraterable):
    return reduce(lambda x, y: x * y, iteraterable)


if __name__ == '__main__':
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
