import pygame, sys
from Solver import solve, valid, find_empty, print_board
import time
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 80)

# colours
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)

pygame.display.set_caption('Main Menu')


def drawtext(text, font, color, win, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    win.blit(textobj, textrect)


def main_menu():
    screen = pygame.display.set_mode((300, 250), 0, 32)
    pygame.display.set_caption('Main Menu')
    buttonsolve = pygame.Rect(50, 100, 200, 50)
    buttonplay = pygame.Rect(50, 175, 200, 50)

    while True:
        screen.fill(color_white)
        pygame.draw.rect(screen, color_red, buttonsolve)
        pygame.draw.rect(screen, color_red, buttonplay)

        drawtext('Puzzle Solver', font, color_black, screen, buttonsolve.left + 5, buttonsolve.bottom / 2 + 37)
        drawtext('Play a Game', font, color_black, screen, buttonplay.left + 17, buttonplay.centery - 10)
        drawtext('Sudoku', font2, color_black, screen, 45, 25)
        pygame.display.update()

        mx, my = pygame.mouse.get_pos()

        if buttonsolve.collidepoint((mx, my)):
            if clicked:
                solve_window()
                # pass
        if buttonplay.collidepoint((mx, my)):
            if clicked:
                pass
        clicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        pygame.display.update()
        mainClock.tick(60)


def solve_window():
    pygame.display.init()
    screen2 = pygame.display.set_mode((540, 600), 0, 32)
    pygame.display.set_caption('Solver')
    screen2.fill(color_white)
    board = Grid(9, 9, 540, 540)
    key = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # pygame.quit()
                    pygame.display.set_mode((300, 250), 0, 32)
                    running = False
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    key = 0
                if event.key == pygame.K_SPACE:
                    board.update_model()
                    print_board(board.model)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.place(key)
            # print_board(board.board)

        redraw_solver(screen2, board)
        pygame.display.update()
        mainClock.tick(60)


class Box:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        # self.temp = 0

    def draw(self, win):
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.value != 0:
            text = font.render(str(self.value), True, color_black)  # drawtext(text, font, color, win, x, y)
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if self.selected:
            pygame.draw.rect(win, color_red, (x, y, gap, gap), 3)

    def set(self, value):
        self.value = value


class Grid:
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.box = [[Box(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):     # updating the board
        self.model = [[self.box[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, value):     # putting new numbers in
        row, col = self.selected
        self.box[row][col].set(value)
        self.update_model()

    def draw(self, win):
        gap = self.width / 9

        for i in range(self.rows + 1):  # drawing lines
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1

            pygame.draw.line(win, color_black, (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(win, color_black, (i * gap, 0), (i * gap, self.height), thick)

        for i in range(self.rows):      # drawing boxes
            for j in range(self.cols):
                self.box[i][j].draw(win)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.box[i][j].selected = False  # deselect all boxes

        self.box[row][col].selected = True  # select new box
        self.selected = (row, col)

    def click(self, pos):
        if pos[0] < self.width and pos [1] < self.height:  # clicks are within the game screen
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None


def redraw_solver(win, board):
    win.fill(color_white)
    board.draw(win)


main_menu()