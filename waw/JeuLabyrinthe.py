import pygame
import os
os.chdir("C://Users//Ridha//Desktop//waw")
pygame.init()
from pygame.locals import *
ecran = pygame.display.set_mode((1050,690))
from Personnage import *
import time

Personnage='Luffy'
Les_Imgs=Blocks()
Path_Lvl='Niveaux//'
Les_Imgs.Generate_Blocks(Path_Lvl+'Niveau1.txt')
Les_Imgs.Coords()
Les_Imgs.Muerta()


class Game:
    def __init__(self):
        self.player = Player(Les_Imgs,'Itachi')
        self.pressed={}


GameOver = pygame.image.load("black.jpg").convert_alpha()
Rect_GameOver= GameOver.get_rect()
game= Game()

###Initialisation:



Characters=[Choose_Character('Itachi',(10000,10000),ecran),Choose_Character('Luffy',(10000,10000),ecran)]

class Options:
    hovered = False
    def __init__(self, text, pos, action):
        self.text = text
        self.pos = pos
        self.action=action
        self.set_rect()
        self.draw()


    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            if self.action=='None':
                return (0,0,0)
            elif self.action=='Niveau':
                return (255,215,0)
            elif self.action=='Restart':
                return (255,215,92)
            else:
                return (255, 0,0)


    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def draw(self):
        self.set_rend()
        ecran.blit(self.rend, self.rect)
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
    def launch(self):
        if self.action=='Start':
            Start()
        elif self.action=='Settings':
            Settings()
        elif self.action=='Back':
            Back_()
        elif self.action=='Facile':
            Mode_de_jeu(0)
        elif self.action=='Normal':
            Mode_de_jeu(1)
        elif self.action=='Difficile':
            Mode_de_jeu(2)
        elif self.action=='Credits':
            Credits()



"""Fonction qui permet de tout clear"""
def Clear(options):
    for option in options:
        option.rect.topleft=(20000,20000)

"""Fonction qui modifie la difficulté"""
def Mode_de_jeu(arg):
    if arg==0:
        game.player.Total_Lifes=4
        game.player.timer=60
        game.player.vitesse=2
    elif arg==1:
        game.player.Total_Lifes=3
        game.player.timer=50
        game.player.vitesse=3
    elif arg==2:
        game.player.Total_Lifes=2
        game.player.timer=30
        game.player.vitesse=4


def demmarer(ecran,x,y,txt,stop):
    ax=x
    ay=y
    L=[]
    for i in range(int(txt),int(stop)):
        a=Pane(ax,ay,str(i),ecran)
        if ax!=970:
            ax+=100
            L.append(a)
        else:
            ax=x
            ay+=90
            L.append(a)
    return L

'''Fonctions Back, Start, Settings & ChooseLvl'''
###
def Back_():
    ecran.blit(image,(0,0))
    options[0].rect.topleft=(505, 300)
    options[1].rect.topleft=(465, 370)
    options[2].rect.topleft=(490, 440)
    for i in range(3,9):
        options[i].rect.topleft=(10000,10000)
    for k in range (len(Characters)):
        Characters[k].rect.topleft=(10000,10000)
    Rect_GameOver.topleft=(10000,10000)

    game.player.L=[]
    game.player.n=1
    Les_Imgs.murs=0
    Les_Imgs.Coordonees=[]
    Les_Imgs.Collisions=[]
    Les_Imgs.Generate_Blocks(Path_Lvl+'Niveau1.txt')
    Les_Imgs.Coords()
    Les_Imgs.Muerta()
    game.player.collidelist=Les_Imgs.Collisions



