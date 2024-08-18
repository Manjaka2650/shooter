import pygame
import random

import pygame.locals
class Monster(pygame.sprite.Sprite):

    def __init__(self,player,game):
        super().__init__()
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.game=game
        self.velocity = 1
        self.attack=1
        self.player=player
        self.rect.x =random.randint(0,1080)
        self.rect.y = random.randint(0,640)+43
        self.max_health=100
        self.health=100
        self.origin_image = self.image
        self.angle = 0
        self.origin=1

    def damage(self,number):
        self.health-=number
        if self.health<=0:
            # self.remove()
            self.rect.x=random.randint(0,1080)
            self.rect.y=random.randint(0,1080)
            self.health=self.max_health
            if len(self.game.all_monster)<4:
                self.game.create_monster()

    def update_health_bar(self,surface):
        barcolor = (111,210,46)
        # position de la jauge et la largeur         
        bar_position=[self.rect.x+10,self.rect.y-20,self.health,5]
        bar_back = (0,0,46)
        # position de la jauge et la largeur         
        bar_posit=[self.rect.x+10,self.rect.y-20,self.max_health,5]
        pygame.draw.rect(surface,bar_back,bar_posit)
        pygame.draw.rect(surface,barcolor,bar_position)
        
    def move(self):

        if self.rect.x>self.player.rect.x:
            # for  i in range (1,24):
            if self.origin==48 :
                self.origin=1
            self.image=pygame.image.load(f'assets/mummy_left/mummy{self.origin}.png')

            self.rect.x-=self.velocity
            self.origin+=1
        elif self.rect.x<self.player.rect.x:
            #  for  i in range (1,24):
            if self.origin==48 :
                self.origin=1
            self.image=pygame.image.load(f'assets/mummy_right/rmummy{self.origin}.png')

            self.rect.x+=self.velocity
            self.origin+=1
        if self.rect.y-40>self.player.rect.y:
            self.rect.y-=self.velocity
        else:
            self.rect.y+=self.velocity
    