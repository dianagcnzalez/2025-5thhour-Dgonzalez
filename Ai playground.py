import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Playfield dimensions
COLS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE

# Colors (R, G, B)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Blue
    (255, 165, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 0, 0),    # Red
]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],                 # I
    [[1, 0, 0], [1, 1, 1]],        # J
    [[0, 0, 1], [1, 1, 1]],        # L
    [[1, 1], [1, 1]],               # O
    [[0, 1, 1], [1, 1, 0]],        # S
    [[0, 1, 0], [1, 1, 1]],        # T
    [[1, 1, 0], [0, 1, 1]],        # Z
]

class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = COLS // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(COLS)] for _ in range(ROWS)]

    for y in range(ROWS):
        for x in range(COLS):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]

    return grid

def valid_space(shape, grid, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + off_x
                new_y = y + off_y
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return False
                if new_y >= 0 and grid[new_y][new_x] != BLACK:
                    return False
    return True

def clear_rows(grid, locked):
    cleared = 0
    for y in range(ROWS-1, -1, -1):
        if BLACK not in grid[y]:
            cleared += 1
            for x in range(COLS):
                try:
                    del locked[(x, y)]
                except KeyError:
                    pass
            # Move every row above down one
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x_k, y_k = key
                if y_k < y:
                    locked[(x_k, y_k + 1)] = locked.pop(key)
    return cleared

def draw_grid(surface, grid):
    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(surface, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(surface, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_window(surface, grid, score=0):
    surface.fill(BLACK)
    draw_grid(surface, grid)

    # Draw score
    font = pygame.font.SysFont('Arial', 24)
    label = font.render(f'Score: {score}', 1, WHITE)
    surface.blit(label, (10, 10))

    pygame.display.update()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Simple Tetris')

    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5

    current_piece = Tetromino(random.choice(SHAPES), random.choice(COLORS))
    next_piece = Tetromino(random.choice(SHAPES), random.choice(COLORS))
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        # Rotate back if invalid
                        for _ in range(3):
                            current_piece.rotate()

        # Add piece to grid for drawing
        shape_pos = []
        for y, row in enumerate(current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    shape_pos.append((current_piece.x + x, current_piece.y + y))

        for pos in shape_pos:
            x, y = pos
            if y >= 0:
                grid[y][x] = current_piece.color

        # If piece hit the ground, lock it and spawn new
        if change_piece:
            for pos in shape_pos:
                locked_positions[pos] = current_piece.color
            current_piece = next_piece
            next_piece = Tetromino(random.choice(SHAPES), random.choice(COLORS))
            change_piece = False
            # Clear rows and update score
            cleared = clear_rows(grid, locked_positions)
            if cleared > 0:
                score += cleared * 10

        draw_window(screen, grid, score)

        # Check for game over
        for pos in locked_positions:
            if pos[1] < 1:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
