import pygame
width=1050
height=630
import time
import os
os.chdir("C://Users//Ridha//Desktop//waw")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Blocks:
    def __init__(self):

        self.murs=0
        self.Coordonees=[]
        self.Collisions=[]

    def Generate_Blocks(self,file):
        with open(file, "r") as file:
            lvl = []
            for i in file:
                L=[]
                for elt in i:
                    if elt!='\n':
                        L.append(elt)
                lvl.append(L)
        self.murs=lvl

    def Coords(self):
        a=0
        for i in self.murs:
            b=0
            for j in i:
                x= b*30
                y=a*30
                if j==':':
                    self.Coordonees.append([x,y])
                b+=1
            a+=1

    def Muerta(self):
        Colli=[]
        for elt in self.Coordonees:
            self.image = pygame.image.load('block.jpg').convert_alpha()
            rect = self.image.get_rect()
            rect.topleft=(elt[0],elt[1])
            Colli.append(rect)
        self.Collisions=Colli



class Player(pygame.sprite.Sprite):
    Movee=True
    def __init__(self,Les_Imgs,P):
        super().__init__()



        self.Personnage=P
        self.image = pygame.image.load(self.Personnage+'_face.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.timer=50
        self.x=self.rect.x
        self.y=self.rect.y
        self.Total_Lifes=2
        self.life=2
        self.Les_Imgs=Les_Imgs
        self.n=1
        self.arrivee=(990,570)
        self.L=[]
        self.collidelist= self.Les_Imgs.Collisions
        self.vitesse=3

    def move(self,xvel, yvel):
        if self.Movee:
            if self.life>0:
                self.rect.x += xvel
                for block in self.collidelist:
                    if self.rect.colliderect(block):
                        self.life-=1
                        time.sleep(0.5)
                        if xvel < 0:
                            self.rect.left = block.right

                        elif xvel > 0:
                            self.rect.right = block.left

                        break


                self.rect.y += yvel
                for block in self.collidelist:
                    if self.rect.colliderect(block):
                        self.life-=1
                        time.sleep(0.5)
                        if yvel < 0:
                            self.rect.top = block.bottom
                        elif yvel > 0:
                            self.rect.bottom = block.top
                        break


class Pane(object):
    hovered=False
    def __init__(self,x,y,txt,ecran):
        pygame.init()
        self.screen=ecran
        self.font = pygame.font.Font('Police//Brightly Crush Shine.otf', 45)
        self.rect = pygame.draw.rect(self.screen, (255,0,0), (x, y, 70, 60), 2)
        self.txt=txt
        self.x=0
        self.y=0
    def hover(self):
        if self.hovered:
            return (255,255,255)
        else:
            return (255,0,0)
    def draw(self):
        self.screen.blit(self.font.render(str(self.txt), True, self.hover()), (self.rect.x+15, self.rect.y+5))
        pygame.display.update()


class Choose_Character():
    def __init__(self,img,pos,ecran):
        self.img=img
        self.ecran=ecran
        self.pos=pos
        self.image = pygame.image.load(self.img+'.png').convert_alpha()
        self.create_rect()
        self.draw()
    def create_rect(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
    def draw(self):
        self.ecran.blit(self.image, self.rect)
