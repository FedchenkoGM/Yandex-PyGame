import sys
import os
import pygame
from random import randrange


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


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group, size=(500, 500)):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image_boom = load_image("boom.png")
        self.image = load_image("bomb.png")
        self.rect = self.image.get_rect()
        width, height = size
        self.rect.x = randrange(width - self.image.get_rect().width)
        self.rect.y = randrange(height - self.image.get_rect().height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom

def main():
    pygame.init()
    size = 500, 500
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Boom them all')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    for _ in range(20):
        Bomb(all_sprites, size=size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


if __name__ == '__main__':
    main()

