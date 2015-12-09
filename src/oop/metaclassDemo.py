#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: metaclassDemo.py
@time: 2015/12/8 16:01
"""


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)
