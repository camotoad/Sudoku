import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pygame, sys
from Solver import solve, valid, find_empty, print_board
import time
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 80)
font3 = pygame.font.SysFont("comicsans", 30)

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
    clicked = False

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
                Tk().wm_withdraw()
                messagebox.showinfo('Notice', 'Under Construction')
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
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    key = 0
                # if event.key == pygame.K_SPACE:  # used for debug
                #     board.clean()
                #     board.update_model()
                #     print_board(board.model)
            try:
                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse selects a box
                    pos = pygame.mouse.get_pos()
                    clicked = board.click(pos)
                    if clicked:
                        board.select(clicked[0], clicked[1])
                        key = None
                    elif board.clearclick(pos):
                        board.clean()
                        board.update_model()
                        key = 0
                    elif board.solveclick(pos):
                        if board.validate():    # have to check before solving or else the program will hang
                            if solve(board.model):
                                board.solve()
                                key = None
                            else:
                                Tk().wm_withdraw()
                                messagebox.showinfo('Notice', 'This puzzle is not solvable')
                        else:
                            Tk().wm_withdraw()
                            messagebox.showinfo('Notice', 'This puzzle is not solvable')
            finally:
                pass

        if board.selected and key is not None:
            board.place(key)

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
            text = font.render(str(self.value), True, color_black)
            win.blit(text,
                     (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))  # drawing numbers
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
        self.buttonsolve = pygame.Rect(300, 550, 150, 35)  # menu buttons
        self.buttonclear = pygame.Rect(90, 550, 150, 35)

    def update_model(self):  # updating the board
        self.model = [[self.box[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def clean(self):  # clear board
        for i in range(self.rows):
            for j in range(self.cols):
                self.box[i][j].value = 0

    def place(self, value):  # putting new numbers in
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

        for i in range(self.rows):  # drawing boxes
            for j in range(self.cols):
                self.box[i][j].draw(win)

        pygame.draw.rect(win, color_red, self.buttonsolve)
        pygame.draw.rect(win, color_red, self.buttonclear)
        solvetext = font3.render('Solve Puzzle', True, color_black)
        cleartext = font3.render('Clear Board', True, color_black)
        solverect = solvetext.get_rect(center=(self.buttonsolve.left + (self.buttonsolve.width / 2),
                                               self.buttonsolve.top + (self.buttonsolve.height / 2) + 2))

        clearrect = cleartext.get_rect(center=(self.buttonclear.left * 2 - (self.buttonclear.width / 10),
                                               self.buttonclear.top + (self.buttonclear.height / 2) + 2))
        win.blit(solvetext, solverect)
        win.blit(cleartext, clearrect)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.box[i][j].selected = False  # deselect all boxes

        self.box[row][col].selected = True  # select new box
        self.selected = (row, col)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:  # clicks are within the game screen
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))
        else:
            return None

    def clearclick(self, pos):
        if self.buttonclear.collidepoint(pos[0], pos[1]):
            return True
        else:
            return False

    def solveclick(self, pos):
        if self.buttonsolve.collidepoint((pos[0], pos[1])):
            return True
        else:
            Tk().wm_withdraw()
            messagebox.showinfo('Notice', 'This puzzle is not solvable')

    def solve(self):
        if solve(self.model):
            # print_board(self.model)
            self.board = self.model.copy()
            # print_board(self.box)
            for i in range(self.rows):  # drawing boxes
                for j in range(self.cols):
                    self.box[i][j].set(self.board[i][j])
            self.update_model()
            # print_board(self.model)
            # print("draw")

    def validate(self):
        self.update_model()
        # print_board(self.model)
        for i in range(self.rows):
            for j in range(self.cols):
                if self.model[i][j] != 0:
                    if valid(self.model, self.model[i][j], (i, j)):
                        pass
                        # print(self.model[i][j])
                    else:
                        return False
        return True


def redraw_solver(win, board):
    win.fill(color_white)
    board.draw(win)


main_menu()
