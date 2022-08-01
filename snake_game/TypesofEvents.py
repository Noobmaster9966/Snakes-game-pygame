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
        # print(i)
#         visit documentary to get list of events
        if i.type == pygame.QUIT:
            exit_game=True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                print("You have decided to exit the game")
                exit_game=True
            if i.key == pygame.K_w:
                print("Player moving forward")
            if i.key == pygame.K_d:
                print("Player moving rigthward")
            if i.key == pygame.K_a:
                print("Player moving leftward")
            if i.key == pygame.K_s:
                print("Player moving backward")

pygame.quit()
quit()