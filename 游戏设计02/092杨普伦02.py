import pygame       #导入系统模块
pygame.init()       #初始化
screen=pygame.display.set_mode((800,600))       #设置游戏窗体大小
pygame.display.set_caption("092ypl")            #设置标题

Color=(0,128,128) #设置背景颜色
screen.fill(Color)  #填充颜色
pic=pygame.image.load("092yp.jpg")                        #增加图片
picx=0          
picy=0
stepx=0.2
stepy=0.2
screen.blit(pic,(0,0))
picrect=pic.get_rect()
pich=picrect.height
picw=picrect.width


#主循环
keep_going=True
while keep_going:
    #获取事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
#控制图片运动
    picx+=stepx
    picy+=stepy
    if picy+pich>=600 or picy<=0:
        stepy=-stepy
    if picx+picw>=800 or picx<=0:
        stepx=-stepx
    screen.fill(Color)
    screen.blit(pic,(picx,picy))
    pygame.display.update()         #更新屏幕
#结束
pygame.quit()



