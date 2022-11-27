import pygame
from random import choice


class Ball:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = choice([-1, 1])
        self.dy = choice([-1, 1])

    def move(self, d):
        if self.x <= self.radius + d or self.x >= width - self.radius - d:
            self.dx = - self.dx
        if self.y <= self.radius + d or self.y >= height - self.radius - d:
            self.dy = -self.dy
        self.x += (self.dx * d)
        self.y += (self.dy * d)

    def draw(self, scr):
        pygame.draw.circle(scr, self.color, (self.x, self.y), self.radius)



size = width, height = 601, 401
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Шарики')
clock = pygame.time.Clock()
screen2 = pygame.Surface(screen.get_size())

count = 0
running = True
balls = []

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = x, y =event.pos
            balls.append(Ball(x, y, (200, 100, 200), 20))

    screen2.fill(pygame.Color("black"))
    for ball in balls:
        ball.draw(screen2)
    screen.blit(screen2, (0, 0))

    pygame.display.flip()

    for ball in balls:
        ball.move(2)

    clock.tick(50)

pygame.quit()
