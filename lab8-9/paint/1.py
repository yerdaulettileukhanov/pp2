import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

done = False
clock = pygame.time.Clock()

x1 = 10
y1 = 10
x2 = 10
y2 = 10

radius = 10

color = (0, 128, 255)
isMouseDown = False
screen.fill((0, 0, 0))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click
                        x1 = event.pos[0]
                        y1 = event.pos[1]
                        isMouseDown = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        isMouseDown = False
                        another_layer.blit(screen, (0, 0))

                if event.type == pygame.MOUSEMOTION:
                        if isMouseDown:
                            x2_cr = event.pos[0]
                            radius = abs(x2_cr - x1_cr)
                            screen.blit(another_layer, (0, 0))
                            pygame.draw.circle(screen, color, (x1_cr, y1_cr), radius)

        pygame.display.flip()
        clock.tick(60)
