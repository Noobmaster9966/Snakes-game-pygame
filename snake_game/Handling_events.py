import pygame

x=pygame.init()
print(x)

# creating a game window
pygame.display.set_mode((1200,720))
pygame.display.set_caption("First Game")

# creating game specific variables
exit_game=False
game_over=False


# game loop
while not exit_game:
    for i in pygame.event.get():
        print(i)
pygame.quit()
quit()