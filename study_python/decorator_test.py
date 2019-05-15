# -*- coding: utf-8 -*-
# @Date    : 2019-05-15 14:21:18
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
# 装饰器实现案例
# https://www.cnblogs.com/cicaday/p/python-decorator.html

class WithoutDecorators:

    def some_static_method():
        print("this is static method")
    some_static_method = staticmethod(some_static_method)

    def some_class_method():
        print("this is class method")

    some_class_method = classmethod(some_class_method)

class WithDecorators:

    @staticmethod
    def some_static_method():
        print("this is static method")

    @classmethod
    def some_class_method():
        print("this is class method")


class Person(object):

    x = 2
    def __init__(self):
        self._name = "bob"

        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        print("set name")
        self._name = value
    #静态方法，类和对象都可以直接调用
    @staticmethod
    def add(a,b,c):
        return a+b+c

    #类方法，类在使用时会将类本身当做参数穿给类的第一个参数Person.print_name
    @classmethod
    def print_name(B):
        print(B.x)

class B:
    x = 2

person = Person()
person.name = "hi"
person.print_name()
print(person.name)
print(person.add(1,2,3))
Person.print_name()
print(Person.add(1,2,3))


'''
def debug(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        return func()
    return wrapper

def say_hello():
    print "hello!"

say_hello = debug(say_hello)  # 添加功能并保持原函数名不变
'''

'''
def debug(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        return func()
    return wrapper

@debug
def say_hello():
    print "hello!"

'''
#带参数版本
#
'''
def debug(func):
    def wrapper(something):  # 指定一毛一样的参数
        print "[DEBUG]: enter {}()".format(func.__name__)
        return func(something)
    return wrapper  # 返回包装过函数

@debug
def say(something):
    print "hello {}!".format(something)

'''

#带多个参数版本
def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print "[DEBUG]: enter {}()".format(func.__name__)
        print 'Prepare and say...',
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print "hello {}!".format(something)