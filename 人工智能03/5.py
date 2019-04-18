
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd

from sklearn import datasets,linear_model
x_parameter=[[150],[200],[250],[300],[350],[400],[600]]
y_parameter=[6450,7450,8450,9450,11450,15450,18450]
print(x_parameter)
print(y_parameter)

def linear_model_main(x_parameter,y_parameter,predict_value):#定义x_参数，y_参数，及预测值
    regr=linear_model.LinearRegression()                     #定义一个线性回归对象
    regr.fit(x_parameter,y_parameter)
    predict_outcome=regr.predict(predict_value)             #预测结果

    predictions={}                                           #预言
    predictions['intercept']=regr.intercept_                 #拦截
    predictions['coefficient'] = regr.coef_                  #系数
    predictions['predicted_value'] = predict_outcome
    return predictions
predict_squre=700                                            #预测的值
result=linear_model_main(x_parameter,y_parameter,predict_squre)
def show_linear_line(X_parameters,Y_parameters):
    #创建线性回归对象
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()
