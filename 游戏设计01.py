#092������
#pygame���
import pygame    #����ģ��
pygame.init()    #��ʼ��
#��������
screen=pygame.display.set_mode((800,600))     #������Ϸ�����С
pygame.display.set_caption("092yangpulun")    #���ñ���
#��ѭ��
keep_going=True
while keep_going:
    #��ȡ�¼�
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    #������Ļ
    pygame.display.update()
#over

        
    
