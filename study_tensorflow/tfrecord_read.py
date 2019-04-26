
# -*- coding: utf-8 -*-
# @Date    : 2019-04-25 17:14:28
# @Author  : QilongPan 
# @Email   : 3102377627@qq.com
import tensorflow as tf

'''
for serialized_example in tf.python_io.tf_record_iterator('test.tfrecords'):
    example = tf.train.Example()
    example.ParseFromString(serialized_example)

    label = example.features.feature['features'].float_list.value
    # 可以做一些预处理之类的
    print(label)

'''

reader = tf.TFRecordReader()

#根据文件生成一个队列
filename_queue = tf.train.string_input_producer(
    ['test.tfrecords'],num_epochs=1)
#返回文件名和文件
file_name, serialized_example = reader.read(filename_queue)
print(file_name)
read_data = tf.io.parse_single_example(
  serialized_example,
  # Defaults are not specified since both keys are required.
  features={
      'features': tf.FixedLenFeature([], tf.float32),
      'label': tf.FixedLenFeature([], tf.float32),
  })

sess = tf.Session()
sess.run(tf.global_variables_initializer())
sess.run(read_data['label'])
print("complish")