# -*- coding: utf-8 -*-

import os
from xpinyin import Pinyin
p = Pinyin()

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
       print(name)
       tmp = p.get_pinyin(os.path.join(root, name),"")
       print(tmp)
       if(name.endswith('.jpg')): #排除不相关的文件名 
          os.renames(os.path.join(root, name),tmp)
		  
#os.renames(file,newname1)  
		  
# assert len(labels) == len(path) ,'注意检查 if(name != get_labels.py" and name != "labels.txt")'
# assert len(labels) == 250


# # print(labels)
# # print(path)

