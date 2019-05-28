# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 14:23:30
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
# 相同的组不会出现在两个不同的折叠中(不同组的数量必须至少等于折叠的数量)
# group定义了每天数据的分组id
from sklearn.model_selection import GroupKFold 
import numpy as np 

X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 3, 4])
groups = np.array([0,0, 2, 2])
group_kfold = GroupKFold(n_splits=2)
for train_index,test_index in group_kfold.split(X, y, groups):
    print(train_index)
    print(test_index)
