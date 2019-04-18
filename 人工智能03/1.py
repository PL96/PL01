print("-----------------第一题-----------------")
print("利用matplotlib绘制直线与抛物线，并显示图例")
#导入库
import matplotlib.pyplot as plt
import numpy as np
data=[]
x=np.linspace(-1,2,50)#从-1到2的50个点
y1=2*x+1              #设置一个函数y1
y2=x**2               #设置一个函数y2


plt.figure(num=1,figsize=(8,5))  #图像的页面名称及长和宽
plt.plot(x,y2,color='red',linewidth=1,linestyle='--')#对y2函数填充红色，线条宽为1，风格为'--'
plt.plot(x,y1)
plt.xlim((-1,2))    #设置坐标轴
plt.ylim((-2,3))
plt.xlabel("l am x")#调整名字
plt.ylabel("l am y")
 
new_ticks=np.linspace(-1,2,10)  #调整间隔
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1,3],
         [r'$a$',r'$b$',r'$c$',r'$d$',r'$e$'])
plt.show()




















