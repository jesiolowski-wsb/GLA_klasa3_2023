import random


def initialize_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines = set()
    while len(mines) < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        mines.add((row, col))
        board[row][col] = 'X'
    return board


def count_adjacent_mines(board, row, col):
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'X':
                count += 1
    return count


def reveal(board, row, col, revealed):
    if (row, col) in revealed:
        return
    revealed.add((row, col))
    if board[row][col] == ' ':
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    reveal(board, i, j, revealed)


def print_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) in revealed:
                print(board[i][j], end=' ')
            else:
                print('-', end=' ')
        print()


def main():
    rows = 10
    cols = 10
    num_mines = 10
    board = initialize_board(rows, cols, num_mines)
    for i in range(rows):
        for j in range(cols):
            if board[i][j] != 'X':
                board[i][j] = str(count_adjacent_mines(board, i, j))
    revealed = set()
    game_over = False
    print_board(board, revealed)
    while not game_over:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        if (row, col) in revealed:
            print("Already revealed.")
            continue
        if board[row][col] == 'X':
            print_board(board, revealed | {(row, col)})
            print("Game Over! You hit a mine.")
            game_over = True
        else:
            reveal(board, row, col, revealed)
            print_board(board, revealed)
            if len(revealed) == rows * cols - num_mines:
                print("Congratulations! You've won!")
                game_over = True


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()