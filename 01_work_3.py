import pygame
import sys

def draw_chess(screen, b):
#   красный квадрат
    w = screen.get_size()[0]
    d = b % 2
    a = w // b
    for y in range(0, w, a):
        for x in range(0 + d * a, w, 2 * a):
            pygame.draw.rect(screen, (255, 255, 255), (x, y, a, a), 0)
        d = (d + 1) % 2



if __name__ == '__main__':
    data = sys.stdin.readlines()
    if not data or len(data) > 1 or data[0].strip().count(' ') != 1 :
        print('Неправильный формат ввода')
        exit()
    else:
        a, b = data[0].strip().split()
        if not a.isdigit() or not b.isdigit():
            print('Неправильный формат ввода')
            exit()
        else:
            pygame.init()
            size = int(a), int(a)
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Шахматная клетка')

            draw_chess(screen, int(b))

            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()