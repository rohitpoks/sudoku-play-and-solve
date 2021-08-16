import random

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def generate_random_board(sudoku_board):
    temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    del_list = []
    x = 0
    x = random.choice(temp_list)
    sudoku_board[0][0] = random.randint(1, 9)
    del_list = temp_list.pop(linear_search(temp_list, x))
    x = random.choice(temp_list)
    sudoku_board[1][8] = random.choice(temp_list)
    del_list = temp_list.pop(linear_search(temp_list, x))
    x = random.choice(temp_list)
    sudoku_board[8][5] = random.choice(temp_list)
    del_list = temp_list.pop(linear_search(temp_list, x))
    x = random.choice(temp_list)
    sudoku_board[6][7] = random.choice(temp_list)
    del_list = temp_list.pop(linear_search(temp_list, x))
    x = random.choice(temp_list)
    repeating_searches(sudoku_board)
    for i in range(70):
        sudoku_board[random.randint(0, 8)][random.randint(0, 8)] = 0


def pick_empty_square(sudoku_board):
    for i in range(9):
        for j in range(9):
            if sudoku_board[i][j] == 0:
                return [i, j]
    return ['*', '*']


def check_if_valid(row, column, number, sudoku_board):
    temp_column = (column + 1) % 3
    temp_row = (row + 1) % 3
    for i in range(9):
        if sudoku_board[row][i] == number:
            return False
    for i in range(9):
        if sudoku_board[i][column] == number:
            return False
    if temp_column == 0:
        if sudoku_board[row][column - 1] == number or sudoku_board[row][column - 2] == number:
            return False
        if temp_row == 0:
            if sudoku_board[row - 1][column] == number or sudoku_board[row - 1][column - 1] == number or \
                    sudoku_board[row - 1][column - 2] == number or sudoku_board[row - 2][column] == number or \
                    sudoku_board[row - 2][column - 1] == number or sudoku_board[row - 2][column - 2] == number:
                return False
        if temp_row == 1:
            if sudoku_board[row + 1][column] == number or sudoku_board[row + 1][column - 1] == number or \
                    sudoku_board[row + 1][column - 2] == number or sudoku_board[row + 2][column] == number or \
                    sudoku_board[row + 2][column - 1] == number or sudoku_board[row + 2][column - 2] == number:
                return False
        if temp_row == 2:
            if sudoku_board[row + 1][column] == number or sudoku_board[row + 1][column - 1] == number or \
                    sudoku_board[row + 1][column - 2] == number or sudoku_board[row - 1][column] == number or \
                    sudoku_board[row - 1][column - 1] == number or sudoku_board[row - 1][column - 2] == number:
                return False
    if temp_column == 1:
        if sudoku_board[row][column + 1] == number or sudoku_board[row][column + 2] == number:
            return False
        if temp_row == 0:
            if sudoku_board[row - 1][column] == number or sudoku_board[row - 1][column + 1] == number or \
                    sudoku_board[row - 1][column + 2] == number or sudoku_board[row - 2][column] == number or \
                    sudoku_board[row - 2][column + 1] == number or sudoku_board[row - 2][column + 2] == number:
                return False
        if temp_row == 1:
            if sudoku_board[row + 1][column] == number or sudoku_board[row + 1][column + 1] == number or \
                    sudoku_board[row + 1][column + 2] == number or sudoku_board[row + 2][column] == number or \
                    sudoku_board[row + 2][column + 1] == number or sudoku_board[row + 2][column + 2] == number:
                return False
        if temp_row == 2:
            if sudoku_board[row + 1][column] == number or sudoku_board[row + 1][column + 1] == number or \
                    sudoku_board[row + 1][column + 2] == number or sudoku_board[row - 1][column] == number or \
                    sudoku_board[row - 1][column + 1] == number or sudoku_board[row - 1][column + 2] == number:
                return False
    if temp_column == 2:
        if sudoku_board[row][column + 1] == number or sudoku_board[row][column - 1] == number:
            return False
        if temp_row == 0:
            if sudoku_board[row - 1][column] == number or sudoku_board[row - 1][column + 1] == number or \
                    sudoku_board[row - 1][column - 1] == number or sudoku_board[row - 2][column] == number or \
                    sudoku_board[row - 2][column + 1] == number or sudoku_board[row - 2][column - 1] == number:
                return False
        if temp_row == 1:
            if sudoku_board[row + 1][column] == number or sudoku_board[row + 1][column + 1] == number or \
                    sudoku_board[row + 1][column - 1] == number or sudoku_board[row + 2][column] == number or \
                    sudoku_board[row + 2][column + 1] == number or sudoku_board[row + 2][column - 1] == number:
                return False
        if temp_row == 2:
            if sudoku_board[row + 1][column] == number or sudoku_board[row + 1][column + 1] == number or \
                    sudoku_board[row + 1][column - 1] == number or sudoku_board[row - 1][column] == number or \
                    sudoku_board[row - 1][column + 1] == number or sudoku_board[row - 1][column - 1] == number:
                return False
    # if temp_row == 0:
    #     if sudoku_board[row - 1][column] == number or sudoku_board[row - 2][column] == number:
    #         return False
    # if temp_row == 1:
    #     if sudoku_board[row + 1][column] == number or sudoku_board[row + 2][column] == number:
    #         return False
    # if temp_row == 2:
    #     if sudoku_board[row + 1][column] == number or sudoku_board[row - 1][column] == number:
    #         return False
    return True


def repeating_searches(sudoku_board):
    [row, column] = pick_empty_square(sudoku_board)
    if [row, column] == ['*', '*']:
        return True
    else:
        for i in range(1, 10):
            if check_if_valid(row, column, i, sudoku_board):
                sudoku_board[row][column] = i
                if repeating_searches(sudoku_board):
                    return True
                sudoku_board[row][column] = 0
        return False


def display_board(sudoku_board):
    for i in range(9):
        for j in range(9):
            print(sudoku_board[i][j], end=' ')
            if (j + 1) % 3 == 0:
                print(end=' ')
        print()
        if (i + 1) % 3 == 0:
            print()
    print('-------------------------')


def linear_search(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i
