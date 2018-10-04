
首先，我在参加[天池比赛](https://tianchi.aliyun.com/competition/introduction.htm?spm=5176.11165268.5678.1.3d8410c5H0TIaC&raceId=231682)

想在SENet上进行finetune，prototxt可以在[这里找到](https://github.com/hujie-frank/SENet/issues/8),数据集是比赛提供的。

我修改后的prototxt在我的github上可以找到，其中数据层是将图片直接输入网络，并且做了一些镜像、颜色、亮度、缩放的变换增加数据量，文件里测试部分没有用，可以删掉。不删也不影响训练，后面有一个用来测试的prototxt文件。 
类别数在最后的全连接层fc层，将类别数量改为所需的12即可。 

SE-BN-Inception_t2.prototxt 是训练时用的，下面修改下用于推断，命名为 deploy.prototxt

注意点：
```
在finetune Resnet时，网络结构文件中BatchNorm层的参数要注意： 
1.在训练时所有BN层要设置use_global_stats: false（也可以不写，caffe默认是false） 
2.在测试时所有BN层要设置use_global_stats: true

影响： 
1.训练如果不设为false，会导致模型不收敛 
2.测试如果不设置为true，会导致准确率极低 

区别： 
use_global_stats: false是使用了每个Batch里的数据的均值和方差； 
use_global_stats: true是使用了所有数据的均值和方差。
```

参考这个，很不错： https://blog.csdn.net/tangwenbo124/article/details/56070322/

预训模型：SENet [下载地址](https://github.com/hujie-frank/SENet)

模型现在精度：

| 日期 | 模型 | 精度 |
| ------ | ------ | ------ |
| 2018.09.29 | SENet | 0.79 |
| 2018.09.30 | SENet | - |
