#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import Augmentor


dir_all = set()
for root, dirs, files in os.walk("./guangdong_round1_train1_20180903/", topdown=False):
    for name in files:
        #if "output" in os.path.join(root, name):
        #   continue
        #if "train" not in os.path.join(root, name):
        #   continue
        print(os.path.join(root, name))
        if os.path.join(root, name).endswith(".jpg"):
           len1 = os.path.join(root, name).rfind('/')
           dir_all.add(os.path.join(root, name)[:len1])
            
    # for name in dirs:
        # print(os.path.join(root, name))

print(dir_all)


'''
# # dir = '.\\2\\2_2'
# # aa = [lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]
# # #print([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))])
# # print(len(aa))

# for dir in dir_all:
    # # Initialised with 100 images found in selected directory
    # p = Augmentor.Pipeline(dir)
    # p.random_erasing(probability=1,rectangle_area=0.2)
    # len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))])
    # p.sample(len1*2) #总图像扩增为原来的5倍
	


# for dir in dir_all:
    # p=Augmentor.Pipeline(dir)

    # p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)

    # p.rotate(probability=1,max_right_rotation=10,max_left_rotation=10)
    # len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))])
    # p.sample(len1*2) #总图像扩增为原来的5倍

	
for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)
    p.skew_tilt(probability=0.7)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍

for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)
    #这两个要结合起来
    #p.skew_tilt(probability=0.7)
    p.flip_left_right(probability=0.99)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍


for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)    
    #p.skew_tilt(probability=0.7)
    p.flip_top_bottom(probability=1.0)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍
for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)    
    p.skew_tilt(probability=0.3)
    p.flip_random(probability=0.3)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍
  


for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.random_distortion(probability=0.3,grid_width=5, grid_height=5, magnitude=2)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍


for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.rotate_random_90(probability=1.0)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍

for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.rotate270(probability=0.7)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍

for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.shear(probability=0.7, max_shear_left = 10, max_shear_right=10)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍

for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍
 
for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.crop_centre(probability=0.9,percentage_area=0.8)
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍

for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.crop_by_size(probability=0.7,width=2000, height=1000)  
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍

for dir in dir_all:
    # Initialised with 100 images found in selected directory
    p = Augmentor.Pipeline(dir)  
    p.crop_random(probability=0.7,percentage_area=0.7)  
    len1 = len([lists for lists in os.listdir(dir) if os.path.isfile(os.path.join(dir, lists))]) 
    p.sample(len1*2) #总图像扩增为原来的5倍
'''

