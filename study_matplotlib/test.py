# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-01 10:16:49
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-01 10:17:33
import matplotlib.pyplot as plt 
import numpy as np 

plt.figure(figsize=(20, 20))
#plt.subplots(1, 4)
plt.title('pic 1')
plt.subplot(1, 4, 2)
plt.title('pic x')
plt.grid(True)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.subplot(1, 4, 3)
plt.subplot(1, 4, 4)
plt.show()
