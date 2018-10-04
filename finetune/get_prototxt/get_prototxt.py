# coding:utf-8
import sys
sys.path.insert(0, "/home/wangchao/ali-tianchi/caffe/python")

caffe_root = '/home/wangchao/ali-tianchi/caffe/'
sys.path.append(caffe_root+'python')

import caffe
 
import caffe.proto.caffe_pb2 as caffe_pb2# 载入caffe.proto编译生成的caffe_pb2文件
 
# 载入模型
caffemodel_filename = '/home/wangchao/ali-tianchi/caffe/finetune/get_prototxt/se_resnet_50_v1.caffemodel'



#stage3:对照着caffe.proto，把一些参数的默认值过滤掉，以及blobs过滤掉。
#开始解析ZFnet:运用在faster rcnn的模型

# 载入模型，根据网络结构模型，结合caffemodel，生成prototxt文件
 
model = caffe_pb2.NetParameter()

f = open(caffemodel_filename, 'rb')
model.ParseFromString(f.read())
f.close()

layers = model.layer
# print 'name: ' + model.name#name: ImageNet_Zeiler_spm
layer_id=-1

result_file='SE-ResNet-50.prototxt'

for layer in layers:#遍历每一层
    layer_id = layer_id + 1

    res = list()

    # name
    res.append('layer {')
    res.append('  name: "%s"' % layer.name)

    # type
    res.append('  type: "%s"' % layer.type)

    # bottom
    for bottom in layer.bottom:
        res.append('  bottom: "%s"' % bottom)

    # top
    for top in layer.top:
        res.append('  top: "%s"' % top)

    # loss_weight
    for loss_weight in layer.loss_weight:
        res.append('  loss_weight: ' + loss_weight)

    # param
    for param in layer.param:
        param_res = list()
        if param.lr_mult is not None:
            param_res.append('    lr_mult: %s' % param.lr_mult)
        if param.decay_mult != 1:
            param_res.append('    decay_mult: %s' % param.decay_mult)
        if len(param_res) > 0:
            res.append('  param{')
            res.extend(param_res)
            res.append('  }')

    # lrn_param
    if layer.lrn_param is not None:
        lrn_res = list()
        if layer.lrn_param.local_size != 5:#这个值应该是默认值，如果不等于这个默认值的话，那么就需要添加
            lrn_res.append('    local_size: %d' % layer.lrn_param.local_size)
        if layer.lrn_param.alpha != 1:
            lrn_res.append('    alpha: %f' % layer.lrn_param.alpha)
        if layer.lrn_param.beta != 0.75:
            lrn_res.append('    beta: %f' % layer.lrn_param.beta)
        NormRegionMapper = {'0': 'ACROSS_CHANNELS', '1': 'WITHIN_CHANNEL'}
        if layer.lrn_param.norm_region != 0:
            lrn_res.append('    norm_region: %s' % NormRegionMapper[str(layer.lrn_param.norm_region)])
        EngineMapper = {'0': 'DEFAULT', '1': 'CAFFE', '2': 'CUDNN'}
        if layer.lrn_param.engine != 0:
            lrn_res.append('    engine: %s' % EngineMapper[str(layer.lrn_param.engine)])
        if len(lrn_res) > 0:
            res.append('  lrn_param{')
            res.extend(lrn_res)
            res.append('  }')

    # include
    if len(layer.include) > 0:
        include_res = list()
        includes = layer.include
        phase_mapper = {
            '0': 'TRAIN',
            '1': 'TEST'
        }

        for include in includes:
            if include.phase is not None:
                #include_res.append('    phase: ', phase_mapper[str(include.phase)])
                include_res.append('    phase: '+phase_mapper[str(include.phase)])


        if len(include_res) > 0:
            res.append('  include {')
            res.extend(include_res)
            res.append('  }')

    # transform_param
    if layer.transform_param is not None:
        transform_param_res = list()
        if layer.transform_param.scale != 1:
            transform_param_res.append('    scale: %s' % layer.transform_param.scale)
        if layer.transform_param.mirror != False:
            transform_param_res.append('    mirror: ' + layer.transform_param.mirror)
        if len(transform_param_res) > 0:
            res.append('  transform_param {')
            res.extend(transform_param_res)
            res.append('  }')

    # data_param
    if layer.data_param is not None and (
                layer.data_param.source != "" or layer.data_param.batch_size != 0 or layer.data_param.backend != 0):
        data_param_res = list()
        if layer.data_param.source is not None:
            data_param_res.append('    source: "%s"' % layer.data_param.source)
        if layer.data_param.batch_size is not None:
            data_param_res.append('    batch_size: %d' % layer.data_param.batch_size)
        if layer.data_param.backend is not None:
            data_param_res.append('    backend: %s' % layer.data_param.backend)

        if len(data_param_res) > 0:
            res.append('  data_param: {')
            res.extend(data_param_res)
            res.append('  }')

    # convolution_param
    if layer.convolution_param is not None:
        convolution_param_res = list()
        conv_param = layer.convolution_param
        if conv_param.num_output != 0:
            convolution_param_res.append('    num_output: %d' % conv_param.num_output)
        if len(conv_param.kernel_size) > 0:
            for kernel_size in conv_param.kernel_size:
                convolution_param_res.append('    kernel_size: %d' % kernel_size)
        if len(conv_param.pad) > 0:
            for pad in conv_param.pad:
                convolution_param_res.append('    pad: %d' % pad)
        if len(conv_param.stride) > 0:
            for stride in conv_param.stride:
                convolution_param_res.append('    stride: %d' % stride)
        if conv_param.weight_filler is not None and conv_param.weight_filler.type != 'constant':
            convolution_param_res.append('    weight_filler {')
            convolution_param_res.append('      type: "%s"' % conv_param.weight_filler.type)
            convolution_param_res.append('    }')
        if conv_param.bias_filler is not None and conv_param.bias_filler.type != 'constant':
            convolution_param_res.append('    bias_filler {')
            convolution_param_res.append('      type: "%s"' % conv_param.bias_filler.type)
            convolution_param_res.append('    }')

        if len(convolution_param_res) > 0:
            res.append('  convolution_param {')
            res.extend(convolution_param_res)
            res.append('  }')

    # BatchNorm_param
    if layer.batch_norm_param is not None:
        convolution_param_res = list()
        conv_param = layer.batch_norm_param

        res.append('  batch_norm_param {') 
        res.append('     use_global_stats: false') 
        res.append('  }')

    
    # pooling_param
    if layer.pooling_param is not None:
        pooling_param_res = list()
        if layer.pooling_param.kernel_size > 0:
            pooling_param_res.append('    kernel_size: %d' % layer.pooling_param.kernel_size)
            pooling_param_res.append('    stride: %d' % layer.pooling_param.stride)
            pooling_param_res.append('    pad: %d' % layer.pooling_param.pad)
            PoolMethodMapper = {'0': 'MAX', '1': 'AVE', '2': 'STOCHASTIC'}
            pooling_param_res.append('    pool: %s' % PoolMethodMapper[str(layer.pooling_param.pool)])

        if len(pooling_param_res) > 0:
            res.append('  pooling_param {')
            res.extend(pooling_param_res)
            res.append('  }')

    # inner_product_param
    if layer.inner_product_param is not None:
        inner_product_param_res = list()
        if layer.inner_product_param.num_output != 0:
            inner_product_param_res.append('    num_output: %d' % layer.inner_product_param.num_output)

        if len(inner_product_param_res) > 0:
            res.append('  inner_product_param {')
            res.extend(inner_product_param_res)
            res.append('  }')

    # drop_param
    if layer.dropout_param is not None:
        dropout_param_res = list()
        # if layer.dropout_param.dropout_ratio != 0.5 or layer.dropout_param.scale_train != True:
        if layer.dropout_param.dropout_ratio != 0.5:
            dropout_param_res.append('    dropout_ratio: %f' % layer.dropout_param.dropout_ratio)
            # dropout_param_res.append('    scale_train: ' + str(layer.dropout_param.scale_train))

        if len(dropout_param_res) > 0:
            res.append('  dropout_param {')
            res.extend(dropout_param_res)
            res.append('  }')

    res.append('}')

    with open(result_file, 'a+') as fd:
        for line in res:
            # print line
            fd.writelines('\n'+line)
 

