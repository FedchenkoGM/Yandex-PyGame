import pygame
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width, height, left=20, top=20, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
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

    # текущие координаты в консоль
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Life(Board):
    def __init__(self, width, height, left=20, top=20, cell_size=30):
        super().__init__(width, height, left, top, cell_size)

    def on_click(self, cell):
        x, y = cell
        self.board[y][x] = (self.board[y][x] + 1) % 2

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    pygame.draw.rect(screen, (0, 255, 0),
                                     (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def next_move(self):
        tmp = deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                s = 0
                for dj in (-1, 0, 1):
                    for di in (-1, 0, 1):
                        s += self.board[(i + di) % self.height][(j + dj) % self.width]
                s -= self.board[i][j]
                if s == 3:
                    tmp[i][j] = 1
                elif s < 2 or s > 3:
                    tmp[i][j] = 0
        self.board = deepcopy(tmp)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    size = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Жизнь на Торе')
    screen.fill((0, 0, 0))
    board = Life(22, 22)
    board.set_view(20, 20, 30)

    running = True
    life = False
    ticks = 0
    fps = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # клик левой кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            # пробел или клик правой кнопки мыши
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or \
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                life = not life
            # ускорить
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                fps += 1
            # замедлить
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                fps -= 1

        screen.fill((0, 0, 0))
        board.render(screen)
        if fps < 1:
            fps = 1

        if life:
            board.next_move()
            clock.tick(fps)
            print(fps)

        pygame.display.flip()

    pygame.quit()
