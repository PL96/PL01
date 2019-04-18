#绘制线条
import pygame,sys  #导入sys库
from pygame.locals import*
pygame.init()            #初始化
screen=pygame.display.set_mode((600,500))#设置窗口的大小
pygame.display.set_caption("绘制线条")   #设置标题名称
while True:
    for event in pygame.event.get():     #遍历所有的事件
        if event.type in (QUIT,KEYDOWN): #如果单击则退出
            sys.exit()
    screen.fill((0,80,0))                #填充窗口的颜色
    #-----------画直线------------
    color=(100,255,200)                  #设置颜色
    width=8
    pygame.draw.line(screen,color,(100,100),(500,400),width)
    pygame.display.update()              #刷新
        
        
        
