#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: inheritDemo.py
@time: 2015/12/7 16:09
"""


class Animal(object):
    def run(self):
        print("animal running")


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == "__main__":
    dog = Dog()
    dog.run()

    Cat().run()