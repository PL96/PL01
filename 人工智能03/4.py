'''
绘制直线函数上的5个蓝色圆点，
并为5个点增加Y轴方向上的随机误差。
并利用线性模型对这5个点进行拟合。
'''
print("---------------第四题----------------------")
import numpy as np
import matplotlib.pyplot as plt
import random  #导入随机函数库
#数据量
SIZE=5
#纵轴数据。np.linspace返回一个一维数组,SIZE指定数组长度。
#数组最小值是2，最大值是18，所有元素间隔相等，整个数组是
#等差数列
Y=np.linspace(2,18,SIZE)
#横向数据
X=np.linspace(1,9,SIZE)

fig=plt.figure() #创建图表       
#画图区域分成一行一虐，选择第一块区域
ax1=fig.add_subplot(1,1,1)
#标题
ax1.set_title("yangpulun")
#让散点随机增加
random_x=[]
random_y=[]
for i in range(SIZE):
    random_x.append(X[i]+random.uniform(-1,1))
for i in range(SIZE):
    random_y.append(Y[i]+random.uniform(-1,1))
RANDOM_X=np.array(random_x)#散点图的横轴
RANDOM_Y=np.array(random_y)#散点图的纵轴

#画散点图
ax1.scatter(RANDOM_X,RANDOM_Y)
ax1.set_xlabel("x")
# 纵轴名称。
ax1.set_ylabel("y")

#直线图
ax1.plot(X,Y)
plt.show()  #显示所有图表















