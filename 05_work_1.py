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


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("arrow.png")
        self.rect = self.image.get_rect()
        self.rect = pygame.mouse.get_pos()

    def update(self):
        self.rect = pygame.mouse.get_pos()


def main():
    pygame.init()
    size = w, h = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Свой курсор мыши')
    screen.fill((0, 0, 0))
    all_sprites = pygame.sprite.Group()
    sprite = Arrow()
    all_sprites.add(sprite)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                all_sprites.update()
        screen.fill((0, 0, 0))
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()

