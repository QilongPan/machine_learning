# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-05 15:48:17
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-05 17:21:27

'''
tutorial: https://blog.csdn.net/qq_33120943/article/details/76569756
'''
import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns
#用pandas读取文件并将第一行设为ID行
df = pd.read_csv("train.csv")
'''
sns.lmplot(x="Age",y = "Survived",data = df,fit_reg = False)
plt.ylim(0,None)
plt.xlim(0,None)
'''
#sns.boxplot(data = df)

sns.countplot(x='Survived',data = df)

plt.show()