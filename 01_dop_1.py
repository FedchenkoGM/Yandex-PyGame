import pygame
import sys


if __name__ == '__main__':
    data = sys.stdin.readlines()
    if not data or len(data) > 1 or data[0].strip().count(' ') != 1 :
        print('Неправильный формат ввода')
        exit()
    else:
        w, hue = data[0].strip().split()
        if not w.isdigit() or not hue.isdigit() or int(w) > 100 or int(w) % 4 or int(w) > 360:
            print('Неправильный формат ввода')
            exit()
        else:
            w, hue =  int(w), int(hue)
            pygame.init()
            size = 300, 300
            screen = pygame.display.set_mode(size)
            pygame.display.set_caption('Куб')

            x0 = y0 = (300 - w - w // 2) // 2
            color = pygame.Color(0, 0, 0)
            color.hsva = (hue, 100, 100, 100)
            pygame.draw.polygon(screen, color, ((x0 + w // 2, y0), (x0 + 3 * w // 2, y0),
                                                (x0 + w, y0 + w // 2), (x0, y0 + w // 2)), 0)
            color.hsva = (hue, 100, 50, 100)
            pygame.draw.polygon(screen, color, ((x0 + 3 * w // 2, y0), (x0 + 3 * w // 2, y0 + w),
                                                (x0 + w, y0 + 3 * w // 2), (x0 + w, y0 + w // 2)), 0)
            color.hsva = (hue, 100, 75, 100)
            pygame.draw.rect(screen, color, (x0, y0 + w // 2, w, w), 0)

            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            pygame.quit()