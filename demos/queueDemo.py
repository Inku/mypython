#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: queueDemo.py
@time: 2015/10/22 15:25
"""

from collections import deque

queue = deque(["a", "b", "c"])
queue.append("d")
queue.append("e")
print(queue)
print(queue.popleft())
print(queue)
print(queue.pop())
print(queue)
