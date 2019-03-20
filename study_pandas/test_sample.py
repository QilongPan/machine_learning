
# -*- coding: utf-8 -*-
# @Date    : 2019-03-13 10:34:52
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import pandas as pd 

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                    'num_specimen_seen': [10, 2, 1, 8]},
                   index=['falcon', 'dog', 'spider', 'fish'])
#random_state为随机种子，如果值一样，那么采样的数据也一样
print(df.sample(n = 3,random_state = 1))