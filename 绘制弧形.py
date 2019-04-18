#绘制弧形
import math        #导入数学库、
import pygame ,sys #导入sys库
from pygame.locals import*
pygame.init()      #初始化
screen=pygame.display.set_mode((600,500))#设置窗口的大小
pygame.display.set_caption("绘制弧形")   #设置标题
while True:
    for event in pygame.event.get():     #遍历所有事件
        if event .type in (QUIT,KEYDOWN):#如果单击则退出
            sys.exit()
    screen.fill((0,0,200))               #填充窗口颜色
    #-----------绘制弧形----------
    color=(255,0,255)                    #设置颜色
    position=(200,150,200,200)           #位置
    start_angle=math.radians(0)          #起始点
    end_angle=math.radians(180)          #终始点
    width=8
    pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
    pygame.display.update()                      #刷新
        

