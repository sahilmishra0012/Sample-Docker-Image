import os
import numpy as np
import pandas
from cv2 import cv2
from tqdm import tqdm
import tensorflow as tf


def create_tf_example(data):
    
    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/encoded': tf.train.Feature(bytes_list=tf.train.BytesList(value=[data['Image Encoded']])),
        'image/format': tf.train.Feature(bytes_list=tf.train.BytesList(value=['jpeg'.encode('utf-8')])),
        'image/class/label': tf.train.Feature(int64_list=tf.train.Int64List(value=[data['Label ID']])),
        'image/class/text': tf.train.Feature(bytes_list=tf.train.BytesList(value=[data['Label'].encode('utf-8')])),
    }))
    return tf_example

data = pandas.read_csv('images/output.csv')
data.sort_values(by=['Image ID'], inplace=True)

train = data[:11227]
val = data[11227:]

train_images = []
train_heights = []
train_widths = []

c=0
for i in tqdm(train['Image ID']):
    image = cv2.imread(os.path.join('images/img',i))
    if c%2==0:
        image = cv2.resize(image, (150, 150), interpolation = cv2.INTER_NEAREST) 
    else:
        image = cv2.resize(image, (200, 200), interpolation = cv2.INTER_NEAREST) 
    c=c+1
    print(image.shape)
    img_data =cv2.imencode('.jpg', image)[1].tostring()
    height = image.shape[0]
    width = image.shape[1] 
    train_images.append(img_data)
    train_heights.append(height)
    train_widths.append(width)
    
    
val_images = []
val_heights = []
val_widths = []

c=0
for i in tqdm(val['Image ID']):
    image = cv2.imread(os.path.join('images/img',i))
    if c%2==0:
        image = cv2.resize(image, (150, 150), interpolation = cv2.INTER_NEAREST) 
    else:
        image = cv2.resize(image, (200, 200), interpolation = cv2.INTER_NEAREST) 
    c=c+1
    print(image.shape)
    img_data =cv2.imencode('.jpg', image)[1].tostring()
    height = image.shape[0]
    width = image.shape[1] 
    val_images.append(img_data)
    val_heights.append(height)
    val_widths.append(width)
    
train['Image Encoded'] = train_images
train['Height'] = train_heights
train['Width'] = train_widths

val['Image Encoded'] = val_images
val['Height'] = val_heights
val['Width'] = val_widths



with tf.io.TFRecordWriter("train.tfrecord") as writer:
    for i in tqdm(train.iterrows()):
        example = create_tf_example(i[1])
        writer.write(example.SerializeToString())
writer.close()

with tf.io.TFRecordWriter("validation.tfrecord") as writer:
    for i in tqdm(val.iterrows()):
        example = create_tf_example(i[1])
        writer.write(example.SerializeToString())
writer.close()