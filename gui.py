import sys

from main import *

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
input_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0]]
import pygame
import copy

def check_if_solved():
    global temp
    temp = copy.deepcopy(board)
    repeating_searches(temp)
    if temp == input_board:
        return True
    else:
        return False


grid = pygame.image.load('grid.png')
red = pygame.image.load('red.png')
bg = pygame.image.load('bg.png')
pygame.init()
font = pygame.font.Font('font.ttf', 30)
font_2 = pygame.font.Font('font.ttf', 25)
screen = pygame.display.set_mode((600, 600))


def reset():
    for i in range(9):
        for j in range(9):
            input_board[i][j] = 0


def draw_text(text, font, color, surface, x, y):
    textObj = font.render(text, 1, color)
    text_rect = textObj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(textObj, text_rect)


click = False
solved_ = pygame.image.load('solved.png')


def solved():
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(solved_, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



def main_menu():
    global temp, input_board, board
    global click
    color_1 = (255, 255, 255)
    color_2 = (255, 255, 255)
    while True:
        board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        temp = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        input_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        screen.blit(bg, (0, 0))
        draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        pygame.draw.rect(screen, color_1, button_1)
        pygame.draw.rect(screen, color_2, button_2)
        mx, my = pygame.mouse.get_pos()
        if button_1.collidepoint(mx, my):
            color_1 = (70, 70, 70)
            if click:
                game()
        else:
            color_1 = (255, 255, 255)
        if button_2.collidepoint(mx, my):
            color_2 = (70, 70, 70)
            if click:
                solver()
        else:
            color_2 = (255, 255, 255)
        draw_text('Solver', font, (0, 0, 0), screen, 60, 210)
        draw_text('Play Sudoku', font, (0, 0, 0), screen, 60, 100)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            pygame.display.update()


def determine_indices(pos_x, pos_y):
    if pos_x == 25 and pos_y == 24:
        return [0, 0]
    if pos_x == 25:
        return [int((pos_y - 24) / 63) + 1, 0]
    if pos_y == 24:
        return [0, int((pos_x - 25) / 63) + 1]
    indices = [int((pos_y - 24) / 63) + 1, int((pos_x - 25) / 63) + 1]
    print(pos_x, pos_y)
    print(indices)
    return indices

def not_solved():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('NOT SOLVED YET, "ESC" TO GO BACK', font, (255, 255, 255), screen, 60, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()

def game():
    global input_board
    pressed_return = False
    running = True
    generate_random_board(board)
    for i in range(8):
        for j in range(8):
            input_board[i][j] = board[i][j]
    pos_x, pos_y = 30, 35
    red_x = 25
    red_y = 24
    while running:
        mx, my = pygame.mouse.get_pos()
        screen.fill((255, 255, 255))
        screen.blit(grid, (0, 0))
        screen.blit(red, (red_x, red_y))
        draw_text('Press "s" for the solution, "r" to reset, "0" to erase, "c" to check', font_2, (255, 0, 255), screen, 20,
                  -7)
        draw_text('Press esc to go back to the menu', font_2, (0, 255, 0), screen, 180, 570)
        pos_y = 35
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    draw_text(str(board[i][j]), font, (255, 0, 0), screen, pos_x, pos_y)
                elif input_board[i][j] != 0:
                    draw_text(str(input_board[i][j]), font, (0, 0, 0), screen, pos_x, pos_y)
                pos_x += 63
            pos_x = 30
            pos_y += 63
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    reset()
                if event.key == pygame.K_RIGHT:
                    red_x += 61
                    if red_x >= 513:
                        red_x = 513
                if event.key == pygame.K_DOWN:
                    red_y += 61
                    if red_y >= 512:
                        red_y = 512
                if event.key == pygame.K_LEFT:
                    red_x -= 61
                    if red_x <= 25:
                        red_x = 25
                if event.key == pygame.K_UP:
                    red_y -= 61
                    if red_y <= 24:
                        red_y = 24
                if event.key == pygame.K_s:
                    reset()
                    repeating_searches(board)
                    input_board = board
                if event.key == pygame.K_RETURN:
                    pressed_return = True
                    [x, y] = determine_indices(red_x, red_y)
                if event.key == pygame.K_c:
                    if check_if_solved():
                        solved()
                    else:
                        not_solved()
                if pressed_return and event.type == pygame.KEYDOWN and 47 < event.key <= 57:
                    number_entered = event.key - 48
                    input_board[x][y] = number_entered
                    print(input_board[x][y])
        pygame.display.update()


def solver():
    x, y = 0, 0
    red_x, red_y = 24, 25
    solve_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
    running = True
    mouse_click = False
    pressed_return = False
    pos_x = 30
    while running:

        screen.fill((255, 255, 255))
        screen.blit(grid, (0, 0))
        screen.blit(red, (red_x, red_y))
        draw_text('Press "s" to solve', font_2, (255, 0, 0), screen, 200, -7)
        pos_y = 35
        for i in range(9):
            for j in range(9):
                if solve_array[i][j] != 0:
                    draw_text(str(solve_array[i][j]), font, (0, 0, 0), screen, pos_x, pos_y)
                pos_x += 63
            pos_x = 30
            pos_y += 63
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pressed_return = True
                if pressed_return and event.type == pygame.KEYDOWN and 47 < event.key <= 57:
                    number_entered = event.key - 48
                    solve_array[x][y] = number_entered
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    reset()
                if event.key == pygame.K_RIGHT:
                    if red_x < 480:
                        y += 1
                        red_x += 61
                if event.key == pygame.K_DOWN:
                    if red_y < 480:
                        x += 1
                        red_y += 61
                if event.key == pygame.K_LEFT:
                    if red_x >= 25:
                        y -= 1
                        red_x -= 61
                if event.key == pygame.K_UP:
                    if red_y >= 25:
                        x -= 1
                        red_y -= 61
                if event.key == pygame.K_s:
                    repeating_searches(solve_array)
        pygame.display.update()


main_menu()
