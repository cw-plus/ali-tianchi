//新加层头文件：diff_cutoff_layer.hpp
//*****************************************
#ifndef CAFFE_DIFFCUTOFF_LAYER_HPP_
#define CAFFE_DIFFCUTOFF_LAYER_HPP_
//*****************************************

#include <vector>
#include "caffe/blob.hpp"
#include "caffe/layer.hpp"
#include "caffe/proto/caffe.pb.h"

//*****************************************
#include "caffe/layers/neuron_layer.hpp"
//*****************************************

namespace caffe {

template <typename Dtype>
//******以后我们层的type: "DiffCutoff" *******
  class DiffCutoffLayer : public NeuronLayer<Dtype> {
//*****************************************
  public:
    explicit DiffCutoffLayer(const LayerParameter& param) : NeuronLayer<Dtype>(param) {}
    virtual void LayerSetUp(const vector<Blob<Dtype>*>& bottom, const vector<Blob<Dtype>*>&top);

//****我们只需要一个bottom和一个top*****
    virtual inline int ExactNumBottomBlobs() const { return 1; }

//******以后我们层的type: "DiffCutoff" *******
    virtual inline const char* type() const { return "DiffCutoff"; }

  protected:
//******这里只写了CPU功能，故删掉了原本的GPU函数 *******
    virtual void Forward_cpu(const vector<Blob<Dtype>*>& bottom, const vector<Blob<Dtype>*>& top);
    virtual void Backward_cpu(const vector<Blob<Dtype>*>& top,const vector<bool>& propagate_down, const vector<Blob<Dtype>*>& bottom);

//  *****定义一个Dtype型的标量，用来存储梯度放缩倍数***
     Dtype diff_scale;
    };
} 
#endif 

