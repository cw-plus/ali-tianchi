#!/usr/bin/env sh
set -e

../build/tools/caffe train \
    --solver=resnet101_solver_adam.prototxt --gpu 0 --weights=ResNet-101-model.caffemodel
$@
