#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: test.py
@time: 2015/12/7 10:11
"""

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    tz_re = re.compile(r'UTC([\+|\-]\d+):\d+')
    groups = re.match(tz_re, tz_str).groups()
    tz = int(groups[0])

    tz_user = timezone(timedelta(hours=tz))
    date = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    date = date.replace(tzinfo=tz_user)

    return date.timestamp()


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
