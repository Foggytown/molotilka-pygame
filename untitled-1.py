# coding=utf-8
import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y,vx,vy):
        super().__init__(all_sprites)
        self.radius = radius
        self.x=x
        self.y=y
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("white"), (radius, radius), radius)
        self.rect = pygame.Rect(x-radius, y-radius, 2 * radius, 2 * radius)
        self.vx=vx
        self.vy=vy

    def update(self,ti):
        global count
        global running
        self.rect = self.rect.move(self.vx*ti, self.vy*ti)
        self.x+=self.vx*ti
        self.y+=self.vy*ti
        if pygame.sprite.spritecollideany(self, bricks):
            self.vx = (-self.vx+(random.random()/10-0.01))
            self.vy = (-self.vy+(random.random()/10-0.01))
            if abs(self.vy)<0.1:
                if self.vy<0:
                    self.vy=-0.2
                else:
                    self.vy=0.2
            if abs(self.vy)>0.6:
                if self.vy<0:
                    self.vy=-0.4
                else:
                    self.vy=0.4  
            if abs(self.vx)<0.03:
                if self.vx<0:
                    self.vx=-0.03
                else:
                    self.vx=0.03 
            if abs(self.vx)>0.6:
                if self.vx<0:
                    self.vx=-0.3
                else:
                    self.vx=0.3 
            now=pygame.sprite.spritecollideany(self, bricks)
            now.delete()
            if now.delit:
                count+=1
            else:
                if self.x<now.center:
                    self.vx-=0.2
                else:
                    self.vx+=0.2
                    
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = (-self.vy+(random.random()/10-0.01))
            if abs(self.vy)<0.1:
                if self.vy<0:
                    self.vy=-0.2
                else:
                    self.vy=0.2
            if abs(self.vy)>0.6:
                if self.vy<0:
                    self.vy=-0.4
                else:
                    self.vy=0.4               
            
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = (-self.vx+(random.random()/10-0.01))
            if abs(self.vx)<0.03:
                if self.vx<0:
                    self.vx=-0.03
                else:
                    self.vx=0.03 
            if abs(self.vx)>0.6:
                if self.vx<0:
                    self.vx=-0.3
                else:
                    self.vx=0.3
                    
        if pygame.sprite.spritecollideany(self,niz):
            screen.fill((0,0,0))
            drawt("You lost",(400,375))
            running=False
            pygame.display.flip()
        
            
class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2,nizis=False):
        super().__init__(all_sprites)
        if x1 == x2: 
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        elif nizis:
            self.add(niz)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)            

            
class Bricks(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2,y2,delit=True):
        super().__init__(all_sprites)
        self.add(bricks)
        opa=pygame.Surface([x2,y2])
        opa.fill((0,0,0))
        pygame.draw.rect(opa,(255,255,255), (0,0,x2,y2),5)
        self.image=opa
        self.rect = pygame.Rect(x1, y1, x2, y2) 
        self.delit=delit
        self.center=x1+x2//2
    def delete(self):
        if self.delit:
            self.rect=pygame.Rect(-1000, -1000, 1,1)  
    def update(self,ti):
        self.rect = self.rect.move(0.5*ti, 0)
        self.center+=0.5*ti

                
def drawt(txt, cords):
    font = pygame.font.Font(None, 50)
    text = font.render(txt, 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, cords)


def drawall():
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    drawt("Score:"+str(count),(300,50))
    pygame.draw.line(screen,(255,255,255),(0,100),(1000,100),5)


    
running = True
pygame.init()
all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
niz=pygame.sprite.Group()
bricks=pygame.sprite.Group()
size = width, height = 1000, 750
screen = pygame.display.set_mode(size)
Border(5, 100, width - 5, 100)
Border(5, height - 5, width - 5, height - 5,True)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
screen.fill((0, 0, 0))
pygame.draw.line(screen,(255,255,255),(0,100),(1000,100),5)
left,top,size1,size2=100,100,100,66
x1=500
count=0
for i in range(8):
    for j in range(6):
        a=Bricks(left+i*size1,top+j*size2,size1,size2)
bar=Bricks(480,650,80,10,False)
ball=Ball(10,500,580,0,-0.4)
all_sprites.draw(screen)
pygame.display.flip()
clock = pygame.time.Clock()
left=False
right=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type== pygame.KEYDOWN:
            if event.key==276:
                left=True
        if event.type== pygame.KEYDOWN:
            if event.key==275:
                right=True
        if event.type==pygame.KEYUP:
            if event.key==276:
                left=False
        if event.type==pygame.KEYUP:
            if event.key==275:
                right=False
    ti = clock.tick()
    if left and right:
        pass
    elif left:
        bar.update(-ti)
    elif right:
        bar.update(ti)
    ball.update(ti)
    drawall()
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()