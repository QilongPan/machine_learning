# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-28 18:20:59
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-29 14:33:48

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

'''
numpy.resize:此函数返回指定大小的新数组。 如果新大小大于原始大小，则包含原始数组中的元素的重复副本
numpy.resize(arr, shape)
arr：要修改大小的输入数组
shape：返回数组的新形状
'''
arr2 = np.array([[1,2,3],[4,5,6]])
print(np.resize(arr2,(3,2)))
print(np.resize(arr2,(3,3)))

'''
numpy.append:此函数在输入数组的末尾添加值。
附加操作不是原地的，而是分配新的数组。 此外，输入数组的维度必须匹配否则将生成ValueError
numpy.append(arr, values, axis)
arr：输入数组
values：要向arr添加的值，比如和arr形状相同(除了要添加的轴)
axis：沿着它完成操作的轴。如果没有提供，两个参数都会被展开
'''
arr3 = np.array([[1,2,3],[4,5,6]])
print(np.append(arr3,[7,8,9]))
print(np.append(arr3,[[7,8,9]],axis = 0))
print(np.append(arr3,[[5,5,5],[7,8,9]],axis = 1))

'''
numpy.insert:此函数在给定索引之前，沿给定轴在输入数组中插入值。 
如果值的类型转换为要插入，则它与输入数组不同。 
插入没有原地的，函数会返回一个新数组。 
此外，如果未提供轴，则输入数组会被展开
numpy.insert(arr, obj, values, axis)
arr：输入数组
obj：在其之前插入值的索引
values：要插入的值
axis：沿着它插入的轴，如果未提供，则输入数组会被展开
'''

'''
numpy.unique:此函数返回输入数组中的去重元素数组。 
该函数能够返回一个元组，包含去重数组和相关索引的数组。 
索引的性质取决于函数调用中返回参数的类型。
numpy.unique(arr, return_index, return_inverse, return_counts)
arr：输入数组，如果不是一维数组则会展开
return_index：如果为true，返回输入数组中的元素下标
return_inverse：如果为true，返回去重数组的下标，它可以用于重构输入数组
return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
'''
arr4 = np.array([5,2,6,2,7,5,6,8,2,9])
print(np.unique((arr4)))