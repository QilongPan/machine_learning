# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 10:24:59
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import tensorflow as tf
def convert_to_tfrecord(output_file_path="test.tfrecords"):
    print("enter")
    writer = tf.python_io.TFRecordWriter(output_file_path)
    data = [1,2,3]
    label = 1
    features = [1,2,3]
    example = tf.train.Example(features=tf.train.Features(
        feature={
        "label":
            tf.train.Feature(float_list=tf.train.FloatList(value=[label])),
        "features":
            tf.train.Feature(float_list=tf.train.FloatList(value=features)),
    }))
    writer.write(example.SerializeToString()) 
    writer.close()
    print("convert to complish")

convert_to_tfrecord()