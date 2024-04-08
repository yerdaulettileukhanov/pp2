import pygame

queue = []
colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
cnt = 0

def getRectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    w = abs(x1-x2)
    h = abs(y1-y2)
    return (x, y, w, h)

def step(screen, x, y, origin_color, fill_color):
    if x < 0 or y < 0: return False
    if x > 400 or y > 300: return False
    if screen.get_at((x, y)) != origin_color: return False
    queue.append((x, y))
    screen.set_at((x, y), fill_color)

pygame.init()
screen = pygame.display.set_mode((400, 300))
another_layer = pygame.Surface((400, 300))

done = False
clock = pygame.time.Clock()

origin_color = (0, 0, 0)
fill_color = (255, 0, 0)

tool = 0
#0 - pencil
#1 - rectangle
#3 - fill
#2 - eraser
#4 - circle

tools_count = 5

x1 = 10
y1 = 10
x2 = 10
y2 = 10

radius = 10

w = 100
h = 100
color = (0, 128, 255)
isMouseDown = False
screen.fill((0, 0, 0))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        cnt += 1
                        if cnt == len(colors):
                            cnt = 0
                    if event.key == pygame.K_LEFT:
                        cnt -= 1
                        if cnt < 0:
                            cnt = len(colors) - 1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click
                        if tool == 0:
                            x1 = event.pos[0]
                            y1 = event.pos[1]
                            x2 = x1
                            y2 = y1
                        elif tool == 3:
                            x1_er = event.pos[0]
                            y1_er = event.pos[1]
                            x2_er = x1_er
                            y2_er = y1_er
                        elif tool == 1:
                            x1 = event.pos[0]
                            y1 = event.pos[1]
                        elif tool == 4:
                            x1_cr = event.pos[0]
                            y1_cr = event.pos[1]
                        elif tool == 2:
                            x1 = event.pos[0]
                            y1 = event.pos[1]
                            origin_color = screen.get_at((x1, y1))
                            queue.append((x1, y1))
                            screen.set_at((x1, y1), colors[cnt])

                            while len(queue) > 0:
                                cur_pos = queue[0]
                                queue.pop(0)
                                step(screen, cur_pos[0] + 1, cur_pos[1], origin_color,  colors[cnt])
                                step(screen, cur_pos[0] - 1, cur_pos[1], origin_color, colors[cnt])
                                step(screen, cur_pos[0], cur_pos[1] + 1, origin_color, colors[cnt])
                                step(screen, cur_pos[0], cur_pos[1] - 1, origin_color, colors[cnt])
                                
                    elif event.button == 3: # right click
                        tool = (tool + 1) % tools_count
                    isMouseDown = True


                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        another_layer.blit(screen, (0, 0))
                    isMouseDown = False
                    
                if event.type == pygame.MOUSEMOTION:
                        if isMouseDown:
                            if tool == 0:
                                x1 = x2
                                y1 = y2
                                x2 = event.pos[0]
                                y2 = event.pos[1]
                                pygame.draw.line(screen, colors[cnt], (x1, y1), (x2, y2))
                            elif tool == 3:
                                x1_er = x2_er
                                y1_er = y2_er
                                x2_er = event.pos[0]
                                y2_er = event.pos[1]
                                pygame.draw.line(screen, (0, 0, 0), (x1_er, y1_er), (x2_er, y2_er))
                            elif tool == 1:
                                screen.blit(another_layer, (0, 0))
                                x2 = event.pos[0]
                                y2 = event.pos[1]
                                pygame.draw.rect(screen, colors[cnt], pygame.Rect(getRectangle(x1, y1, x2, y2)), 1)
                            elif tool == 4:
                                x2_cr = event.pos[0]
                                radius = abs(x2_cr - x1_cr)
                                screen.blit(another_layer, (0, 0))
                                pygame.draw.circle(screen, colors[cnt], (x1_cr, y1_cr), radius)
                        
        pygame.display.flip()
        clock.tick(60)