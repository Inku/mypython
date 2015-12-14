#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: bmpinfo.py
@time: 2015/12/14 14:06
"""

import struct


def check_bmp(path):
    with open(path, 'rb') as f:
        s = f.readline(30)
        try:
            data = struct.unpack('<ccIIIIIIHH', s)
            if data[0] == b'B' and data[1] == b'M':
                print('is bmp!')
                print('width=%s' % data[6])
                print('height=%s' % data[7])
                print('color_count=%s' % data[9])
                print(data)
            else:
                print('not bmp')

        except struct.error:
            print('not bmp')


if __name__ == '__main__':
    file_path = 'D:\\Workspace\\private\\mypython\\resources\\b.bmp'
    check_bmp(file_path)
