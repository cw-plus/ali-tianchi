# Caffe
 
## 1. 新增加常见[数据增强方式](https://github.com/twtygqyy/caffe-augmentation)

2018.10.07 新增

- min_side - resize and crop preserving aspect ratio, default 0 (disabled);

- max_rotation_angle - max angle for an image rotation, default 0;

- contrast_brightness_adjustment - enable/disable contrast adjustment, default false;

- smooth_filtering - enable/disable smooth filterion, default false;

- min_contrast - min contrast multiplier (min alpha), default 0.8;

- max_contrast - min contrast multiplier (max alpha), default 1.2;

- max_brightness_shift - max brightness shift in positive and negative directions (beta), default 5;

- max_smooth - max smooth multiplier, default 6;

- max_color_shift - max color shift along RGB axes

- apply_probability - how often every transformation should be applied, default 0.5;

- debug_params - enable/disable printing tranformation parameters, default false;



使用方法：

在网络的 prototxt 指定：

```
layer {
name: "data"
type: "ImageData"
top: "data"
top: "label"
include {
  phase: TRAIN
}
transform_param {
    mirror: true
    contrast_brightness_adjustment: true
    smooth_filtering: true
    min_side_min: 256
    min_side_max: 480
    crop_size: 224
    mean_file: "imagenet_mean.binaryproto"
    min_contrast: 0.8
    max_contrast: 1.2
    max_smooth: 6
    apply_probability: 0.5
    max_color_shift: 20
    debug_params: false
}
image_data_param {
  source: "train_list.txt"
  batch_size: 64
}
}

在测试(testing phase)时 :

layer {
name: "data"
type: "ImageData"
top: "data"
top: "label"
include {
  phase: TEST
}
transform_param {
    mirror: false
    min_side: 256
    crop_size: 224
    mean_file: "imagenet_mean.binaryproto"
}
image_data_param {
  source: "test_list.txt"
  batch_size: 32
}
}
```








### 坚持参加天池比赛，为春招做准备

#### 1. [2018广东工业智造大数据创新大赛——智能算法赛](https://tianchi.aliyun.com/competition/introduction.htm?spm=5176.100150.711.5.322c2784ctjRFB&raceId=231682) 

### 2. 


















## License and Citation

Caffe is released under the [BSD 2-Clause license](https://github.com/BVLC/caffe/blob/master/LICENSE).
The BAIR/BVLC reference models are released for unrestricted use.

Please cite Caffe in your publications if it helps your research:

    @article{jia2014caffe,
      Author = {Jia, Yangqing and Shelhamer, Evan and Donahue, Jeff and Karayev, Sergey and Long, Jonathan and Girshick, Ross and Guadarrama, Sergio and Darrell, Trevor},
      Journal = {arXiv preprint arXiv:1408.5093},
      Title = {Caffe: Convolutional Architecture for Fast Feature Embedding},
      Year = {2014}
    }
