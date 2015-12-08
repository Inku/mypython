#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: student.py
@time: 2015/12/7 15:37
"""


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s的成绩为%s" % (self.__name, self.__score))


if __name__ == "__main__":
    alan = Student("alan", 62)
    alan.print_score()
