import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

x = 50
y = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("blue")
    pygame.draw.circle(screen, "yellow", (x, y), 25)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
        if y < 25:
            y = 25
    if pressed[pygame.K_DOWN]:
        y += 3
        if y > 475:
            y = 475
    if pressed[pygame.K_LEFT]:
        x -= 3
        if x < 25:
            x = 25
    if pressed[pygame.K_RIGHT]:
        x += 3
        if x > 675:
            x = 675

    pygame.display.update()
    clock.tick(60)