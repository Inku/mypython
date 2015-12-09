#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: user.py
@time: 2015/12/8 16:10
"""
from src.ORM import model


class User(model.Model):
    id = model.Model.IntegerField('id')
