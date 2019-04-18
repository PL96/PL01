#作业4：绘制各种学过的图形
import pygame,sys
import math
import random
from pygame.locals import*    #导入模块

pygame.init()                 #初始化
screen=pygame.display.set_mode((990,800))#设置窗口的大小
pygame.display.set_caption("绘制各种所学过的图形")
screen.fill((0,0,255))#填充窗口颜色

#绘制线条
for i in range(10):
    if i<=10:
        color=random.randint(0,255),random.randint(0,255),random.randint(0,255)#颜色
        width=random.randint(1,10)#填充
        start_angle=random.randint(0,900),random.randint(0,900)#起点坐标
        end_angle=random.randint(0,800),random.randint(0,800)  #终点坐标
        pygame.draw.line(screen,color,start_angle,end_angle,width) #画线条
    else:
        break
       
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
   

    color1=(255,255,0)         #圆的颜色
    position1=(100,100)         #圆的位置
    radius=100                 #圆的直径
    width1=10                   #圆的实体填充
    pygame.draw.circle(screen,color1,position1,radius,width1)
    


    #绘制矩形
    color2=(100,255,0)       #矩形颜色
    width2=10
    position2=(200,200,150,150)#矩形位置
    pygame.draw.rect(screen,color2,position2,width2)
    #绘制弧形
    color3=(5,5,5)
    position3=(350,350,150,150)
    start_angle=math.radians(0)
    end_angle=math.radians (180)
    width3=10
    pygame.draw.arc(screen,color3,position3,start_angle,end_angle,width3)
    #绘制一跟平滑的线
    color4=(20,90,240)#  线的颜色
    start=(400,400)
    end=(800,800)
    width4=10
    pygame.draw.ellipse(screen, (128, 0,128), ((450, 450), (300, 200)), 0)
    
    pygame.display.update()

pygame.quit()







    
