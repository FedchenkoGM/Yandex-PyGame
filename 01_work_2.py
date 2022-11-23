import pygame
import sys

def draw_square(screen):
#   красный квадрат
    w, h = screen.get_size()
    pygame.draw.rect(screen, (255, 0, 0), (1, 1, w - 2, h - 2), 0)


if __name__ == '__main__':
    data = sys.stdin.readlines()
    if not data or len(data) > 1 or data[0].strip().count(' ') != 1 :
        print('Неправильный формат ввода')
        exit()
    else:
        w, h = data[0].strip().split()
        if not w.isdigit() or not h.isdigit():
            print('Неправильный формат ввода')
            exit()
        else:
            pygame.init()
            size = w, h = int(w), int(h)
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Прямоугольник')

            draw_square(screen)

            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()