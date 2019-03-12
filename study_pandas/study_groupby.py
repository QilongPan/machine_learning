
# -*- coding: utf-8 -*-
# @Date    : 2019-03-12 15:17:51
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com

import pandas as pd
import numpy as np

df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
               ('bird', 'Psittaciformes', 24.0),
                      ('mammal', 'Carnivora', 80.2),
                     ('mammal', 'Primates', np.nan),
                      ('mammal', 'Carnivora', 58)],
                      index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                    columns=('class', 'order', 'max_speed'))
df.loc[df['class'] == 'bird', 'max_speed'] = 100
print(df)
print("*****************************")
grouped = df.groupby(['class'],as_index = False)
data = pd.DataFrame()
data['class'] = df['class']
print(df.groupby(['class'])['max_speed'].max().values)
data.drop_duplicates(subset  = ['class'],inplace = True )
data['s'] = df.groupby(['class'])['max_speed'].max().values
data['count'] = df.groupby(['class'])['class'].size().values
#data['count'] = df.groupby(['class']).count().values
print(data)