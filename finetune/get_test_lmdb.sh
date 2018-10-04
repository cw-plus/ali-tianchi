#!/bin/bash
# convert images to lmdb
 

DATA=./
rm -rf $DATA/img_test_lmdb
echo $DATA/
../build/tools/convert_imageset $DATA/  --resize_height=224 --resize_width=224 test.txt  $DATA/img_test_lmdb

#  我们需要提供三个路径 分别是                                                原始图片数据存放路径、图片路径txt 和生成的lmdb文件存放路径：                                                       

