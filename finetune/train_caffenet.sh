#!/usr/bin/env sh
set -e

../build/tools/caffe train \
    --solver=/home/wangchao/ali-tianchi/caffe/finetune/resnet101_solver_adam.prototxt --gpu 0 --weights=/home/wangchao/ali-tianchi/caffe/finetune/ResNet-101-model.caffemodel
$@
