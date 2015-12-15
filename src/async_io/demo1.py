#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@file: demo1.py
@time: 2015/12/15 14:22
"""

import asyncio


@asyncio.coroutine
def hello():
    print('Hello world!')
    yield from asyncio.sleep(1)
    print('hello again')


tasks = [hello(), hello()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
