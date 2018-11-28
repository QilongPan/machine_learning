# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-28 15:13:27
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-28 15:41:39

import numpy as np 

'''
numpy.empty:它创建指定形状和dtype的未初始化数组.它使用以下构造函数：
numpy.empty(shape, dtype = float, order = 'C')
注意：数组元素为随机值，因为它们未初始化。
序号  参数及描述
1.  Shape 空数组的形状，整数或整数元组
2.  Dtype 所需的输出数组类型，可选
3.  Order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''
arr1 = np.empty(shape = [3,2],dtype = np.int32)
print(arr1)

'''
numpy.zeros:返回特定大小,以0填充的新数组
numpy.zeros(shape, dtype = float, order = 'C')
序号  参数及描述
1.  Shape 空数组的形状，整数或整数元组
2.  Dtype 所需的输出数组类型，可选
3.  Order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''

arr2 = np.zeros(shape = [3,2],dtype = np.float32)
print(arr2)

#自定义类型
arr3 = np.zeros((2,2), dtype =  [('x','i4'),  ('y',np.float32)])
print(arr3)

'''
numpy.ones:返回特定大小，以 1 填充的新数组
numpy.ones(shape, dtype = None, order = 'C')
序号  参数及描述
1.  Shape 空数组的形状，整数或整数元组
2.  Dtype 所需的输出数组类型，可选
3.  Order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''
arr4 = np.ones(shape = [2,3],dtype = int)
print(arr4)

'''
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
'''
arr = np.array([1.0,2,3],dtype = np.bool_,order = 'C')
print(arr)
'''
numpy.asarray:此函数类似于numpy.array，除了它有较少的参数.它对于将Python序列转换为ndarray非常有用
numpy.asarray(a, dtype = None, order = None)
序号  参数及描述
1.  a 任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
2.  dtype 通常，输入数据的类型会应用到返回的ndarray
3.  order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''
list1 = [1,2,3]
arr5 = np.asarray(list1)
print(arr5)

tuple1 = [(1,2,3),(4,5)]
arr6 = np.asarray(tuple1)
print(arr6)

'''
numpy.frombuffer:此函数将缓冲区解释为一维数组。 暴露缓冲区接口的任何对象都用作参数来返回ndarray
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
序号  参数及描述
1.  buffer 任何暴露缓冲区借口的对象
2.  dtype 返回数组的数据类型，默认为float
3.  count 需要读取的数据数量，默认为-1，读取所有数据
4.  offset 需要读取的起始位置，默认为0
'''
s= b'Hello World'

arr7 = np.frombuffer(s, dtype =  'S1')
print(arr7)

'''
numpy.fromiter:函数从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组
numpy.fromiter(iterable, dtype, count = -1)
序号  参数及描述
1.  iterable 任何可迭代对象
2.  dtype 返回数组的数据类型
3.  count 需要读取的数据数量，默认为-1，读取所有数据
'''

list1 = range(5)
iter1 = iter(list1)
arr8 = np.fromiter(iter1,dtype = float)
print(arr8)

'''
numpy.arange:返回ndarray对象，包含给定范围内的等间隔值
numpy.arange(start, stop, step, dtype)
序号  参数及描述
1.  start 范围的起始值，默认为0
2.  stop 范围的终止值(不包含)
3.  step 两个值的间隔，默认为1
4.  dtype 返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
'''

arr9 = np.arange(0,5,2,dtype = int)
print(arr9)

'''
numpy.linspace:此函数类似于arange()函数。 在此函数中，指定了范围之间的均匀间隔数量，而不是步长。 此函数的用法如下。
numpy.linspace(start, stop, num, endpoint, retstep, dtype)
序号  参数及描述
1.  start 序列的起始值
2.  stop 序列的终止值，如果endpoint为true，该值包含于序列中
3.  num 要生成的等间隔样例数量，默认为50
4.  endpoint 序列中是否包含stop值，默认为ture
5.  retstep 如果为true，返回样例，以及连续数字之间的步长
6.  dtype 输出ndarray的数据类型
'''
arr10 = np.linspace(0,20,5,endpoint =  False)
print(arr10)

'''
numpy.logspace:此函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字。 刻度的开始和结束端点是某个底数的幂，通常为 10
numpy.logscale(start, stop, num, endpoint, base, dtype)
序号  参数及描述
1.  start 起始值是base ** start
2.  stop 终止值是base ** stop
3.  num 范围内的数值数量，默认为50
4.  endpoint 如果为true，终止值包含在输出数组当中
5.  base 对数空间的底数，默认为10
6.  dtype 输出数组的数据类型，如果没有提供，则取决于其它参数
'''

arr11 = np.logspace(1.0,2.0,num = 10)
print(arr11)