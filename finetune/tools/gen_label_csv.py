#coding:utf-8
import os
import math
import numpy as np
import pandas as pd
import os.path as osp
from tqdm import tqdm

label_warp = {'正常': 0,
              '不导电': 1,
              '擦花': 2,
              '横条压凹': 3,
              '桔皮': 4,
              '漏底': 5,
              '碰伤': 6,
              '起坑': 7,
              '凸粉': 8,
              '涂层开裂': 9,
              '脏点': 10,
              '其他': 11,
              }

# train data
data_train = 'data/guangdong_round1_train2_20180916'
data_val = "data/guangdong_round1_train1_20180903"
train_img, train_label = [], []
val_img, val_label = [], []


###############################################################
# train 样本
###############################################################

all_dir = []

for root, dirs, files in os.walk(data_train, topdown=False):
    #for name in files:
    #    print(os.path.join(root, name))
    for name in dirs:
        all_dir.append(os.path.join(root, name))

#print(all_dir)

for dd in all_dir:
   for img in os.listdir(dd):
       print(dd+"/"+img) 
       full_path = dd+'/'+img     
       if '无瑕疵样本' in full_path and img.endswith(".jpg"):
            train_img.append(full_path)
            train_label.append('正常')
       elif "output" in full_path and img.endswith(".jpg"):
            train_img.append(full_path)
            train_label.append(full_path.split('/')[-3])     
            
       elif img.endswith(".jpg"):
            train_img.append(full_path)
            train_label.append(full_path.split('/')[-2])     

label_file = pd.DataFrame({'img_path': train_img, 'label': train_label})
label_file['label'] = label_file['label'].map(label_warp)

label_file.to_csv('data/train.csv', index=False)
            

'''
for first_path in os.listdir(data_train):
    first_path = osp.join(data_train, first_path)
    if '无瑕疵样本' in first_path:
        for img in os.listdir(first_path):
          if img.endswith(".jpg"):
            train_img.append(osp.join(first_path, img))
            train_label.append('正常')
    else:
        for second_path in os.listdir(first_path):
            #print(second_path)
            defect_label = second_path
            second_path = osp.join(first_path, second_path)
            if defect_label != '其他':
                for img in os.listdir(second_path):
                    if img.endswith(".jpg"):
                       train_img.append(osp.join(second_path, img))
                       train_label.append(defect_label)
            else:
                for third_path in os.listdir(second_path):
                    
                    third_path = osp.join(second_path, third_path)
                    print(third_path)
                    if osp.isdir(third_path):
                        for img in os.listdir(third_path):
                            if 'DS_Store' not in img and img.endswith(".jpg"):
                               train_img.append(osp.join(third_path, img))
                               train_label.append(defect_label)

label_file = pd.DataFrame({'img_path': train_img, 'label': train_label})
label_file['label'] = label_file['label'].map(label_warp)

label_file.to_csv('data/train.csv', index=False)
'''
###############################################################
# val 样本
###############################################################
def f(str_):
    for i in range(len(str_)):
        if str_[i].isdigit():
           return i
    return -1

for first_path in os.listdir(data_val):
    
    if first_path.endswith('.jpg'):
       path = first_path
       first_path = osp.join(data_val, first_path)
       
       #print(path)
       if path[:f(path)] in label_warp:
             val_img.append(first_path)
             val_label.append(label_warp[path[:f(path)]])
       else:
             val_img.append(first_path)
             val_label.append(11)
#print(val_label)
label_file = pd.DataFrame({'img_path': val_img, 'label': val_label})

label_file.to_csv('data/val.csv', index=False)

###############################################################
# test
###############################################################
# test data
test_data_path = 'data/guangdong_round1_test_a_20180916'
all_test_img = os.listdir(test_data_path)
test_img_path = []

for img in all_test_img:
    if osp.splitext(img)[1] == '.jpg':
        test_img_path.append(osp.join(test_data_path, img))

test_file = pd.DataFrame({'img_path': test_img_path})
test_file.to_csv('data/test.csv', index=False)
 
