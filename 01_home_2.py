import pygame
import sys

def draw_rhombus(screen, n):
    a = screen.get_size()[0]
    for x in range(0, a - n + 1, n):
        for y in range(0, a - n + 1, n):
            pygame.draw.polygon(screen, (255, 150, 0),
                                [[x + n // 2, y], [x + n - 1, y + n // 2],
                                 [x + n // 2, y + n - 1], [x, y + n // 2]])


if __name__ == '__main__':
    data = sys.stdin.readlines()
    if not data or len(data) > 1:
        print('Неправильный формат ввода')
        exit()
    else:
        n = data[0].strip()
        if not n.isdigit():
            print('Неправильный формат ввода')
            exit()
        else:
            pygame.init()
            n = int(n)
            size = 300, 300
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Ромбики')
            screen.fill((255, 255, 0))

            draw_rhombus(screen, n)

            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()