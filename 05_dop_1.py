import sys
import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Gameover(pygame.sprite.Sprite):
    def __init__(self, size, d):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("gameover.png")
        self.width, self.height = size
        self.rect = self.image.get_rect()
        self.rect.left = -self.rect.width
        self.d = d

    def update(self):
        if self.rect.left == 0:
            self.d = 0
        self.rect.left += self.d

def main():
    pygame.init()
    size = 600, 300
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 255))
    pygame.display.set_caption('Game over')

    clock = pygame.time.Clock()
    fps = 50
    v = 200

    all_sprites = pygame.sprite.Group()
    gameover = Gameover(size, v // fps)
    all_sprites.add(gameover)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gameover.update()

        screen.fill((0, 0, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()

