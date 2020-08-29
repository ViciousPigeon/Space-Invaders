import pygame

# Initialize pygame
pygame.init()

# Define screen dimensions
SCREEN_X = 800
SCREEN_Y = 600
# Create the screen
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Space Invaders")

# Create the background
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (SCREEN_X, SCREEN_Y))

# Create player image and initial position
player_img = pygame.image.load("space-invaders.png")
player_x = 370
player_y = 480
player_change_x = 0
player_change_y = 0

# Create bullet
# bullet_state: "ready" you can't see the bullet
#               "fire" the bullet is currently moving
# bullet_img = pygame.image.load("bullet.png")
# bullet_x = 0
# bullet_y = 0
# bullet_change_x = 0
# bullet_change_y = 0
# bullet_state = "ready"

def player(x, y):

    screen.blit(player_img, (x, y))

# def fire_bullet(x, y):


running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # player_y += 0.1
    # print(player_y)
    # if player_y > 600:
    #     player_y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -1
            if event.key == pygame.K_RIGHT:
                player_change_x = 1
            if event.key == pygame.K_UP:
                player_change_y = -1
            if event.key == pygame.K_DOWN:
                player_change_y = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                player_change_x = 0
            if event.key == pygame.K_UP or pygame.K_DOWN:
                player_change_y = 0


    player_x += player_change_x
    player_y += player_change_y

    if player_x < 0:
        player_x = 800
    if player_x > 800:
        player_x = 0
    if player_y < 0:
        player_y = 600
    if player_y > 600:
        player_y = 0
    player(player_x, player_y)
    pygame.display.update()

