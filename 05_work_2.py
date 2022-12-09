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


class Creature(pygame.sprite.Sprite):
    def __init__(self, d):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("creature.png")
        self.rect = self.image.get_rect()
 #       self.rect.left, self.rect.top = 0, 0
        self.d = d

    def up(self):
        self.rect.top -= self.d

    def down(self):
        self.rect.top += self.d

    def left(self):
        self.rect.left -= self.d

    def right(self):
        self.rect.right += self.d


def main():
    pygame.init()
    size = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Герой двигается!')
    all_sprites = pygame.sprite.Group()
    hero = Creature(10)
    all_sprites.add(hero)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_DOWN]:
                hero.down()
            if key[pygame.K_UP]:
                hero.up()
            if key[pygame.K_LEFT]:
                hero.left()
            if key[pygame.K_RIGHT]:
                hero.right()

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

