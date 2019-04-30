'''
姓名：杨普伦
学号：201611520
'''
#_*_coding:utf_8_*_
import pygame,math
pygame.init()                              #初始化

screen=pygame.display.set_mode((800,600))  #设置窗口的大小
pygame.display.set_caption("杨普伦")       #设置标题
color1=[0,128,128]
color2=[192,192,192]                 #设置颜色
screen.fill(color1)           #填充颜色
pic=pygame.image.load("33.jpg") #增加图片
picx=0                        #设置图片的横轴坐标
picy=0                        #设置图片的纵轴坐标
#--------------------运动速度----------------------
step=[1,1]
timer=pygame.time.Clock()       #调用time模块的Clock函数来控制运动
#--------------------插入音乐----------------------
pygame.mixer.music.load("55.mp3")
pygame.mixer.music.play(2)       #音乐播放几次
pygame.mixer.music.set_pos(50000)#音乐从什么时候开始播放

screen.blit(pic,(0,0))           #把图片贴到窗口（0,0）位置
picrect=pic.get_rect()           #获取图片的属性
pich=picrect.height              #图片的高
picw=picrect.width               #图片的宽

#--------------------绘制挡板-----------------------

paddlex=50                    #挡板的横轴坐标
paddley=30                     #挡板的纵轴左边
paddlew=200                     #挡板的宽
paddleh=20                      #挡板的高
#--------------------游戏变量------------------------
score=0      #初始分数为0       
lives=3      #生命为3次
#--------------------主程序--------------------------
keep_going=True
while keep_going:
       #检查事件
       for event in pygame.event.get():                   #遍历所有事件
              if event.type==pygame.QUIT:                 #如果单击关闭窗口则退出
                     pygame.mixer.music.stop()            #音乐停此
                     keep_going=False
              elif event.type==pygame.KEYDOWN:            #如果键盘被按下
                     if event.key==pygame.K_ESCAPE:       #如果按下ESC键
                            pygame.mixer.music.pause()    #音暂停乐
                            step[0]=0                     #按ESC小球运动暂停
                            step[1]=0
                     if event.key==pygame.K_RETURN:       #如果按的是回车键
                            pygame.mixer.music.unpause()  #音乐继续
                            step[1]=1
                            step[0]=1                     #按Enter小球继续运动
                     if event.key==pygame.K_UP:           #如果键盘弹起来
                            y1=pygame.mixer.music.get.get_volume()#获取音量
                            y1+=0.05                      #音量自加
                            pygame.mixer.music.set_volume(y1)   #音量的范围是[0,1]
                            
#--------------------控制小球的运动--------------------
       picx+=step[0]
       picy+=step[1]


       if picx<=0 or picx+picw>=800:        #控制小球的水平方向
              step[0]=-step[0]
       if picy+pich>=600:                   #如果纵轴方向小于600
              step[1]=-step[1]              
       if picy<=0:                          #如果纵轴方向加上小球的宽小于600
              step[1]=1
              step[0]=1
              lives-=1                      #生命减一
              if lives==0:                  #如果生命为0
                     keep_going=False       #停此
              picy=0
              picx=0
              score=0
       screen.fill(color1)                 #填充颜色

       
       screen.blit(pic,(picx,picy))   #贴图片screen.blit(pic,(picrectleft,picrect.top))

       
#---------------------根据鼠标中心绘制挡板---------------------
       paddlex=pygame.mouse.get_pos()[0]-paddlew/2                    #
       pygame.draw.rect(screen,color2,[paddlex,paddley,paddlew,paddleh])

#---------------------绘制挡板接球的过程------------------------
       if step[1]<0 and picx+picw/2>=paddlex and picx-picw/2<=paddlex+paddlew:
              if picy>=paddley and picy<=paddley+paddleh:
                     step[1]=-step[1]
                     #-----音效------
                     yx=pygame.mixer.Sound("1.wav")
                     yx.play()
                     #------分数-----
                     score=score+10
       fontobj=pygame.font.SysFont("Times",30,italic=False)
       text_score="Lives:"+str(lives)+"Score="+str(score)
       text=fontobj.render(text_score,True,(255,255,255))  #blit贴贴
       text_rect=text.get_rect()
       text_rect.top=450
       text_rect.centerx=screen.get_rect().centerx
       screen.blit(text,text_rect)
       fontobj=pygame.font.SysFont("Times",30,italic=False)
       text_score=("yangpulun")
       text=fontobj.render(text_score,True,(255,255,255))  #blit贴贴
       text_rect=text.get_rect()
       text_rect.top=500
       text_rect.centerx=screen.get_rect().centerx
       screen.blit(text,text_rect)



       timer.tick(200)#每秒刷新的次数
       pygame.display.update()
pygame.quit()
       




































       
       
       



























       
                  
    
