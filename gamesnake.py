import pygame 
import random

# Khởi tạo màn hình
pygame.init()
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Game")

# Màu sắc
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Kích thước ô và bàn cờ
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Các khối hình
SHAPES = [
    [[1, 1, 1, 1]],  # Khối I
    [[1, 1], [1, 1]],  # Khối O
    [[1, 1, 0], [0, 1, 1]],  # Khối Z
    [[0, 1, 1], [1, 1, 0]],  # Khối S
    [[1, 1, 1], [0, 1, 0]],  # Khối T
    [[1, 1, 1], [0, 0, 1]],  # Khối L
    [[1, 1, 1], [1, 0, 0]]  # Khối J
]

# Màu sắc tương ứng với từng khối hình
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

# Hàm để vẽ khối hình và bàn cờ trên màn hình
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(WINDOW, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(WINDOW, BLACK, (0, y), (WIDTH, y))

def draw_shape(shape, x, y, color):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                pygame.draw.rect(WINDOW, color, (x + col * GRID_SIZE, y + row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_board(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]:
                pygame.draw.rect(WINDOW, SHAPE_COLORS[board[row][col]], (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Kiểm tra xem khối hình có vượt quá biên của bàn cờ hay không
def is_outside_board(shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if x + col < 0 or x + col >= GRID_WIDTH or y + row >= GRID_HEIGHT:
                    return True
    return False

# Kiểm tra xem khối hình có va chạm với các khối đã xếp trên bàn cờ hay không
def is_collision(shape, x, y, board):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if y + row >= GRID_HEIGHT or board[y + row][x + col] != 0:
                    return True
    return False

# Hàm chính của trò chơi
def main():
    clock = pygame.time.Clock()

    board = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_shape = random.choice(SHAPES)
    current_shape_color = random.choice(SHAPE_COLORS)
    shape_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
    shape_y = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not is_collision(current_shape, shape_x - 1, shape_y, board):
                        shape_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not is_collision(current_shape, shape_x + 1, shape_y, board):
                        shape_x += 1
                elif event.key == pygame.K_DOWN:
                    if not is_collision(current_shape, shape_x, shape_y + 1, board):
                        shape_y += 1

        if not is_collision(current_shape, shape_x, shape_y + 1, board):
            shape_y += 1
        else:
            for row in range(len(current_shape)):
                for col in range(len(current_shape[row])):
                    if current_shape[row][col]:
                        board[shape_y + row][shape_x + col] = SHAPE_COLORS.index(current_shape_color) + 1

            # Kiểm tra xem có dòng nào được xóa không
            for row in range(GRID_HEIGHT):
                if all(board[row]):
                    del board[row]
                    board.insert(0, [0] * GRID_WIDTH)

            current_shape = random.choice(SHAPES)
            current_shape_color = random.choice(SHAPE_COLORS)
            shape_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
            shape_y = 0

            if is_collision(current_shape, shape_x, shape_y, board):
                game_over = True

        # Vẽ trạng thái mới của trò chơi
        WINDOW.fill(BLACK)
        draw_grid()
        draw_board(board)
        draw_shape(current_shape, shape_x * GRID_SIZE, shape_y * GRID_SIZE, current_shape_color)
        pygame.display.update()

        clock.tick(5)

    pygame.quit()

if __name__ == '__main__':
    main()