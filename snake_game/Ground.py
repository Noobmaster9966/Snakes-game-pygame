import pygame
x=pygame.init()

# game window
gameWindow = pygame.display.set_mode((1200,720))
pygame.display.set_caption("Snakes")
# pygame.display.update()

# colors
white = (255,255,255)
red = (255,0,0)
black=(0,0,0)

# game specific variables
exit_game=False
game_over=False

# game loop
while not exit_game:
    for i in pygame.event.get():
        print(i)
        if(i.type==pygame.QUIT):
            exit_game=True

        if(i.type==pygame.KEYDOWN):
            if(i.key==pygame.K_w):

                gameWindow.fill(white)
                pygame.display.update()

            if(i.key==pygame.K_s):
                gameWindow.fill(red)
                pygame.display.update()s

# out of game loop

# ending game
pygame.quit()
quit()