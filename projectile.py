import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self,player,game):
        super().__init__()
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(55,55))
        self.velocity = 16
        self.game=game
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+ player.rect.width*2/3
        self.rect.y = player.rect.y+player.rect.height/2
        self.direction=''
        # acceder a une fonction de redimension
        self.origin_image = self.image
        self.angle = 0
    def rotate(self):
        #  tourner le projectile        
        self.angle+=-8
        self.image=pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect=self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectile.remove(self)

    # def move_right(self):
    #     self.rect.x +=self.velocity
    #     self.rotate()

    #     if self.rect.x>1080:
    #         self.remove()
    #         return
    #     for monster in self.player.game.check_collision(self,self.player.game.all_monster):
    #         # return
    #             print('destroyed')
    #             monster.damage(self.player.attack)

    #             self.game.score+=1
    #             self.remove()
        
    # def move_left(self):
    #     self.rect.x-=self.velocity
    #     self.rotate()
    #     if self.rect.x<0:
    #         self.remove()
    #         return
    #     for monster in self.player.game.check_collision(self,self.player.game.all_monster):
    #         # return
    #             print('destroyed')
    #             monster.damage(self.player.attack)
    #             print(f'{self.game.score}')
    #             self.game.score+=1
    #             self.remove()
    def move_right(self):
       self.rect.x += self.velocity
       self.rotate()

       if self.rect.x > 1080:
            self.remove()
            return

    # Check for collisions
       collided_monsters = pygame.sprite.spritecollide(self, self.player.game.all_monster, False)
       if collided_monsters:
            for monster in collided_monsters:
                monster.damage(self.player.attack)
                self.game.score += 1
            self.remove()

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate()

        if self.rect.x < 0:
            self.remove()
            return

    # Check for collisions
        collided_monsters = pygame.sprite.spritecollide(self, self.player.game.all_monster, False)
        if collided_monsters:
            for monster in collided_monsters:
                monster.damage(self.player.attack)
                self.game.score += 1
            self.remove()

    def move(self):
        if self.direction=='right':
            self.move_right()
            
        elif self.direction=='left':
                self.move_left()