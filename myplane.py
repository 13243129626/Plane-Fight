import pygame

#需要有碰撞监测，继承该类
class MyPlane(pygame.sprite.Sprite):        
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        
        #提高 blit(位块)的速度，也实现透明效果
        self.image1 = pygame.image.load("images/me1.png").convert_alpha()
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()
        #坠机情况
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_2.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_3.png").convert_alpha(),\
            pygame.image.load("images/me_destroy_4.png").convert_alpha()])
        #创建一个image的矩形
        self.rect = self.image1.get_rect()       
        self.width,self.height = bg_size[0],bg_size[1]
        #设定飞机初始位置，在底部中央位置
        self.rect.left,self.rect.top= \
                        (self.width - self.rect.width) // 2,\
                        self.height - self.rect.height - 60
              
        self.speed = 10
        self.active = True
        #将非透明区域设为mask
        self.mask = pygame.mask.from_surface(self.image1)
        
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0
            
    def moveDown(self):
        if self.rect.bottom < self.height-60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60
            
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0
       
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width
        
    def reset(self):
        self.rect.left,self.rect.top= \
                        (self.width - self.rect.width) // 2,\
                        self.height - self.rect.height - 60
        self.active = True
        
