


import tushare as ts
import sys
print("---------------------第一题---------------")
print("利用numpy ，创建2个3*3的数组，并完成2个数组的加减乘除运算。")

import numpy as np  #导入模块
A1=np.array([[1,2,3],[4,5,6],[7,8,9]])           #定义两个数组
A2=np.array([[10,11,12],[13,14,15],[16,17,18]])
print(A1+A2)
print(A1-A2)
print(A1*A2)
print(A1/A2)

print("---------------------第二题------------------")
print("创建一个5*2和2*5的矩阵，完成两个矩阵相乘，并查看矩阵结构")
B1=np.arange(10).reshape(5,2)
B1=np.mat(B1)
print(B1)
B2=np.arange(10).reshape(2,5)
B2=np.mat(B2)
print(B2)
print(B1*B2)
print(B2*B1)
print("----------------------第三题---------------------")
print("利用numpy ，创建一个4*4的随机数矩阵")
C=(np.random.rand(4,4))
print(C)
print("-----------------------第四题---------------------")
print("求该矩阵的逆矩阵")
import numpy.linalg as nlg
D=np.mat(C)
print(D)
D1=nlg.inv(D)
print("inverse of D")
print(D1)
print("c*inv(D)")
print(D*D1)
print("------------------------第五题---------------------:")
print("求出该矩阵的特征值、特征向量")
eig_value,eig_vector=nlg.eig(C)
print("特征值:")
print(eig_value)
print("特征向量:")
print(eig_vector)
print("------------------------第六题---------------------")
print("生成10个series，每个series包含10个随机数。并将这10个series构造成一个dataFrame")
from pandas import Series,DataFrame
E={}
for i in range(10):
    E[i]=np.random.randn(10)
df=DataFrame(E)
print(df)
print("-----------------------第七题----------------------")
print("获取该dataFrame中一个4*4的正方形数据切片。")
print(df[0:4])
print("-----------------------第八题----------------------")

print("-----------------------第九题----------------------")
print("找出中国资产总额最大的20家上市公司")
import numpy as np 
dt = ts.get_stock_basics()
print(dt)
print(dt.sort_values('totals',ascending=0).head(20))
print("-----------------------第十题-----------------------")
print("找出中国“地产行业”的上市公司的数量")
print(dt[dt['industry']=='全国地产'].count())
print("-----------------------第十一------------------------")
print("找出中国“地产行业” 资产总额最大的10家上市公司")
db=(dt[dt['industry']==('全国地产' or '区域地产')])
print(db.sort_values('totals',ascending=0).head(10))
print("----------------------第十五题------------------------")
print("通过接口获得“云南城投”2016、2017年的月线数据，并以时间、收盘价、成交量绘图。将收盘价、成交量的曲线叠加显示。")
df = ts.get_k_data('600239',ktype='M',start='2016-01-01',end='2017-12-31')
print(df)








