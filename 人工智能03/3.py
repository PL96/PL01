print("-------------第三题---------------")
print("绘制直线函数上的5个蓝色圆点，并绘制这条直线（红色虚线）穿过5个点")
import numpy as np
import matplotlib.pyplot as plt
x= np.arange(1,10,2).reshape(-1,1)
y = 2*x               #函数
plt.plot(x,y,'r-',linewidth=2, linestyle="--",label=u"线性拟合")#用红色进行标记
plt.plot(x,y, 'bo')   #用蓝色圆圈标记
plt.show()            #显示绘画的图像
