# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-29 16:01:13
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-29 16:11:54
import pandas as pd 
'''
read_csv使用
'''
'''
data_train = pd.read_csv("E:/allcode/machineLearningExercise/titanic/data/train.csv")
print(data_train)
'''
'''
to_csv()是DataFrame类的方法，read_csv()是pandas的方法
'''
data = [[1,1],[1,1],[1,1],[1,1]]
df = pd.DataFrame(data)
for i in range(df.shape[0]):
    data = df.iloc[i].values
    label = float(data[len(data)-1])
    features = [float(i) for i in data[:len(data)-1]]
    print(label)
    print(features)
'''
index= False 表示不需要下标
'''
'''
df.to_csv("logistic_regression_predictions.csv",index = False)
print(df)
'''