import pygame


size = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Перетаскивание')
clock = pygame.time.Clock()
color = (0, 255, 0)
xt = yt = 0
running = True
move = False

while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, (xt, yt, 100, 100), 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = x, y = event.pos
            if xt <= x <= xt + 100 and yt <= y <= yt + 100 and not move:
                move = True
                xd, yd = x - xt, y - yt
        if event.type == pygame.MOUSEMOTION and move:
            pos = x, y = event.pos
            xt = x - xd
            yt = y - yd
        if event.type == pygame.MOUSEBUTTONUP and move:
            pos = x, y = event.pos
            move = False
            xt = x - xd
            yt = y - yd
            xd = yd = 0

        pygame.draw.rect(screen, color, (xt, yt, 100, 100), 0)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
