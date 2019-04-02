
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 08:50:40
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import pandas as pd 
import numpy as np 

df = pd.DataFrame([[1,np.nan,1],[1,2,1]])
print(df)
print(df.sum(skipna = True))