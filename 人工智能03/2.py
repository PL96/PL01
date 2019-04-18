print("------第二题--------")
print("100名学生成绩，课1均值70，方差为5，课2均值为60，方差为10")
#导入库
import matplotlib.pyplot as plt
import numpy as np
n =100  # 班级人数
X = np.random.normal(70,5,n) # 课程1 的均值70，方差为5，
Y = np.random.normal(60,10,n) # 课程2的均值为60，方差为10
T = np.arctan2(Y,X) # for color value
plt.scatter(X, Y, s=55, c=T, alpha=0.5)
plt.xlim(0,120)
plt.ylim(0,120)
plt.show()
