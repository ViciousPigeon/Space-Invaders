import pygame

# Initialize pygame
pygame.init()

# Define constants for screen width and height; set size to this tuple
WIDTH = 800
HEIGHT = 600
size = (WIDTH, HEIGHT)

# Create the screen
screen = pygame.display.set_mode(size)

done = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

click_sound = pygame.mixer.Sound("laser5.ogg")

while not done:
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (x, y, 50, 50))

    pygame.display.flip()

    clock.tick(20)

pygame.quit()

