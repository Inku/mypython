#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: normalize.py
@time: 2015/12/3 14:34
"""


def normalize(name):
    return name[0].upper() + name[1:].lower()


if __name__ == '__main__':
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)
