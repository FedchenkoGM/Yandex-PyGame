import pygame
import sys

def draw_chess(screen, w, n):
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    k = (n - 1) % 3
    for r in range(w * n, w - 1, -w):
        pygame.draw.circle(screen, color[k], (w * n, w * n), r)
        k = (k - 1) % 3



if __name__ == '__main__':
    data = sys.stdin.readlines()
    if not data or len(data) > 1 or data[0].strip().count(' ') != 1 :
        print('Неправильный формат ввода')
        exit()
    else:
        w, n = data[0].strip().split()
        if not w.isdigit() or not n.isdigit():
            print('Неправильный формат ввода')
            exit()
        else:
            pygame.init()
            w, n = int(w), int(n)
            size = 2 * w * n, 2 * w * n
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Мишень')

            draw_chess(screen, w, n)

            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()