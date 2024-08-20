import pygame
import sys
from sound_utils import create_tone

# Initialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Constants
WIDTH, HEIGHT = 500, 600
LINE_WIDTH = 2
BOARD_ROWS, BOARD_COLS = 4, 4
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 4
CROSS_WIDTH = 4
SPACE = SQUARE_SIZE // 4

# RGB Colors
BG_COLOR = (241, 250, 238)  # Soft mint cream
LINE_COLOR = (29, 53, 87)   # Dark blue
CIRCLE_COLOR = (230, 57, 70)  # Bright red
CROSS_COLOR = (69, 123, 157)  # Steel blue
TEXT_COLOR = (29, 53, 87)   # Dark blue
STATUS_BG_COLOR = (168, 218, 220)  # Light cyan

# Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe 4x4')
screen.fill(BG_COLOR)

# Board
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Fonts
font = pygame.font.Font(None, 40)

# Create sounds
place_sound = create_tone(440, 0.1)  # A4 note, 0.1 seconds
win_sound = create_tone(880, 0.5)    # A5 note, 0.5 seconds
draw_sound = create_tone(220, 0.5)   # A3 note, 0.5 seconds

def draw_lines():
    # Horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == ''

def is_board_full():
    return all(board[row][col] != '' for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

def check_win(player):
    # Check horizontal and vertical
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)) or all(board[j][i] == player for j in range(BOARD_ROWS)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_COLS-1-i] == player for i in range(BOARD_ROWS)):
        return True
    return False

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = ''
    return 'X', False

def draw_status(player, game_over, result):
    pygame.draw.rect(screen, STATUS_BG_COLOR, (0, WIDTH, WIDTH, HEIGHT - WIDTH))
    if not game_over:
        text = font.render(f"Player {player}'s turn", True, TEXT_COLOR)
    else:
        text = font.render(result, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, WIDTH + (HEIGHT - WIDTH) // 2))
    screen.blit(text, text_rect)

screen.fill(BG_COLOR)
draw_lines()

player = 'X'
game_over = False
result = ""

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            
            if clicked_row < BOARD_ROWS and clicked_col < BOARD_COLS and available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                place_sound.play()
                if check_win(player):
                    game_over = True
                    result = f"Player {player} wins!"
                    win_sound.play()
                elif is_board_full():
                    game_over = True
                    result = "It's a tie!"
                    draw_sound.play()
                else:
                    player = 'O' if player == 'X' else 'X'
                
                draw_figures()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r or (game_over and event.key == pygame.K_SPACE):
                player, game_over = restart()
                result = ""
    
    draw_status(player, game_over, result)
    pygame.display.update()

    if game_over:
        pygame.time.wait(2000)  # Wait for 2 seconds
        player, game_over = restart()
        result = ""

# Make sure to call pygame.quit() when the game exits
pygame.quit()