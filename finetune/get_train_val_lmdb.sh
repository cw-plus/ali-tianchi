#!/bin/bash
# convert images to lmdb
 

# 图片大小2560*1920

DATA=.
rm -rf $DATA/img_train_lmdb
echo $DATA/
../build/tools/convert_imageset --shuffle=true  $DATA/  --resize_height=300 --resize_width=300 train.txt  $DATA/img_train_lmdb

#  我们需要提供三个路径 分别是                                                原始图片数据存放路径、图片路径txt 和生成的lmdb文件存放路径：   



#!/bin/bash
# convert images to lmdb
 

DATA=.
rm -rf $DATA/img_val_lmdb
echo $DATA/
../build/tools/convert_imageset --shuffle=true $DATA/ --resize_height=225 --resize_width=225  val.txt  $DATA/img_val_lmdb

#  我们需要提供三个路径 分别是                                                原始图片数据存放路径、图片路径txt 和生成的lmdb文件存放路径：                                                       
                                                    

