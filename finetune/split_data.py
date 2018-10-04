import numpy as np
import numpy.random as npr
import sys
import cv2
import os
import numpy as np
import pickle as pickle
import pandas as pd

from sklearn.model_selection import train_test_split


# 验证集比例
val_ratio = 0.12

# 读取训练图片列表
all_data = pd.read_csv('data/label.csv')
# 分离训练集和测试集，stratify参数用于分层抽样
train_data_list, val_data_list = train_test_split(all_data, test_size=val_ratio, random_state=666, stratify=all_data['label'])
# 读取测试图片列表
test_data_list = pd.read_csv('data/test.csv')

train_path = list(train_data_list['img_path'])
train_label = list(train_data_list['label'])



val_path = list(val_data_list['img_path'])
val_label = list(val_data_list['label'])



print(train_label)

 
with open('train.txt', 'w') as f:
    for i in range(len(train_path)):
       f.write(train_path[i]+" "+str(train_label[i]))
       f.write('\n')


with open('val.txt', 'w') as f:
    for i in range(len(val_path)):
       f.write(val_path[i]+" "+str(val_label[i]))
       f.write('\n')

