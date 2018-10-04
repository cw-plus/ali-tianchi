#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

DATA=.
TOOLS=../build/tools

$TOOLS/compute_image_mean /home/wangchao/ali-competition/caffe/data/img_train_lmdb/ \
  /home/wangchao/ali-competition/caffe/data/img_train_lmdb/imagenet_mean.binaryproto

$TOOLS/compute_image_mean /home/wangchao/ali-competition/caffe/data/img_val_lmdb/ \
    /home/wangchao/ali-competition/caffe/data/img_val_lmdb/imagenet_mean.binaryproto



echo "Done."
