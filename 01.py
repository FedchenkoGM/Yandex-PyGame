import os
import pygame

pygame.init()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)


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

class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # РІС‹С‡РёСЃР»СЏРµРј РјР°СЃРєСѓ РґР»СЏ СЌС„С„РµРєС‚РёРІРЅРѕРіРѕ СЃСЂР°РІРЅРµРЅРёСЏ
        self.mask = pygame.mask.from_surface(self.image)
        # СЂР°СЃРїРѕР»Р°РіР°РµРј РіРѕСЂС‹ РІРЅРёР·Сѓ
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = load_image("star.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # РІС‹С‡РёСЃР»СЏРµРј РјР°СЃРєСѓ РґР»СЏ СЌС„С„РµРєС‚РёРІРЅРѕРіРѕ СЃСЂР°РІРЅРµРЅРёСЏ
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        # РµСЃР»Рё РµС‰Рµ РІ РЅРµР±Рµ
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


# РіСЂСѓРїРїР°, СЃРѕРґРµСЂР¶Р°С‰Р°СЏ РІСЃРµ СЃРїСЂР°Р№С‚С‹
all_sprites = pygame.sprite.Group()

mountain = Mountain()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Landing(event.pos)
    screen.fill(pygame.Color("black"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)
pygame.quit()