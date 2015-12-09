#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: decoratorDemo.py
@time: 2015/12/7 14:16
"""

import functools


def log(va):
    if callable(va):
        func = va

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s():' % func.__name__)
            re = func(*args, **kw)
            print('end call')
            return re

        return wrapper
    else:
        msg = va

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (msg, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator


@log("execute")
def now():
    print('2015-3-25')


now()
