#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: queueDemo.py
@time: 2015/12/10 10:07
"""
from multiprocessing import Queue, Process
import os, time, random


def write(queue):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        queue.put(value)
        time.sleep(random.random())


def read(queue):
    print('Process to read: %s' % os.getpid())
    while True:
        value = queue.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
