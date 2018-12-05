# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-05 15:21:15
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-05 15:38:25

import numpy as np 

'''
numpy.random.rand()
numpy.random.rand(d0,d1,…,dn)
rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
dn表格每个维度
返回值为指定维度的array
'''
print(np.random.rand(4,2))

'''
numpy.random.randn()
numpy.random.randn(d0,d1,…,dn)
randn函数返回一个或一组样本，具有标准正态分布。
dn表格每个维度
返回值为指定维度的array
'''
print(np.random.randn(2,4))


'''
numpy.random.randint()
numpy.random.randint(low, high=None, size=None, dtype=’l’)
返回随机整数，范围区间为[low,high），包含low，不包含high
参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int
high没有填写时，默认生成随机数的范围是[0，low)
'''
# 返回[0,1)之间的整数，所以只有0)
print(np.random.randint(1,size=5))

'''
numpy.random.random_integers
numpy.random.random_integers(low, high=None, size=None)
返回随机整数，范围区间为[low,high]，包含low和high
参数：low为最小值，high为最大值，size为数组维度大小
high没有填写时，默认生成随机数的范围是[1，low]
该函数在最新的numpy版本中已被替代，建议使用randint函数
'''
print(np.random.random_integers(1,size=5))

'''
生成[0,1)之间的浮点数
numpy.random.random_sample(size=None)
numpy.random.random(size=None)
numpy.random.ranf(size=None)
numpy.random.sample(size=None)
'''
print('-----------random_sample--------------')
print(np.random.random_sample(size=(2,2)))
print('-----------random--------------')
print(np.random.random(size=(2,2)))
print('-----------ranf--------------')
print(np.random.ranf(size=(2,2)))
print('-----------sample--------------')
print(np.random.sample(size=(2,2)))

'''
numpy.random.choice()
numpy.random.choice(a, size=None, replace=True, p=None)
从给定的一维数组中生成随机数
参数： a为一维数组类似数据或整数；size为数组维度；p为数组中的数据出现的概率
a为整数时，对应的一维数组为np.arange(a)
replace:为False时，生成的随机数不能有重复的数值
参数p的长度与参数a的长度需要一致
参数p为概率，p里的数据之和应为1
'''
print(np.random.choice(5,3,replace = False))

'''
numpy.random.seed()
np.random.seed()的作用：使得随机数据可预测。
当我们设置相同的seed，每次生成的随机数相同。
如果不设置seed，则每次会生成不同的随机数
'''
np.random.seed(0)
print(np.random.rand(5))
np.random.seed(1676)
print(np.random.rand(5))
np.random.seed(1676)
print(np.random.rand(5))