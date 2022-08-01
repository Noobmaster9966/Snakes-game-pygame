import pygame
x=pygame.init()

# game window
gameWindow = pygame.display.set_mode((1200,720))
pygame.display.set_caption("Snakes")
pygame.display.update()

# colors
white = (255,255,255)
red = (255,0,0)
black=(0,0,0)

# game specific variables
exit_game=False
game_over=False
snake_x=0
snake_y=0
snake_size_x=30
snake_size_y=10
clock = pygame.time.Clock()
fps=60
velocity_x=0
velocity_y=0


# game loop
while not exit_game:
    for i in pygame.event.get():
        # print(i)
        if(i.type==pygame.QUIT):
            exit_game=True

        if(i.type==pygame.KEYDOWN):
            if(i.key==pygame.K_d):
                velocity_x= 10
                velocity_y=0

            if (i.key == pygame.K_a):
                 velocity_x= -10
                 velocity_y=0


            if (i.key == pygame.K_w):
                 velocity_y= -10
                 velocity_x=0



            if (i.key == pygame.K_s):
                 velocity_y = 10
                 velocity_x = 0


    snake_x=snake_x+velocity_x
    snake_y=snake_y+velocity_y
    if(snake_x==1200 or snake_y==720 or snake_x== -10 or snake_y== -10):
        exit_game=True
        print("GAME OVER")

    clock.tick(30)
    gameWindow.fill(black)

    pygame.draw.rect(gameWindow, white, [snake_x, snake_y, snake_size_x, snake_size_y], 0, 100)
    pygame.display.update()

# out of game loop

# ending game
pygame.quit()
quit()