import pygame
import random
import time
from sys import exit

# setup
pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont("Verdana", 40)
game_over = font.render("Game Over", True, "white")
status = 0
FPS = 10
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x = 30
        self.y = 30
        self.x_dir = 1
        self.y_dir = 0
        self.body = [pygame.Rect((self.x, self.y), (30, 30)), pygame.Rect((self.x - 30, self.y - 30), (30, 30))]
        self.stop = False
    
    def update(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x, self.body[i].y = self.body[i - 1].x, self.body[i - 1].y
        self.body[0].x += self.x_dir * 30
        self.body[0].y += self.y_dir * 30

        # is snake dead
        for element in range(1, len(self.body)):
            if self.body[0].x == self.body[element].x and self.body[0].y == self.body[element].y:
                self.stop = True
            if self.body[0].x not in range(0, 600) or self.body[0].y not in range(0, 600):
                self.stop = True
            if self.stop:
                screen.blit(game_over, (200, 150))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                exit()

        # drawing snake
        for element in self.body:
            pygame.draw.rect(screen, "blue", element)

class Apple:
    def __init__(self):
        self.x = random.randrange(0, 600, 30)
        self.y = random.randrange(0, 600, 30)
        self.width = random.randrange(10, 40)
        self.rect = pygame.Rect((self.x, self.y), (self.width, self.width))
    
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)

snake = Snake()
apple = Apple()

# apple disappering after 10 second
pygame.time.set_timer(pygame.USEREVENT, 10000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.x_dir = 1
                snake.y_dir = 0
            elif event.key == pygame.K_LEFT:
                snake.x_dir = -1
                snake.y_dir = 0
            elif event.key == pygame.K_UP:
                snake.y_dir = -1
                snake.x_dir = 0
            elif event.key == pygame.K_DOWN:
                snake.y_dir = 1
                snake.x_dir = 0
        if event.type == pygame.USEREVENT:
            apple = Apple()
    
    screen.fill("black")
    score = font.render(f"{len(snake.body)}", True, "white")
    screen.blit(score, (5, 5))
    level = font.render(f"{status}", True, "white")
    screen.blit(level, (580, 5))
    snake.update()
    apple.update()

    # is snake eat apple
    if snake.body[0].x == apple.x and snake.body[0].y == apple.y:
        snake.body.append(pygame.Rect((apple.x, apple.y), (30, 30)))
        apple = Apple()
    
    #Level 1
    if len(snake.body) > 3 and len(snake.body) < 9:
        rect1 = pygame.Rect((300, 300), (60, 210))
        status = 1
        FPS = 14
        for element in snake.body:
            if not (element.colliderect(rect1)):
                pygame.draw.rect(screen, "#1d1d1d", rect1)
            else:
                screen.blit(game_over, (200, 150))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                exit()
    
    #Level 2
    if len(snake.body) > 8:
        status = 2
        FPS = 18
        rect1 = pygame.Rect((200, 100), (120, 60))
        rect2 = pygame.Rect((500, 300), (30, 120))
        for element in snake.body:
            if not (element.colliderect(rect1) or element.colliderect(rect2)):
                pygame.draw.rect(screen, "#1d1d1d", rect1)
                pygame.draw.rect(screen, "#1d1d1d", rect2)
            else:
                screen.blit(game_over, (200, 150))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                exit()

    pygame.display.flip()
    clock.tick(10)