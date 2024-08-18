# class player
import pygame
from monster import Monster
from player import PLayer
import datetime



class Game:
    def __init__(self) :
        # pass
        self.is_plaing=False
        # generer un autre joeur 
        self.all_player=pygame.sprite.Group()
        self.player= PLayer(self)
        # groupe de monstre
        self.all_player.add(self.player)
        self.all_monster=pygame.sprite.Group()
        self.pressed={}
        self.score=0
        self.create_monster()

    def update_score(self,screen):

        # Define colors
        green = (111,210,46)

        # Create a font object
        font = pygame.font.Font(None, 36)  # None uses the default font, and 36 is the font size
        # Render the text into an image (surface)
        text_surface = font.render(f"Score : {self.score}", True,green)  # True for anti-aliasing, white for the color
        # Get the rectangle of the text surface to position it
        text_rect = text_surface.get_rect()
        text_rect.x = 10
        text_rect.y= 20  # Center of the screen

        screen.blit(text_surface, text_rect)
    def startMonster(self):
        pass
        self.create_monster()
        # self.create_monster
        self.is_plaing=True
        # restarting all
    def game_over(self):
        self.all_monster.empty()
        self.player.health=self.player.max_health
        self.player.rect.x=400
        self.player.rect.y=450
        self.is_plaing=False

        # Create a date object with the current date
        current_date = datetime.datetime.today()

# Format the date as a string
        date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Formats as 'YYYY-MM-DD'

# Write the date to a file, appending to it if it already exists
        with open("score.txt", "a") as file:  # Open in append mode
            file.write('===============================Shooter===============================\n\n')
            file.write(f"Date: {date_str}\n")
            file.write(f'Score: {self.score}\n')
            file.write('==============================================================\n')
            
        self.score=0


    def start(self,screen):
            # appliquer le joueur
        screen.blit(self.player.image,self.player.rect)
    # avant de les dessiner faudrais les recuperer d'anprd 

    # if self.pressed.get(pygame.K_RIGHT)and self.pressed.get(pygame.K_SPACE):

    # if self.pressed.get(pygame.K_LEFT)and self.pressed.get(pygame.K_SPACE):
        self.update_score(screen)
        self.player.check_collision()
        for projectile in self.player.all_projectile:
        # print(projectile.direction)
            projectile.move()

        self.player.all_projectile.draw(screen)
        for monster in self.all_monster:
            # print(monster.rect.x)
            monster.move()
            monster.update_health_bar(screen)
        self.all_monster.draw(screen)

        self.player.update_health_bar(screen)

    # connaitre les touches actives
        if self.pressed.get(pygame.K_RIGHT):
            if self.player.rect.x<screen.get_width()-self.player.rect.width:
                self.player.move_right()
        if self.pressed.get(pygame.K_LEFT):
            if self.player.rect.x>0:
                self.player.move_left()
    
        if self.pressed.get(pygame.K_UP):
            if self.player.rect.y>0:
                self.player.move_up()
    
        if self.pressed.get(pygame.K_DOWN):
            if self.player.rect.y<screen.get_height()-self.player.rect.width:
                self.player.move_down()

    def create_monster(self):
        monster=Monster(self.player,self)
        self.all_monster.add(monster)

    def check_collision(slelf,sprite,group):
        return pygame.sprite.spritecollide(sprite=sprite,group=group,dokill=False,collided=pygame.sprite.collide_mask)

    def quit_game():
        print('quiting')
