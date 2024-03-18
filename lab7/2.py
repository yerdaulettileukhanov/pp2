import pygame, os
from sys import exit

music_list = os.listdir("music")
cnt = 0
playing = True

pygame.init()
screen = pygame.display.set_mode((300, 100))
pygame.mixer.music.load("music/" + music_list[cnt])
pygame.mixer.music.play()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and (cnt < len(music_list)):
                if cnt == len(music_list) - 1:
                    cnt = 0
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/" + music_list[cnt])
                    pygame.mixer.music.play()
                else:
                    cnt += 1
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/" + music_list[cnt])
                    pygame.mixer.music.play()
            if event.key == pygame.K_LEFT and (cnt >= 0):
                if cnt == 0:
                    cnt = 0
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/" + music_list[cnt])
                    pygame.mixer.music.play()
                else:
                    cnt -= 1
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("music/" + music_list[cnt])
                    pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                playing = not playing
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    pygame.display.flip()
    clock.tick(60)