# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 14:09:21
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
# 生成器实现案例

def fibonacci():
    a,b = 0,1
    while True:
        yield b
        a,b = b,a+b

fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))