# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-28 15:53:22
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-28 16:05:04

import numpy as np 

'''
ndarray对象的内容可以通过索引或切片来访问和修改，就像 Python 的内置容器对象一样。
如前所述，ndarray对象中的元素遵循基于零的索引。 
有三种可用的索引方法类型： 字段访问，基本切片和高级索引。
基本切片是 Python 中基本切片概念到 n 维的扩展。 
通过将start，stop和step参数提供给内置的slice函数来构造一个 Python slice对象。 
此slice对象被传递给数组来提取数组的一部分。
'''

arr1 = np.arange(10)
slice1 = slice(2,7,2)
print(arr1[slice1])

'''
通过将由冒号分隔的切片参数(start:stop:step)直接提供给ndarray对象，也可以获得相同的结果
'''
arr2 = np.arange(10)
print(arr2[2:7:2])
'''
如果只输入一个参数，则将返回与索引对应的单个项目。
如果使用a:，则从该索引向后的所有项目将被提取。
如果使用两个参数(以:分隔)，则对两个索引(不包括停止索引)之间的元素以默认步骤进行切片
'''
print(arr2[0])
print(arr2[0:])
print(arr2[0:2])
print(arr2[0:2:2])

'''
切片还可以包括省略号(...)，来使选择元组的长度与数组的维度相同。 如果在行位置使用省略号，它将返回包含行中元素的ndarray
'''
# 最开始的数组  
arr3 = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(arr3[0,0])
print('我们的数组是：')
print(arr3)
# 这会返回第二列元素的数组：  
print('第二列的元素是：')
print(arr3[...,1])
# 现在我们从第二行切片所有元素：  
print('第二行的元素是：')
print(arr3[1,...])
# 现在我们从第二列向后切片所有元素：
print('第二列及其剩余元素是：')
print(arr3[...,1:])