import pygame
import sys

def draw_sphere(screen, n):
    a = screen.get_size()[0]
    r = a // 2 // n
    rr = a // 2
    for x in range(0, a // 2 - r + 1, r):
        pygame.draw.ellipse(screen, (255, 255, 255), (0, x, a, 2 * rr), 1)
        pygame.draw.ellipse(screen, (255, 255, 255), (x, 0, 2 * rr, a), 1)
        rr -= r


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
            pygame.display.set_caption('Сфера')

            draw_sphere(screen, n)

            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()