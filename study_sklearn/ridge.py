
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 15:38:12
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

from sklearn import linear_model

reg = linear_model.Ridge(alpha = 0.5)
reg.fit([[0,0],[0,0],[1,1]],[0,0.1,1])
print(reg.coef_)
print(reg.intercept_)