def Start():
    pygame.time.set_timer(USEREVENT+1, 1000)
    Rect_GameOver.topleft=(0,0)
    running = True
    options[3].rect.topleft=(0,630)
    timer=game.player.timer
    game.player.life=game.player.Total_Lifes
    game.player.Movee=True
    game.player.rect.topleft=(0,0)
    game.player.image = pygame.image.load(game.player.Personnage+'_face.png').convert_alpha()

    clock = pygame.time.Clock()
    draw_all=True
    while running:
        if draw_all:
            ecran.blit(laby,(0, 0))

            for elt in Les_Imgs.Collisions:
                ecran.blit(Mur,elt)
            ecran.blit(Arrivee,Zone_Arrivee)

            """On set les Compteurs"""
            Compteur_Vies= Options('Lifes : {}'.format(game.player.life),(570,635),'None')
            Compteur_Vies.draw()
            Timer= Options('Timer : {}'.format(timer),(210,635),'None')
            Timer.draw()
            Niveau= Options('Niveau {}'.format(game.player.n),(840,635),'ued')
            Niveau.draw()

            """On insere le bouton back si le mec veut quitter"""

            if options[3].rect.collidepoint(pygame.mouse.get_pos()):
                options[3].hovered = True
                if pygame.mouse.get_pressed()[0]==1:
                    running=False
            else:
                options[3].hovered = False
            options[3].draw()






            if game.pressed.get(pygame.K_RIGHT):

                game.player.move(game.player.vitesse, 0)
                game.player.image = pygame.image.load(game.player.Personnage+'_droite.png').convert_alpha()
            if game.pressed.get(pygame.K_LEFT):

                game.player.move(-game.player.vitesse, 0)
                game.player.image = pygame.image.load(game.player.Personnage+'_gauche.png').convert_alpha()
            if game.pressed.get(pygame.K_UP):
                game.player.move(0, -game.player.vitesse)
                game.player.image = pygame.image.load(game.player.Personnage+'_back.png').convert_alpha()
            if game.pressed.get(pygame.K_DOWN):
                game.player.move(0, game.player.vitesse)
                game.player.image = pygame.image.load(game.player.Personnage+'_face.png').convert_alpha()

        #Ici on gère le timer pour faire en sorte que le timer fonctionne, et que si le timer ou la vie est à 0 avant que le joueur n'ait atteint la ligne d'arrivée, alors la partie est finie
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            if event.type ==USEREVENT+1:
                if timer>0 and game.player.life>0 and [game.player.rect.topleft[0],game.player.rect.topleft[1]] not in game.player.arrivee:
                    timer -= 1
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key]= True

            elif event.type == pygame.KEYUP:
                game.pressed[event.key]= False

            if timer==0 or game.player.life==0:
                game.player.Movee=False
                draw_all=False

                ecran.blit(GameOver,Rect_GameOver)
                if event.type == pygame.KEYDOWN and event.key== pygame.K_SPACE:

                        running=False

                        Back_()
                        game.pressed.clear()




        game.player.update()
        if draw_all:
            ecran.blit(game.player.image, game.player.rect)
        pygame.display.update()

        #Si le  joueur atteint la ligne d'arrivée, il passe au niveau suivant
        if game.player.rect.colliderect(Zone_Arrivee):
            if game.player.n==10:
                game.player.Movee=False
                if tk_info:
                    Tk().wm_withdraw()
                    messagebox.showinfo('','You made it in {} seconds'.format(sum(game.player.L)))
                    tk_info=False
            else:
                game.player.Movee=True
                game.player.n+=1
                running=False
                Les_Imgs.murs,Les_Imgs.Coordonees =0,[]
                Les_Imgs.Collisions=[]
                Les_Imgs.Generate_Blocks(Path_Lvl+'Niveau'+str(game.player.n)+'.txt')
                Les_Imgs.Coords()
                Les_Imgs.Muerta()
                game.player.collidelist=Les_Imgs.Collisions
                Start()


        clock.tick(50)


