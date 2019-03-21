
# -*- coding: utf-8 -*-
# @Date    : 2019-03-20 08:23:31
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
#python的字典内部实现是散列表，所以字典的键值必须是可hash的
#python搜索或者遍历时用的并不是键值的值比对，而是键值的hash值去比，那么遍历顺序就应该跟hash值的值有关。
#
a={"a":"1", "b":"1", "c":"1", "d":"1"}
for i in a:
    print(i)
#输出顺序为：a,c,b,d
print(a)
#输出：{'a': '1', 'c': '1', 'b': '1', 'd': '1'}
