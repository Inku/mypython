#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: myclass.py
@time: 2015/12/8 14:18
"""


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'students\'s name=%s' % self.__name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    __repr__ = __str__


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    s = Student('alan')
    print(s)
    print(Fib()[2])
