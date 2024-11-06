import random


def initialize_board(size, mines):
    board = [[0 for _ in range(size)] for _ in range(size)]
    mine_positions = random.sample(range(size * size), mines)

    for pos in mine_positions:
        row, col = divmod(pos, size)
        board[row][col] = -1  # Place mine

        for r in range(max(0, row - 1), min(size, row + 2)):
            for c in range(max(0, col - 1), min(size, col + 2)):
                if board[r][c] != -1:
                    board[r][c] += 1  # Increment the number of adjacent mines

    return board


def reveal_cell(board, revealed, row, col):
    if board[row][col] == -1:
        return False  # Hit a mine
    if revealed[row][col]:
        return True  # Already revealed

    revealed[row][col] = True
    if board[row][col] == 0:
        for r in range(max(0, row - 1), min(len(board), row + 2)):
            for c in range(max(0, col - 1), min(len(board), col + 2)):
                if not revealed[r][c]:
                    reveal_cell(board, revealed, r, c)  # Recursive reveal

    return True


def display_board(board, revealed):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if revealed[r][c]:
                if board[r][c] == -1:
                    print('*', end=' ')
                else:
                    print(board[r][c], end=' ')
            else:
                print('.', end=' ')
        print()


# Example usage
size = 5
mines = 5
board = initialize_board(size, mines)
revealed = [[False for _ in range(size)] for _ in range(size)]

while True:
    display_board(board, revealed)
    row, col = map(int, input("Enter row and column to reveal (0-indexed): ").split())

    if not reveal_cell(board, revealed, row, col):
        print("Game Over! You hit a mine.")
        break

    if all(revealed[r][c] or board[r][c] == -1 for r in range(size) for c in range(size)):
        print("Congratulations! You've revealed all safe cells.")
        break
