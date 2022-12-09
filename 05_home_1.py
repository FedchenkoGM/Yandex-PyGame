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


class Car(pygame.sprite.Sprite):
    def __init__(self, size, d):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = load_image("car.png")
        self.image2 = pygame.transform.flip(self.image1, True, False)
        self.image = self.image1
        self.width, self.height = size
        self.rect = self.image.get_rect()
        self.d = d

    def update(self):
        if self.rect.left < 0 or self.rect.left > self.width - self.image.get_width():
            self.d = -self.d
            if self.d > 0:
                self.image = self.image1
            else:
                self.image = self.image2
        self.rect.left += self.d

def main():
    pygame.init()
    size = 600, 95
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Машинка')
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    car = Car(size, 2)
    all_sprites.add(car)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        car.update()

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


if __name__ == '__main__':
    main()

