#绘制矩形
import pygame,sys          #导入sys库
from pygame.locals import*
pygame.init()                            #初始化
screen=pygame.display.set_mode((600,500))#设置窗口的大小
pygame.display.set_caption("绘制矩形")   #设置标题
pos_x=300                                #x轴的位置
pos_y=250                                #y轴的位置
vel_x=2                                  #横轴运动速度                                
vel_y=1                                  #纵轴运动速度
#执行死循环，确保窗口一直显示
while True:
    for event in pygame.event.get():     #遍历所有的事件
        if event.type in(QUIT,KEYDOWN):  #如果单击则退出
            sys.exit()
    screen.fill((0,0,200))     #填充颜色
    #---------------移动矩形-----------------
    pos_x+=vel_x               #矩形横轴运动速度
    pos_y+=vel_y               #矩形纵轴运动速度

    #保证矩形在窗口里面运动
    if pos_x>500 or pos_x<0:
        vel_x=-vel_x
    if pos_y>400 or pos_y<0:
        vel_y=-vel_y

    #--------------绘制矩形------------------
    color=(255,255,0)        #设置颜色
    width=0                  #填充为0（不填充）
    pos=(pos_x,pos_y,100,100)#位置
    pygame.draw.rect(screen,color,pos,width)

    pygame.display.update()  #更新
    















        
