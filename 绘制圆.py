#绘制圆

import pygame,sys           #导入sys模块
from pygame.locals import*
pygame.init()                  #初始化
screen=pygame.display.set_mode((600,500))                   #设置窗口的大小
pygame.display.set_caption("绘制圆")#设置标题
#执行死循环，确保窗口一直显示
while True:
    for event in pygame.event.get():                        #遍历所有事件
        if event.type in (QUIT,KEYDOWN):                    #如果单击窗口则退出
            sys.exit()
    screen.fill((0,0,200))                                  #填充颜色
    #绘制圆
    color=(255,255,0)                                       #设置颜色
    position=(300,250)                                      #位置
    radius=100                                              #设置半径
    width=100                                               #填充圆的
    pygame.draw.circle(screen,color,position,radius,width)  #画圆
    pygame.display.update()
        
