#coding:utf-8
import numpy as np
import os
import sys
import cv2
import csv
caffe_root = '/home/wangchao/ali-tianchi/'
sys.path.append(caffe_root+'python')
 
#导入进度条
from tqdm import tqdm

import caffe
#caffe.set_device(0)
#caffe.set_mode_gpu()

model_def = 'deploy.prototxt'
model_weights = 'resnet101_solver_adam_iter_90000.caffemodel'
net = caffe.Net(model_def, 'models/'+model_weights, caffe.TEST)
#net.blobs['data'].reshape(1,3,h,w) # (batch_size,c,h,w)
net.blobs['data'].reshape(1,3,224,224) # (batch_size,c,h,w)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # (h,w,c)--->(c,h,w)
transformer.set_mean('data', np.array([104,117,123])) #注意是 BGR

transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))# RGB--->BGR

'''
可能你对均值设置成BGR有疑问，不是到后面才把RGB转为BGR吗?
其实transformer.setXXX()这些只是设置属性，实际执行顺序是参考附录preprocess函数定义
'''


with open("test.txt","r") as f:
    image_names = f.readlines()
  
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
submit = ['norm','defect1','defect2','defect3','defect4','defect5','defect6','defect7','defect8','defect9','defect10','defect11']



cnt = 0
pbar = tqdm(total=440)


with open('submit.txt','w') as f: 
  for image_name in image_names:
      pbar.update(1)
      cnt = cnt+1  
      image_name = image_name.strip()
      image = caffe.io.load_image(image_name)# 用的是skimage库，见附录
      # 利用刚刚的设置进行图片预处理
      transformed_image = transformer.preprocess('data', image)
      net.blobs['data'].data[...] = transformed_image
      # 网络前传（测试无后传）
      output = net.forward()
 

      output_prob= output['prob'][0].argmax()  # 概率最大的label
      #image_name,output_prob)#
      #print (output_prob)      
      f.write(image_name.split("/")[-1]+',' + submit[output_prob]+'\n')
	  
os.rename('submit.txt', 'submit.csv')

pbar.close()

'''
标签对照表
正常-norm 不导电-defect1 擦花-defect2 横条压凹-defect3 桔皮-defect4 漏底-defect5 碰伤-defect6
起坑-defect7 凸粉-defect8 涂层开裂-defect9 脏点-defect10 其他-defect11
name_list = ['zhengchang','budaodian', 'cahua', 'hengtiaoyaao', 'jiepi', 'loudi', 'pengshang', 'qikeng', 'tufen', 'tucengkailie', 'zangdian', 'qita']
            ['norm','defect1','defect2','defect3','defect4','defect5','defect6','defect7','defect8','defect9','defect10','defect11',]

'''






'''
正常	norm
不导电	defect1
擦花	defect2
横条压凹	defect3
桔皮	defect4
漏底	defect5
碰伤	defect6
起坑	defect7
凸粉	defect8
涂层开裂	defect9
脏点	defect10
其他	defect11
'''
