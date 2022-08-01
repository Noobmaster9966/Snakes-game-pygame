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
snake_x=10
snake_y=10
snake_size_x=30
snake_size_y=10



# game loop
while not exit_game:
    for i in pygame.event.get():
        # print(i)
        if(i.type==pygame.QUIT):
            exit_game=True

        gameWindow.fill(white)
        pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size_x,snake_size_y],0,100)
        pygame.draw.rect
        pygame.display.update()

# out of game loop

# ending game
pygame.quit()
quit()