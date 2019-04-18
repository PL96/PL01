'''
20161152092
杨普伦
'''
#绘制数据样本散点图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None) # 加载Iris数据集作为DataFrame对象
X = df.iloc[:, [0, 2]].values # 取出2个特征，并把它们用Numpy数组表示

plt.scatter(X[:50, 0], X[:50, 1],color='red', marker='o', label='setosa') # 前50个样本的散点图
plt.scatter(X[50:100, 0], X[50:100, 1],color='blue', marker='x', label='versicolor') # 中间50个样本的散点图
plt.scatter(X[100:, 0], X[100:, 1],color='green', marker='+', label='Virginica') # 后50个样本的散点图
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc=2) # 把说明放在左上角，
plt.show()        #显示
