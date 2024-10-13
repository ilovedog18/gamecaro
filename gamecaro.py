import pygame

# Khởi tạo màn hình
pygame.init()
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Cờ Caro")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Kích thước ô và bàn cờ
SQUARE_SIZE = 200
BOARD_SIZE = 3

# Khởi tạo bàn cờ
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Hàm để vẽ bàn cờ trên màn hình
def draw_board():
    WIN.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            pygame.draw.rect(WIN, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
            if board[row][col] == 'X':
                pygame.draw.line(WIN, RED, (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + 50),
                                 (col * SQUARE_SIZE + 150, row * SQUARE_SIZE + 150), 3)
                pygame.draw.line(WIN, RED, (col * SQUARE_SIZE + 150, row * SQUARE_SIZE + 50),
                                 (col * SQUARE_SIZE + 50, row * SQUARE_SIZE + 150), 3)
            elif board[row][col] == 'O':
                pygame.draw.circle(WIN, BLUE, (col * SQUARE_SIZE + 100, row * SQUARE_SIZE + 100), 50)
    pygame.display.update()

# Hàm để kiểm tra người chiến thắng
def check_winner():
    # Kiểm tra các hàng
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    # Kiểm tra các cột
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Kiểm tra đường chéo chính
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    # Kiểm tra đường chéo phụ
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Hàm để thực hiện lượt đi của người chơi
def player_move(row, col):
    if board[row][col] == ' ':
        board[row][col] = 'X'
        return True
    return False

# Hàm để thực hiện lượt đi của máy
def computer_move():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                return

# Hàm để kiểm tra xem bàn cờ đã đầy chưa
def is_board_full():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == ' ':
                return False
    return True

# Hàm chính của trò chơi
def main():
    clock = pygame.time.Clock()
    turn = 'X'
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and turn == 'X':
                mouse_pos = pygame.mouse.get_pos()
                clicked_row = mouse_pos[1] // SQUARE_SIZE
                clicked_col = mouse_pos[0] // SQUARE_SIZE
                if player_move(clicked_row, clicked_col):
                    if check_winner() == 'X':
                        print("Người chơi X thắng!")
                        game_over = True
                    elif is_board_full():
                        print("Hòa!")
                        game_over = True
                    else:
                        turn = 'O'
                        draw_board()

                        computer_move()
                        if check_winner() == 'O':
                            print("Người chơi O thắng!")
                            game_over = True
                        elif is_board_full():
                            print("Hòa!")
                            game_over = True
                        else:
                            turn = 'X'
                        draw_board()
        draw_board()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()