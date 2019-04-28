# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 09:34:42
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import multiprocessing
import time

def func(msg):
    for i in range(3):
        print(msg)
        time.sleep(1)

'''
单线程
'''
if __name__ == "__main__":
    start = time.time()
    for i in range(10):
        msg = "hello %d" %(i)
        func(msg)
    end = time.time()
    print(end-start)
    print("Sub-process(es) done.")

'''
多线程
'''
if __name__ == "__main__":
    start = time.time()
    pool = multiprocessing.Pool(processes=4)
    for i in range(10):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))
    pool.close()
    pool.join()
    end = time.time()
    print(end-start)
    print("Sub-process(es) done.")