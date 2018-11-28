# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-28 18:20:59
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-28 18:51:29

import numpy as np 

arr = np.arange(0,60,5)
arr = arr.reshape(3,4)
print(arr)
for num in np.nditer(arr):
    print(num,end = " ")

'''
numpy.reshape:函数在不改变数据的条件下修改形状
numpy.reshape(arr, newshape, order')
arr：要修改形状的数组
newshape：整数或者整数数组，新的形状应当兼容原有形状
order：'C'为 C 风格顺序，'F'为 F 风格顺序，'A'为保留原顺序。
'''

'''
numpy.ndarray.flat:该函数返回数组上的一维迭代器，行为类似 Python 内建的迭代器
'''
print()
print(arr.flat)
print(arr.flat[5])

'''
numpy.ndarray.flatten:该函数返回折叠为一维的数组副本
ndarray.flatten(order)
'''
print(arr.flatten(order = 'C'))

'''
numpy.transpose:翻转给定数组的维度。如果可能的话它会返回一个视图
numpy.transpose(arr, axes)
arr：要转置的数组
axes：整数的列表，对应维度，通常所有维度都会翻转。
'''
print(np.transpose(arr))
'''
[1,0]表示将第1维放在最前面，将0维放在第二位置
'''
print(np.transpose(arr,[1,0]))

'''
numpy.ndarray.T：行为类似于numpy.transpose
'''
print(arr.T)

'''
numpy.rollaxis:该函数向后滚动特定的轴，直到一个特定位置
numpy.rollaxis(arr, axis, start)
arr：输入数组
axis：要向后滚动的轴，其它轴的相对位置不会改变
start：默认为零，表示完整的滚动。会滚动到特定位置。
'''
