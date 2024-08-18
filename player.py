import pygame
from projectile import Projectile
import asyncio
class PLayer(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()#constructeur de la super classe
        self.health = 100
        self.game=game
        self.max_health = 100 #nombre max de point de vie
        self.attack = 40
        self.velocity = 10
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x=400
        self.rect.y=450
        self.all_projectile =  pygame.sprite.Group()
        # player mooving
    def update_health_bar(self,surface):
        
        barcolor = (111,210,46)

        # position de la jauge et la largeur         
        bar_position=[self.rect.x+45,self.rect.y,self.health,5]
        bar_back = (0,0,46)
        # position de la jauge et la largeur         
        bar_posit=[self.rect.x+45,self.rect.y,self.max_health,5]
        pygame.draw.rect(surface,bar_back,bar_posit)
        pygame.draw.rect(surface,barcolor,bar_position)
   
    def damage(self,number):
        self.health-=number
        if self.health<=0:
            # self.remove()
            print('health < 0')
            # quiter
            self.game.game_over()


    def move_right(self):
        self.rect.x+=self.velocity

    def move_left(self):

        self.rect.x-=self.velocity

    def move_up(self):
        # if not self.game.check_collision(self,self.game.all_monster):
        self.rect.y-=self.velocity

    def move_down(self):
        # if not self.game.check_collision(self,self.game.all_monster):
        self.rect.y+=self.velocity


    # player shooting right
    def shoot_right(self):
        project=Projectile(self,self.game)
        project.direction='right'
        project.rect.x=self.rect.x+45
        self.all_projectile.add(project)
        # player shooting left
    def shoot_left(self):
        project=Projectile(self,self.game)
        project.rect.x=self.rect.x+45
        project.direction='left'
        self.all_projectile.add(project)
    def check_collision(self):
        for monster in self.game.check_collision(self,self.game.all_monster):
            self.damage(monster.attack)
      