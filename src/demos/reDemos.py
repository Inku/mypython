#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: reDemos.py
@time: 2015/12/14 10:24
"""

import re

e1 = 'someone@gmail.com'
e2 = 'bill.gates@microsoft.com'

re_email = re.compile(r'[\w|.]+@\w+.\w+')
flag = re.match(re_email, e2)

print(flag)
