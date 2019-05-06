# -*- coding: utf-8 -*-
# @Date    : 2019-05-06 14:21:51
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
from collections import Counter

words = [
    'look', 'into', 'my', 'look', 'into', 'my', 
    'the',  'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

print(Counter(words))
#OUT
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, "you're": 1, "don't": 1, 'under': 1, 'not': 1})


print (Counter(words).most_common(1)[0][0])