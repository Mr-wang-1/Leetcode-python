# 关于python 中 collectionmo模块的学习

from collections import *

# 命名元组(namedtuple)是元组和字典的混合体，他赋予每个元素含义(字典的特性)，而且元素不可修改(元组的特性)
# 创建命名元组需要设定两个必须参数：元组名称，字段名称
# Final Product  FP

FP=namedtuple('FP',['assect','instrument'])
print(FP)                 #<class '__main__.FP'>

product = FP('FX','European Option')
print(product)            #FP(assect='FX', instrument='European Option')




