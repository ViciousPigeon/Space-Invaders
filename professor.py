import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (700, 500)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

font = pygame.font.SysFont("Calibri", 25, True, False)
text = font.render("My Text", True, BLACK)


done = False

clock = pygame.time.Clock()

rect_x_change = 5
rect_y_change = 5
rect_x = 50
rect_y = 50

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    rect_x += rect_x_change
    rect_y += rect_y_change

    if rect_x >650 or rect_x < 0:
        rect_x_change *= -1
    if rect_y > 450 or rect_y < 0:
        rect_y_change *= -1

    # pygame.draw.line(screen, GREEN, (0, 0), (100, 100), 5)
    # screen.blit(text, (250, 250))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
