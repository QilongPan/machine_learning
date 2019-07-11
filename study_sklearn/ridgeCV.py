
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 16:06:01
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
from sklearn import linear_model
reg = linear_model.RidgeCV(alphas = [0.1,1.0,10.0],cv = 3)
reg.fit([[0,0],[0,0],[1,1]],[0,0.1,1])
print(reg.alpha_)