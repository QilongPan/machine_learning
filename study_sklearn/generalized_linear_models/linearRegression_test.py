# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-21 11:06:11
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-21 11:39:36
'''
最小二乘法 线性回归
'''
from sklearn import linear_model

reg = linear_model.LinearRegression()
train_x = [[0,0],[1,1],[2,2]]
train_y = [0,1,2]
test_x = [[3,3],[4,4]]
test_y = [3,4]
#获取模型输入参数
#输出{'copy_X': True, 'fit_intercept': True, 'n_jobs': None, 'normalize': False}
print(reg.get_params())
#训练模型
reg.fit(train_x,train_y)
#获取w的取值
print(reg.coef_)
#预测值
predict_y = reg.predict(test_x)
print(predict_y)
score = reg.score(test_x,test_y)
print(score)