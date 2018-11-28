# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-11-28 13:30:26
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-11-28 15:12:44

import numpy as np 

'''
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)

object:任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列。
dtype:数组的所需数据类型，可选。
copy:可选，默认为true，对象是否被复制
order:C(为按行的C风格数组)、F(为按列的Fortran风格数组)或A(任意，默认)。
subok:默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类
ndimin:指定返回数组的最小维数

C(按行)、F(按列)或A(任意，默认)。
ndarray对象由计算机内存中的一维连续区域组成，带有将每个元素映射到内存块中某个位置的索引方案。 
内存块以按行(C 风格)或按列(FORTRAN 或MatLab风格)的方式保存元素。
如果把这一段内存地址视为 2*4 元素的二维数组，则 Fortran 和 C 还有另一个差异：
Fortran 会先变化前面的维度，即顺序为 a(1,1) , a(2,1) .... 前面的 1 先变化为 2，后面维度始终保持为 1。
直到循环完毕后，再将后面的维度加一，即 a(1,2) , a(2,2).....
C 语言则相反，会先变化后面的维度，即顺序为 a[0][0] , a[0][1] .... 后面的 0 先变化为 1，前面维度始终保持为 0。
直到循环完毕后，再将前面的维度加一，即 a[1][0] , a[1][1].....
'''

arr = np.array([1.0,2,3],dtype = np.bool_,order = 'C')
print(arr)

arr2 = np.array([[1,2],[3,4]])
print(arr2)

arr3 = np.array([1,2,3,4,5,6],ndmin = 2)
print(arr3)


'''
1.  bool_存储为一个字节的布尔值(真或假)
2.  int_默认整数，相当于 C 的long，通常为int32或int64
3.  intc相当于 C 的int，通常为int32或int64
4.  intp用于索引的整数，相当于 C 的size_t，通常为int32或int64
5.  int8字节(-128 ~ 127)
6.  int1616 位整数(-32768 ~ 32767)
7.  int3232 位整数(-2147483648 ~ 2147483647)
8.  int6464 位整数(-9223372036854775808 ~ 9223372036854775807)
9.  uint88 位无符号整数(0 ~ 255)
10. uint1616 位无符号整数(0 ~ 65535)
11. uint3232 位无符号整数(0 ~ 4294967295)
12. uint6464 位无符号整数(0 ~ 18446744073709551615)
13. float_float64的简写
14. float16半精度浮点：符号位，5 位指数，10 位尾数
15. float32单精度浮点：符号位，8 位指数，23 位尾数
16. float64双精度浮点：符号位，11 位指数，52 位尾数
17. complex_complex128的简写
18. complex64复数，由两个 32 位浮点表示(实部和虚部)
19. complex128复数，由两个 64 位浮点表示(实部和虚部)
'''
#获取dtype对象
dt = np.dtype(np.int32)
arr4 = np.array([1.0,3.2],dtype = dt)
print(arr4)

dt2 = np.dtype([('age',np.int8)]) 
arr5 = np.array([(10,),(20,),(30,)], dtype = dt2)  
print(arr5['age'])

student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')]) 
arr6 = np.array([('abc',  21,  50),('xyz',  18,  75)], dtype = student)  
print(arr6)


'''
ndarray.shape:返回一个包含数组维度的元组，它也可以用于调整数组大小
'''
print(np.array([[1,2,3],[4,5,6]]).shape)
arr7 = np.array([[1,2,3],[4,5,6]]) 
arr7.shape =  (3,2)  
print(arr7)

'''
ndarray.ndim:返回数组的维数
'''
arr8 = np.arange(24)
arr9 = arr8.reshape(2,4,3)
print(arr9)
print("ndim:" + str(arr9.ndim))

'''
numpy.itemsize:返回数组中每个元素的字节单位长度
'''
arr10 = np.array([1,2,3,4,5], dtype = np.int8)
print(arr10.itemsize)
