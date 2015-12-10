#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: jsonDemo.py
@time: 2015/12/9 15:03
"""

import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)
jsonstr = json.dumps(s, default=lambda obj: obj.__dict__)
print(jsonstr)
std = json.loads(jsonstr, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(std)
