import pygame, sys
from Solver import solve, valid, find_empty
import time
from pygame.locals import *
mainClock = pygame.time.Clock()
pygame.font.init()
pygame.display.set_caption('Main Menu')


board = [
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def main_menu():
    screen = pygame.display.set_mode((300, 250), 0, 32)
    pygame.display.set_caption('Main Menu')
    while True:

        screen.fill((255, 255, 255))

        mx, my = pygame.mouse.get_pos()

        buttonsolve = pygame.Rect(50, 100, 200, 50)

        if buttonsolve.collidepoint((mx, my)):
            if click:
                solve_window()
                # pass
        pygame.draw.rect(screen, (255, 0, 0), buttonsolve)

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
    screen2 = pygame.display.set_mode((540, 600), 0, 32)
    pygame.display.set_caption('Solver')
    screen2.fill((255, 255, 255))
    draw(screen2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def draw(win):
    for i in range(1, 540):  # drawing vertical lines
        if i % 180 == 0:
            pygame.draw.line(win, (0, 0, 0), (i, 0), (i, 540), width=3)
        elif i % 60 == 0 or i == 480:
            pygame.draw.line(win, (0, 0, 0), (i, 0), (i, 540), width=1)

    for j in range(1, 600):  # drawing horizontal lines
        if j % 180 == 0 or j == 600:
            pygame.draw.line(win, (0, 0, 0), (0, j), (540, j), width=3)
        elif j % 60 == 0 or j == 540:
            pygame.draw.line(win, (0, 0, 0), (0, j), (540, j), width=1)


main_menu()