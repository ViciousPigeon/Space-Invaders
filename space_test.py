import pygame
import random
from Sentient import Sentient
from Projectile import Projectile

# Debugging variable
verbose = False


# Initialize pygame
pygame.init()


# Define useful color constants

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Test")

# Load the background image
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define font for score output
font = pygame.font.SysFont("courier", 24)

score = 0
score_text = font.render(f"Score: {score}", True, WHITE, )
player_health = 100
health_text = font.render(f"Health: {player_health}", True, WHITE)


# Load the player image
# Commenting this out now that I have created a sentient class; testing this
#player_image = pygame.image.load("space-invaders.png")

# Load the player at a specific point
# Commenting this out now that I have created a sentient class; testing this
#player_x = 370
#player_y = 480

# Specify how quickly the player can change position
# Commenting this out now that I have created a sentient class; testing this
#player_y_change = 5

# Make a new player using the Sentient class
player = Sentient("player", 400, 536, 2, 100, "space-invaders.png", (0, SCREEN_WIDTH), (0, SCREEN_HEIGHT), 6, 0)

# Make a new enemy using the Sentient class
# Testing addition of levels - this will eventually be deprecated
#enemy = Sentient("enemy", 400, 100, 2, 100, "ship.png", (0, SCREEN_WIDTH), (0, SCREEN_HEIGHT), 4, 0)

level_one_enemies = []

for row in range(0, 3):
    for col in range(0, 6):
        enemy = Sentient("enemy", (50 + (col * 50)), (50 + (row * 40)), 2, 100, "ship.png", (0, SCREEN_WIDTH),
        (0, SCREEN_HEIGHT), 4, 0)

        level_one_enemies.append(enemy)


# This is a list of every sprite. All Sentients and Projectiles are contained here
all_sprites_list = pygame.sprite.Group()
enemy_sprites_list = pygame.sprite.Group()
all_but_player_list = pygame.sprite.Group()
player_projectile_list = pygame.sprite.Group()
enemy_projectile_list = pygame.sprite.Group()

all_sprites_list.add(player)

#Commenting out for same reason as line 57
# all_sprites_list.add(enemy)
# enemy_sprites_list.add(enemy)
# all_but_player_list.add(enemy)

for enemy in level_one_enemies:
    all_sprites_list.add(enemy)
    enemy_sprites_list.add(enemy)
    all_but_player_list.add(enemy)


clock = pygame.time.Clock()
player_last_fired_time = 0
player_fired_time = 0
enemy_last_fired_time = 0
enemy_fired_time = 0

# Define variable for continuing game loop
running = True

# def draw_sprite(player_x, player_y, player_x_change=0, player_y_change=0):
#     """
#     A function to draw the player at the coordinates passed in
#     :param player_x: the x coordinate
#     :param player_y: the y coordinate
#     :param player_x_change: the function can take a change in x
#     :param player_y_change: the
#     :return:
#     """


while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()


    if pressed[pygame.K_LEFT]: #in pressed:
        if verbose:
            print("Left pressed")
        player.move_left()
    if pressed[pygame.K_RIGHT]: # in pressed:
        if verbose:
            print("Right pressed")
        player.move_right()
    if pressed[pygame.K_UP]: # in pressed:
        if verbose:
            print("Up pressed")
        player.move_up()
    if pressed[pygame.K_DOWN]: # in pressed:
        if verbose:
            print("Down pressed")
        player.move_down()
    if pressed[pygame.K_SPACE]:
        if verbose:
            print("Space pressed")
            print(f"Player (x,y): ({player.rect.x}, {player.rect.y})")
            print(f"Player x mid: {int(player.rect.x + (player.image_width)/2)}")

        player_fired_time = pygame.time.get_ticks()
        if player.fire(pygame.time.get_ticks(), player_last_fired_time):
            projectile = Projectile("player",
                                    player.rect.x + 16,
                                    player.rect.y,
                                    "bullet.png",
                                    "laser5.ogg",
                                    1,
                                    (0, SCREEN_WIDTH),
                                    (0, SCREEN_HEIGHT),
                                    0,
                                    -8)
            player_last_fired_time = pygame.time.get_ticks()
            projectile.play_sound()
            all_sprites_list.add(projectile)
            all_but_player_list.add(projectile)
            player_projectile_list.add(projectile)

    for enemy in enemy_sprites_list:
        enemy.move()

        if enemy.fire(pygame.time.get_ticks(), enemy_last_fired_time):
            if verbose:
                print("Enemy fired")

            projectile = Projectile("enemy",
                                    enemy.rect.x + 16,
                                    enemy.rect.y + enemy.image_height,
                                    "enemy_bullet.png",
                                    "laser5.ogg",
                                    1,
                                    (0, SCREEN_WIDTH),
                                    (0, SCREEN_HEIGHT),
                                    0,
                                    8)
            enemy_last_fired_time = pygame.time.get_ticks()
            if verbose:
                print(f"Enemy last fire time: {enemy_last_fired_time}")

            projectile.play_sound()
            all_sprites_list.add(projectile)
            all_but_player_list.add(projectile)
            enemy_projectile_list.add(projectile)


    for enemy in enemy_sprites_list:
        for projectile in player_projectile_list:
            if pygame.sprite.collide_rect(projectile, enemy):
                projectile.kill()
                enemy.kill()
                score +=1
                score_text = font.render(f"Score: {score}", True, WHITE)
                # enemy = Sentient("enemy",
                #                  random.randrange(0, SCREEN_WIDTH - 50),
                #                  random.randrange(0, SCREEN_HEIGHT / 2),
                #                  1,
                #                  100,
                #                  "ship.png",
                #                  (0, SCREEN_WIDTH),
                #                  (0, SCREEN_HEIGHT),
                #                  4,
                #                  0)
                # all_but_player_list.add(enemy)
                # enemy_sprites_list.add(enemy)
                # all_sprites_list.add(enemy)

    for projectile in enemy_projectile_list:
        if pygame.sprite.collide_rect(player, projectile):
            projectile.kill()
            player.health -= 10


    screen.fill(BLACK)
    screen.blit(background_image, (0, 0))

    health_text = font.render(f"Health: {player.health}", True, WHITE)
    screen.blit(score_text, (0, 0))
    screen.blit(health_text, (SCREEN_WIDTH - health_text.get_width() - 10, 0))
    all_sprites_list.draw(screen)
    all_sprites_list.update(screen)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()



