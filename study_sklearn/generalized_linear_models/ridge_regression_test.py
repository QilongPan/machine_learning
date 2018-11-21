# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-21 11:38:55
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-21 13:20:07
# 
'''
岭回归为了解决线性回归中出现的过拟合以及通过正规方程方法求解的过程中出现的x装置乘以x不可逆这两类问题
'''
from sklearn import linear_model

reg = linear_model.Ridge(alpha = 0.5)
train_x = [[0,0],[0,0],[1,1]]
train_y = [0,0.1,1]
reg.fit(train_x,train_y)
#输出系数w
print(reg.coef_)
#输出截距b
print(reg.intercept_)