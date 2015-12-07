#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: palindrome.py
@time: 2015/12/7 10:27
"""


def is_palindrome(n):
    s = str(n)
    s1 = s[::-1]
    return s == s1


# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))
