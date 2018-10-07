//创建 diff_cutoff_layer.cpp 文件
#include <algorithm>
#include <vector>

//*****************************************
// 我们定义的头文件
#include "caffe/layers/diff_cutoff_layer.hpp"
//*****************************************

#include "caffe/util/math_functions.hpp"
namespace caffe {

  template <typename Dtype>
  void DiffCutoffLayer<Dtype>::LayerSetUp(
    const vector<Blob<Dtype>*>& bottom, const vector<Blob<Dtype>*>& top) {
    NeuronLayer<Dtype>::LayerSetUp(bottom, top);

 // 因为对前向传播不修改，因此top的shape应和bottom的shape相同
    top[0]->Reshape(bottom[0]->shape()); 
  }

  template <typename Dtype>
  void DiffCutoffLayer<Dtype>::Forward_cpu(const vector<Blob<Dtype>*>& bottom,
    const vector<Blob<Dtype>*>& top) {

 // 前向传播直接将bottom的数据copy到top
    const int count = top[0]->count();
    caffe_copy(count, bottom[0]->cpu_data(), top[0]->mutable_cpu_data());
    // mutable_cpu_data() 要改变的数据用 mutable 的 cpu 或者 gpu
  }

  template <typename Dtype>
  void DiffCutoffLayer<Dtype>::Backward_cpu(const vector<Blob<Dtype>*>& top,const vector<bool>& propagate_down, const vector<Blob<Dtype>*>& bottom) {

    const int count = top[0]->count();
    const Dtype* top_diff = top[0]->cpu_diff();

    //读取我们实际指定的梯度放缩倍数，注意我们的参数名为diff_scale
    diff_scale= this->layer_param_.diff_cutoff_param().diff_scale();

    // 如果bottom前向传播完成，我们就把top的diff放缩后赋给bottom的diff
    if (propagate_down[0]) {
      Dtype* bottom_diff = bottom[0]->mutable_cpu_diff();

      caffe_cpu_axpby(count,diff_scale,top_diff,Dtype(0),bottom_diff);
     
     // 完成的功能是 对梯度缩放，如下式所示：
     // bottom_diff = diff_scale * top_diff + Dtype(0) * bottom_diff


    }  
  }

#ifdef CPU_ONLY
  STUB_GPU(DiffCutoffLayer);
#endif

  INSTANTIATE_CLASS(DiffCutoffLayer); //注册
  REGISTER_LAYER_CLASS(DiffCutoff);
}
