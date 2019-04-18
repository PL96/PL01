#绘制矩形
#-*- conding:utf-8-*-
import pygame,sys
import random                            #导入随机函数
from pygame.locals import*               #导入模块
pygame.init()                            #初始化
screen=pygame.display.set_mode((900,800))#设置窗体的大小
pygame.display.set_caption("绘制矩形")   #设置标题的名称
color=[(255),(255),(0)]                  #设置颜色
pos_x=250
pos_y=250
vel_x=1   #横向运动速度
vel_y=1   #纵向运动速度
#---------插入音乐----------
pygame.mixer.music.load("ypl.mp3")     #插入音乐
pygame.mixer.music.play(-1)
mic=pygame.mixer.Sound("11.wav")
#音乐无限循环
#---------插入文字-----------
fontobj=pygame.font.SysFont("stfangsong",50,italic=True,)             #字体为仿宋，50号大，倾斜
wenzi=fontobj.render(u"杨普伦092",True,(255,0,0),(110,160,246))       #文字内容，文字颜色及背景颜色 


while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill((120,0,200))                   #填充窗口颜色
       #-------移动矩形-------
    pos_x+=vel_x                                #横向运动速度
    pos_y+=vel_y                                #纵向运动速度
    width=0                                     #实体填充
    pos=(pos_x,pos_y,100,100)                   #定义矩形所在的位置及大小
    screen.blit(wenzi,(300,300))

        #---保证矩形在窗口内---
    if pos_x>800 or pos_x<0:
        vel_x=-vel_x
        color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        
        #-------音效-------
        
        mic.play()
    
    if pos_y>700 or pos_y<0:
        vel_y=-vel_y
        color = random.randint(0,255),random.randint(0,255),random.randint(0,255)

        #---音效----
        #mic=pygame.mixer.Sound("11.wav")
        mic.play()
    
    pygame.draw.rect(screen,color,pos,width) 
    pygame.display.update()    #刷新

    
 

















    

