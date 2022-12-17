import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, all_sprites, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
# добавить в последнюю очередь
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx

    def move(self, vx, vy):
        self.rect.left += vx
        self.rect.top += vy

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, all_sprites, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


def main():
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Balls')
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    all_sprites_border = pygame.sprite.Group()

    Border(all_sprites_border, 5, 5, width - 5, 5)
    Border(all_sprites_border, 5, height - 5, width - 5, height - 5)
    Border(all_sprites_border, 5, 5, 5, height - 5)
    Border(all_sprites_border, width - 5, 5, width - 5, height - 5)

    all_sprites_ball = pygame.sprite.Group()

    for i in range(10):
        Ball(all_sprites_ball, 20, 100, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))

        all_sprites_ball.draw(screen)
        all_sprites_ball.update()
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


if __name__ == '__main__':
    main()