def Settings():
    Clear(options)
    options[3].rect.topleft=(0,0)
    options[4].rect.topleft=(370, 250)
    options[5].rect.topleft=(510, 250)
    options[6].rect.topleft=(710, 250)
    options[7].rect.topleft=(100,250)
    options[8].rect.topleft=(100,450)

    Characters[0].rect.topleft=(400,450)
    Characters[1].rect.topleft=(550,450)
    run=True
    while run:
        ecran.blit(image,(0,0))
        for i in range(4,9):

            if options[i].rect.collidepoint(pygame.mouse.get_pos()):
                if options[i].action!='None':
                    options[i].hovered = True
                if pygame.mouse.get_pressed()[0]==1:
                    game.player.n=1
                    options[i].launch()
            else:
                options[i].hovered = False
            options[i].draw()

        if options[3].rect.collidepoint(pygame.mouse.get_pos()):
            options[3].hovered = True
            if pygame.mouse.get_pressed()[0]==1:
                run=False
        else:
            options[3].hovered = False
        options[3].draw()

        for char in Characters:
            if char.rect.collidepoint(pygame.mouse.get_pos()):
                char.hovered= True
                if pygame.mouse.get_pressed()[0]==1:
                    game.player.Personnage= char.img
            char.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
        pygame.display.update()




def Credits():
    ecran.blit(image,(0, 0))
    L=demmarer(ecran,70,100,"1","30")
    continuer=True
    options[3].rect.topleft=(0,0)
    while continuer:
        for option in L:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered=True
                if pygame.mouse.get_pressed()[0]==1:
                    game.player.n=int(option.txt)
                    pygame.display.set_caption('Level ' +str(game.player.n))
                    continuer=False
                    Les_Imgs.murs,Les_Imgs.Coordonees =0,[]
                    Les_Imgs.Collisions=[]
                    Les_Imgs.Generate_Blocks(Path_Lvl+'Niveau'+str(game.player.n)+'.txt')
                    Les_Imgs.Coords()
                    Les_Imgs.Muerta()
                    game.player.collidelist=Les_Imgs.Collisions
                    Start()
            else:
                option.hovered=False
            option.draw()
        if options[3].rect.collidepoint(pygame.mouse.get_pos()):
            options[3].hovered = True
            if pygame.mouse.get_pressed()[0]==1:
                continuer=False
                options[3].rect.topleft=(10000,10000)
                game.player.n=1
                Les_Imgs.murs=0
                Les_Imgs.Coordonees=[]
                Les_Imgs.Collisions=[]
                Les_Imgs.Generate_Blocks(Path_Lvl+'Niveau1.txt')
                Les_Imgs.Coords()
                Les_Imgs.Muerta()
                game.player.collidelist=Les_Imgs.Collisions
        else:
            options[3].hovered = False
        options[3].draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
                quit()

####
'''Options & Texture'''
menu_font = pygame.font.Font('Police//Brightly Crush Shine.otf', 45)


options = [Options("PLAY", (505, 300),'Start'), Options("SETTINGS", (465, 370),'Settings'),
           Options("LEVELS", (490, 440),'Credits'),Options('<=',(3330,3330),'Back'),Options("Easy", (52000, 30000),'Facile'), Options("Normal", (46005, 37000),'Normal'),
           Options("Hard", (47000, 44000),'Difficile'),Options("Difficulty: ",(10000,10000),'None'),Options('Character: ',(10000,10000),'None')]




'''Images'''
image = pygame.image.load("Fond.jpg").convert_alpha()

laby= pygame.image.load("Labyrinthe.jpg").convert_alpha()
Mur = pygame.image.load('block.jpg').convert_alpha()
Arrivee= pygame.image.load('Arrivée.png').convert_alpha()
Zone_Arrivee= Arrivee.get_rect()
Zone_Arrivee.topleft=game.player.arrivee





continuer=True
while continuer:
    ecran.blit(image,(0, 0))
    for option in options:
        if option.action!='None':
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
                if pygame.mouse.get_pressed()[0]==1:
                    game.player.n=1
                    option.launch()
            else:
                option.hovered = False
        option.draw()


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip()
    pygame.display.update()
pygame.quit()