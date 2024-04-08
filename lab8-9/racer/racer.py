import pygame
import random
import time
from sys import exit

# Initializing
pygame.init()
screen = pygame.display.set_mode((400, 600))

# Settings
background = pygame.image.load("media/AnimatedStreet.png")
pygame.mixer.Sound('media/background.wav').play()
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))
speed = 5
score = 0
coin = 0
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("media/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 540) # Player position
    
    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 50:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 350:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("media/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 350), -200) # Enemy position (randomly generated x position)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 700:
            score += 1
            self.rect.top = -200
            self.rect.center = (random.randint(60, 300), -200) # Updating old position to new random position

class Coin(pygame.sprite.Sprite):
    def __init__(self, start, b, e):
        super().__init__()
        self.image = pygame.image.load(f"media/{random.randint(b ,e)}.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 350), start)

    def move(self):
        self.rect.move_ip(0, 4)
        if self.rect.bottom > 700:
            self.rect.top = -200
            self.rect.center = (random.randint(60, 300), -300)

P1 = Player()
E1 = Enemy()

#Different coin weight and values
C1 = Coin(-1200, 1, 3)
C2 = Coin(-2700, 6, 9)
C3 = Coin(-4000, 3, 6)

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
coins.add(C2)
coins.add(C3)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
all_sprites.add(C3)

# Custom event for increasing enemy speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED and coin > 5:
            speed += 2
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Drawing background and points
    screen.blit(background, (0,0))
    scores = font_small.render(f"{score}", True, (0, 0, 0))
    screen.blit(scores, (5, 5))
    coins = font_small.render(f"{coin}", True, (0, 0, 0))
    screen.blit(coins, (380, 5))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
        
    # Collision between player and enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('media/background.wav').stop()
        pygame.mixer.Sound('media/crash.wav').play()
        time.sleep(0.5)

        screen.fill((255, 0, 0))
        screen.blit(game_over, (30, 250))

        pygame.display.flip()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        exit()
    
    # Checking coins for collision with player
    if P1.rect.colliderect(C1.rect):
        C1.rect.center = (random.randint(60, 300), -1900)
        coin += 1
    if P1.rect.colliderect(C2.rect):
        C2.rect.center = (random.randint(60, 300), -100)
        coin += 1
    if P1.rect.colliderect(C3.rect):
        C3.rect.center = (random.randint(60, 300), -800)
        coin += 1
    
    pygame.display.flip()
    clock.tick(60)