# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-06 09:18:01
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-12 10:42:19
import numpy as np 
'''
numpy.mean(a, axis, dtype, out，keepdims )
mean()函数功能：求取均值 
经常操作的参数为axis，以m * n矩阵举例：
axis 不设置值，对 m*n 个数求均值，返回一个实数
axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵
'''
arr1 = np.array([[1,2],[3,4]])
print(np.mean(arr1))
# axis=0，计算每一列的均值
print(np.mean(arr1,axis = 0))
# 计算每一行的均值 
print(np.mean(arr1,axis = 1))

arr2 = np.array([1,2,3,4])
print(np.tanh(arr2))