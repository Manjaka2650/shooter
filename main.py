import pygame 
import cProfile
pygame.init()
from game import Game
import math
    # creer la classe pour le joueur
    # load background
def main():
    bg = pygame.image.load('assets/bg.jpg')
    banner= pygame.image.load('assets/banner.png')
    button= pygame.image.load('assets/button.png')
    # pour le titre
    pygame.display.set_caption('Shooter')
    # taille
    screen = pygame.display.set_mode((1080,640))
    image = pygame.transform.scale(banner,(500,500))
    image_rect= image.get_rect()
    image_rect.x=math.ceil(screen.get_width()/4)

    # import button for launching the game

    play_bouton=pygame.image.load('assets/button.png')
    play_bouton=pygame.transform.scale(play_bouton,(400,150))
    play_bouton_rect= play_bouton.get_rect()
    play_bouton_rect.x=math.ceil(screen.get_width()/3.33)
    play_bouton_rect.y=math.ceil(screen.get_height()/1.7)

    # charger notre jeux
    game=Game()
    # player = models.PLayer()
    # connaitre si elle est ouverte 
    running=True

    while running:
        # appliquer l'arrier plan
        screen.blit(bg,(0,-250))
        
        if game.is_plaing:
            game.start(screen)
        else:

            screen.blit(play_bouton,play_bouton_rect)
            screen.blit(image,image_rect)


            # game.start(screen)
        # get all projectile

        # metre a jour l'ecran
        pygame.display.flip()
        # si je joueur ferme la  fenetre
        for event in pygame.event.get():
            # verifier que l'evenement est la fermeture
            if event.type==pygame.QUIT:
                running=False
                print('fermeture')
                pygame.quit()
            # si le joueur lache une touce du clavier
            elif event.type==pygame.KEYDOWN:
                game.pressed[event.key]=True
                # detecter la touche espace
                if event.key==pygame.K_d :
                    print('launching_right')
                    game.player.shoot_right()
                
                if event.key==pygame.K_a :
                    print('launching_left')
                    game.player.shoot_left()
                    
                    
            elif event.type==pygame.KEYUP:
                game.pressed[event.key]=False
                # play button
            elif event.type==pygame.MOUSEBUTTONDOWN:
                # verifier si on touche le rectangle
                if play_bouton_rect.collidepoint(event.pos):

                    game.startMonster()
                    
main()