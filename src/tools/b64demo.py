#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: b64demo.py
@time: 2015/12/14 13:51
"""

import base64


def safe_base64_decode(s):
    a = len(s) % 4
    s += b'=' * a
    return base64.b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
