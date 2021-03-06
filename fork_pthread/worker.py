#!/usr/bin/python3
# -*- coding:utf-8 -*-

import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManger(BaseManager):
    pass


if __name__ == "__main__":
    QueueManger.register('get_task_queue')
    QueueManger.register('get_result_queue')

    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)

    m = QueueManger(address=(server_addr,5000),authkey=b'abc')
    m.connent()
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 从task队列取任务,并把结果写入result队列:
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print('task queue is empty.')
    # 处理结束:
    print('worker exit.')