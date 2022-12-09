import pygame
from random import randrange


class Board:
    # создание поля
    def __init__(self, width, height, left=20, top=20, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # прорисовка поля квадратами
    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        j, i = (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
        if 0 <= j < self.width and 0 <= i < self.height:
            return j, i
        else:
            return None

    # что делаем
    def on_click(self, cell):
        pass

    # текущие координаты
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Minesweeper(Board):
    def __init__(self, n, width, height, left=20, top=20, cell_size=30):
        super().__init__(width, height, left, top, cell_size)
        self.n = n
        for _ in range(self.n):
            i, j = randrange(self.height), randrange(self.width)
            self.board[i][j] = -2

    def on_click(self, cell):
        x, y = cell
        if self.board[y][x] == -1:
            self.open_cell(cell)

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == -2:
                    pygame.draw.rect(screen, (255, 0, 0),
                                     (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
                if self.board[i][j] >= 0:
                    font = pygame.font.Font(None, self.cell_size)
                    text = font.render(str(self.board[i][j]), 1, (0, 255, 0))
                    screen.blit(text, (j * self.cell_size + self.left + 10, i * self.cell_size + self.top + 10))

    def open_cell(self, cell):
        j, i = cell

        s = 0
        for dj in (-1, 0, 1):
            for di in (-1, 0, 1):
                if 0 <= i + di < self.height and 0 <= j + dj < self.width and self.board[i + di][j + dj] == -2:
                    s += 1
        self.board[i][j] = s
        if s == 0:
            for dj in (-1, 0, 1):
                for di in (-1, 0, 1):
                    if 0 <= i + di < self.height and 0 <= j + dj < self.width and self.board[i + di][j + dj] == -1:
                        self.open_cell((j + dj, i + di))


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    size = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Папа сапёра')
    screen.fill((0, 0, 0))
    board = Minesweeper(20, 16, 16)
    board.set_view(25, 25, 40)

    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # клик левой кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)


        screen.fill((0, 0, 0))
        board.render(screen)

        clock.tick(50)
        pygame.display.flip()

    pygame.quit()
