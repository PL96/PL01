#092杨普伦
#pygame框架
import pygame    #导入模块
pygame.init()    #初始化
#基本设置
screen=pygame.display.set_mode((800,600))     #设置游戏窗体大小
pygame.display.set_caption("092yangpulun")    #设置标题
#主循环
keep_going=True
while keep_going:
    #获取事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    #更新屏幕
    pygame.display.update()
#over

        
    
