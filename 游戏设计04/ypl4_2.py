#-*-coding:utf-8-*-
#导入模块
import math
import random
import pygame,sys
from pygame.locals import*
pygame.init()#初始化
screen=pygame.display.set_mode((900,800))#设置窗口的大小
pygame.display.set_caption("092杨普伦")  #设置文件的标题
#参数pygame.font.Font(file,size),如果参数设置为None则默认采用系统自带的字体，size是字体的大小
myfont=pygame.font.Font(None,60)

color=(255,255,0)    #字体颜色
width=4              #填充字体
x=300
y=250                #圆心
radius=200           #半径
position=(x-radius,y-radius,radius*2,radius*2)   #位置
a="?"
b="?"
c="?"
d="?"

#生成一个数值
A=[]   #建立一个空的列表
while True:
    i=random.randint(0,9)
    if i not in A:
        A.append(i)
    if len(A)==4:
        break
print(A)
dic={0:False,1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False}
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()
        elif event.type==KEYUP:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_0:
                dic[0]=True
            elif event.key==pygame.K_1:
                dic[1]=True
            elif event.key==pygame.K_2:
                dic[2]=True
            elif event.key==pygame.K_3:
                dic[3]=True
            elif event.key==pygame.K_4:
                dic[4]=True
            elif event.key==pygame.K_5:
                dic[5]=True
            elif event.key==pygame.K_6:
                dic[6]=True
            elif event.key==pygame.K_7:
                dic[7]=True
            elif event.key==pygame.K_8:
                dic[8]=True
            elif event.key==pygame.K_9:

                dic[9]=True
    #clear the screen
    screen.fill((0,255,128))
           
    textImg0=myfont.render(a,True,color)
    screen.blit(textImg0,(x+radius/2-20,y-radius/2))
    textImg1=myfont.render(b,True,color)
    screen.blit(textImg1,(x-radius/2,y-radius/2))
    textImg2=myfont.render(c,True,color)
    screen.blit(textImg2,(x-radius/2,y+radius/2-20))
    textImg3=myfont.render(d,True,color)
    screen.blit(textImg3,(x+radius/2-20,y+radius/2-20))

    #shold the pieces be drawn?
    if dic[A[0]]:
        a=str(A[0])
        start_angle=math.radians(0)
        end_angle=math.radians (90)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x,y-radius),width)
        pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
        textImg0=myfont.render(a,True,color)
        screen.blit(textImg0,(x+radius/2-20,y-radius/2))
        
      
    if dic[A[1]]:
        b=str(A[1])
        start_angle=math.radians(90)
        end_angle=math.radians(180)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
        textImg1=myfont.render(b,True,color)
        screen.blit(textImg1,(x-radius/2,y-radius/2))
        
       
    if dic[A[2]]:
        c=str(A[2])
        start_angle=math.radians(180)
        end_angle=math.radians(270)
        pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
        pygame.draw.line(screen,color,(x,y),(x-radius,y),width)
        pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
        textImg2=myfont.render(c,True,color)
        screen.blit(textImg2,(x-radius/2,y+radius/2-20))
     
    
       
    if dic[A[3]]:
       d=str(A[3])
       start_angle=math.radians(270)
       end_angle=math.radians(360)
       pygame.draw.arc(screen,color,position,start_angle,end_angle,width)
       pygame.draw.line(screen,color,(x,y),(x,y+radius),width)
       pygame.draw.line(screen,color,(x,y),(x+radius,y),width)
       textImg3=myfont.render(d,True,color)
       screen.blit(textImg3,(x-radius/2,y+radius/2-20))
    
    #判断饼是否吃完
    if dic[A[0]] and dic[A[1]] and dic[A[2]] and dic[A[3]]:
        color=(0,255,0)
    pygame.display.update()
        


























                
            
        
        
