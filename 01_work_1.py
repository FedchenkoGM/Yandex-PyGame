import sys
import pygame

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
            pygame.display.set_caption('Крест')
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, pygame.Color('white'), (0, 0), (w, h), width=5)
            pygame.draw.line(screen, pygame.Color('white'), (0, h), (w, 0), width=5)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                pygame.display.flip()
            pygame.quit()