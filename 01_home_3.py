import pygame


def draw_bricks(screen):
    for y in range(0, 200 - 15, 34):
        for x in range(0, 300, 32):
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 30, 15), 0)
            pygame.draw.rect(screen, (255, 0, 0), (x - 16, y + 17, 30, 15), 0)


if __name__ == '__main__':
        pygame.init()
        size = 300, 200
        screen = pygame.display.set_mode(size)
        screen.fill((255, 255, 255))
        pygame.display.set_caption('Кирпичи')

        draw_bricks(screen)

        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()