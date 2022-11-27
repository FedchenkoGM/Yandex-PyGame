import pygame

if __name__ == '__main__':
    fps = 60  # количество секунд
    v = 10    # пикселей в секунду
    clock = pygame.time.Clock()
    pygame.init()
    size = w, h = 600, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Желтый круг')
    screen.fill((0, 0, 255))

    running = True
    r = 0
    drawing = False  # режим рисования выключен
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                pos = event.pos
                r = 0
                screen.fill((0, 0, 255))
        if drawing:
            pygame.draw.circle(screen, (255, 255, 0), pos, r)
            r += v * 5 / fps
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
