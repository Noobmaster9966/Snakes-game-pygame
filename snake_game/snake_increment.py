import random
import pygame

x = pygame.init()

# game window
gameWindow = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Snakes")
pygame.display.update()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# game specific variables
exit_game = False
game_over = False
snake_x = 0
snake_y = 0
snake_size_x = 10
snake_size_y = 10
clock = pygame.time.Clock()
fps = 60
velocity_x = 0
velocity_y = 0
food_x=random.randint(20,1150)
food_y=random.randint(20,700)
score=0
init_velocity=5
parameter=6
snake_list=[]
snake_length=1
flag=0


font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])


def plotsnake(gameWindow,color,snake_list,snake_size_x,snake_size_y):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size_x,snake_size_y])
        # print(snake_list)


# game loop
while not exit_game:
    for i in pygame.event.get():
        # print(i)
        if (i.type == pygame.QUIT):
            exit_game = True


        if (i.type == pygame.KEYDOWN):

            if(i.key==pygame.K_ESCAPE):
                exit_game=True

            if (i.key == pygame.K_d):
                velocity_x = init_velocity
                velocity_y = 0

            if (i.key == pygame.K_a):
                velocity_x = -init_velocity
                velocity_y = 0

            if (i.key == pygame.K_w):
                velocity_y = -init_velocity
                velocity_x = 0

            if (i.key == pygame.K_s):
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if(abs(snake_x - food_x)<parameter and abs(snake_y - food_y)<parameter):
        score+=10
        food_x = random.randint(20, 1150)
        food_y = random.randint(20, 700)
        # snake_size_x+=1
        # snake_size_y+=1
        snake_length +=1
        init_velocity+=1
        parameter+=1
        # print(score)

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    # print(snake_list)
    if(len(snake_list)>snake_length):
        del snake_list[0]


    clock.tick(60)
    if(flag!=1):
     gameWindow.fill(black)
     text_screen("Score : "+str(score),red,5,5)
     pygame.draw.rect(gameWindow, red, [food_x, food_y, 10,10])
    # pygame.draw.rect(gameWindow, white, [snake_x, snake_y, snake_size_x, snake_size_y])
     plotsnake(gameWindow,white,snake_list,snake_size_x,snake_size_y)
     pygame.display.update()

    else:
        gameWindow.fill(red)
        text_screen("Game Over",black,450,400)
        text_screen("Your Score = "+str(score),black,450,450)
        text_screen("Press Esc to exit ",black,450,500)
        text_screen("Always Remember : Nanu ka saap bhot bada hai",black,150,600)
        pygame.display.update()

    if (snake_x >= 1200 or snake_y >= 720 or snake_x <= -10 or snake_y <= -10):
        # exit_game = True
        flag=1
        # print("GAME OVER")
        # print("Your Score = ",score)





# out of game loop

# ending game
pygame.quit()
quit()