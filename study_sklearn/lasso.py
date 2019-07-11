
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 16:10:15
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
from sklearn import linear_model
reg = linear_model.Lasso(alpha = 0.1)
reg.fit([[0,0],[1,1]],[0,1])
print(reg.predict([[1,1]]))
