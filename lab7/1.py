import pygame, datetime
from sys import exit

pygame.init()

screen = pygame.display.set_mode((700, 525))
bg = pygame.transform.scale(pygame.image.load("images/clock.jpeg"), (700, 525)).convert()
left = pygame.transform.scale(pygame.image.load("images/left.png"), (700, 525)).convert_alpha()
right = pygame.transform.scale(pygame.image.load("images/right.png"), (700, 525)).convert_alpha()
left_rect = left.get_rect(center=(700/2, 525/2))
right_rect = right.get_rect(center=(700/2, 525/2))
clock = pygame.time.Clock()

x = datetime.datetime.now()
minute_angle = (x.minute * 360) / 60 + 45
second_angle = (x.second * 360) / 60 - 122

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    minute_angle += 0.0095
    rotated_minute_hand = pygame.transform.rotate(left, -minute_angle)
    rotated_minute_hand_rect = rotated_minute_hand.get_rect(center=left_rect.center)

    second_angle += 0.097
    rotated_second_hand = pygame.transform.rotate(right, -second_angle)
    rotated_second_hand_rect = rotated_second_hand.get_rect(center=right_rect.center)
    
    screen.blit(bg, (0, 0))
    screen.blit(rotated_minute_hand, rotated_minute_hand_rect)
    screen.blit(rotated_second_hand, rotated_second_hand_rect)

    pygame.display.flip()
    clock.tick(60)