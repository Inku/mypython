#!/usr/bin/env python
# encoding: utf-8

"""
@author: Inku
@software: PyCharm
@file: task_master.py
@time: 2015/12/11 14:18
"""

import queue
import random
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


def test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=queue.Queue)
    QueueManager.register('get_result_queue', callable=queue.Queue)

    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=30)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    freeze_support()
    test()
