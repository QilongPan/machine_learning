
# -*- coding: utf-8 -*-
# @Date    : 2019-04-25 17:12:18
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import tensorflow as tf
# 写入的文件的路径
file_path = 'test.tfrecords'
# 等待写入的数组
list = [2,3,4,5,6,7]
writer = tf.python_io.TFRecordWriter(file_path)
example = tf.train.Example(features=tf.train.Features(
	feature={
    "label": tf.train.Feature(int64_list=tf.train.Int64List(value=list))
}))
writer.write(example.SerializeToString())
