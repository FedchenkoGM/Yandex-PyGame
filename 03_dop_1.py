import pygame
from random import choice


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.field = [[choice([1,2]) for __ in range(width)]  for _ in range(height)]
        self.player = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # прорисовка поля квадратами
    def render(self, screen):
        colors = ['blue', 'red']
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
                ind = self.field[i][j] - 1
                x0, y0 = self.left + (2 * j + 1) * self.cell_size // 2, self.top + (2 * i + 1) * self.cell_size // 2
                pygame.draw.circle(screen, colors[ind],
                                 (x0, y0), self.cell_size // 2 - 2)


    # координаты клетки
    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        j, i = (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
        if 0 <= j < self.width and 0 <= i < self.height:
            return j, i
        else:
            return None

    # что делаем
    def on_click(self, cell):
        x, y = cell
        for i in range(self.height):
            self.field[i][x] = self.player
        for j in range(self.width):
            self.field[y][j] = self.player
        self.player =(self.player + 1) % 2
#        print('==============\n', *self.field, sep='\n')

    # текущие координаты в консоль
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


if __name__ == '__main__':
    n = int(input())
    print('ход красными')
    pygame.init()
    size = w, h = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Недореверси')
    screen.fill((0, 0, 0))
    board = Board(n, n)
    board.set_view(50, 50, 500 // n)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
