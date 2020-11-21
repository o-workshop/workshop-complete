import sys, pygame
WIDTH = HEIGHT = 600

grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def draw_lines():
    # horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def draw_players():
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 1:
                pygame.draw.circle(screen, BLACK, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                # since 200 is the length, we're drawing it in the center
            elif grid[row][col] == 2:
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )


def fill_square(row, col, player):
    grid[row][col] = player


def is_square_available(row, col):
    if grid[row][col] == 0:
        return True
    else:
        return False


def is_grid_full():
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:
                return False

    return True


def draw_vertical_winning_line(col):
    posX = col * 200 + 100
    color = BLACK

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row):
    posY = row * 200 + 100
    pygame.draw.line(screen, BLACK, (15, posY), (WIDTH - 15, posY), 15)


def draw_diagonal_down():
    pygame.draw.line(screen, BLACK, (15, 15), (WIDTH - 15, HEIGHT- 15), 15)


def draw_diagonal_up():
    pygame.draw.line(screen, BLACK, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def is_winner(player):
    # vertical
    for col in range(3):
        if grid[0][col] == player and grid[1][col] == player and grid[2][col] == player:
            draw_vertical_winning_line(col)
            return True  # return function, end loop

    # horizontal
    for row in range(3):
        if grid[row][0] == player and grid[row][1] == player and grid[row][2] == player:
            draw_horizontal_winning_line(row)
            return True  # return function, end loop

    # diagonal down
    if grid[0][0] == player and grid[1][1] == player and grid[2][2]:
        draw_diagonal_down()
        return True

    # diagonal up
    if grid[2][0] == player and grid[1][1] == player and grid[0][2] == player:
        draw_diagonal_up()
        return True

    return False


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(3):
        for col in range(3):
            grid[row][col] = 0


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR = WHITE
LINE_COLOR = BLACK
LINE_WIDTH = 2

# FOR NEXT PART
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

screen.fill(BG_COLOR)

player = 1
game_over = False

# where we draw, color, starting position, ending position, width
# pygame.draw.line(screen, WHITE, (10, 10), (300, 300), 10)
# 200 is width of screen / 3 (cause of grid)

SQUARE_SIZE = 200
CROSS_WIDTH = 25
SPACE = 44

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            player = 1
            game_over = False
            restart()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)  # 200 is length of the squares
            clicked_col = int(mouseX // 200)  # is dividing and rounding

            if is_square_available(clicked_row, clicked_col):
                fill_square(clicked_row, clicked_col, player)
                game_over = is_winner(player)
                if player == 1:
                    player = 2
                else:
                    player = 1

                draw_players()

    pygame.display.update()
    clock.tick(60)
