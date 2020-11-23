import pygame, sys
from Solver import solve, valid, find_empty
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

pygame.display.set_caption('Main Menu')


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

def drawtext(text, font, color, win, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    win.blit(textobj, textrect)


click = False


def main_menu():
    screen = pygame.display.set_mode((300, 250), 0, 32)
    pygame.display.set_caption('Main Menu')
    buttonsolve = pygame.Rect(50, 100, 200, 50)
    buttonplay = pygame.Rect(50, 175, 200, 50)

    while True:
        screen.fill(color_white)
        pygame.draw.rect(screen, (255, 0, 0), buttonsolve)
        pygame.draw.rect(screen, (255, 0, 0), buttonplay)

        drawtext('Puzzle Solver', font, color_black, screen, buttonsolve.left + 5, buttonsolve.bottom / 2 + 37)
        drawtext('Play a Game', font, color_black, screen, buttonplay.left + 17, buttonplay.centery - 10)
        drawtext('Sudoku', font2, color_black, screen, 45, 25)
        pygame.display.update()

        mx, my = pygame.mouse.get_pos()

        if buttonsolve.collidepoint((mx, my)):
            if click:
                solve_window()
                # pass
        if buttonplay.collidepoint((mx, my)):
            if click:
                pass
        click = False
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
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def solve_window():
    pygame.display.init()
    screen2 = pygame.display.set_mode((540, 600), 0, 32)
    pygame.display.set_caption('Solver')
    screen2.fill(color_white)
    draw(screen2)

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

        pygame.display.update()
        mainClock.tick(60)


def draw(win):
    for i in range(1, 540):  # drawing vertical lines
        if i % 180 == 0:
            pygame.draw.line(win, color_black, (i, 0), (i, 540), width=3)
        elif i % 60 == 0 or i == 480:
            pygame.draw.line(win, color_black, (i, 0), (i, 540), width=1)

    for j in range(1, 600):  # drawing horizontal lines
        if j % 180 == 0 or j == 600:
            pygame.draw.line(win, color_black, (0, j), (540, j), width=3)
        elif j % 60 == 0 or j == 540:
            pygame.draw.line(win, color_black, (0, j), (540, j), width=1)


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

main_menu()