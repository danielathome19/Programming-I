import pygame
from random import randrange

# Constants
WHITE  = (255, 255, 255)
YELLOW = (255, 255, 100)
BLACK  = (0, 0, 0)
RED    = (210, 50, 80)
GREEN  = (0, 255, 0)
BLUE   = (50, 150, 210)
DIS_WIDTH, DIS_HEIGHT = 600, 400
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Setup
pygame.init()
DISPLAY = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("Snake")
FONT = pygame.font.SysFont("sans-serif", 30)
CLOCK = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(DISPLAY, BLACK, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])

def random_food():
    return [randrange(0, DIS_WIDTH, SNAKE_BLOCK), 
            randrange(0, DIS_HEIGHT, SNAKE_BLOCK)]

def game_loop():
    x, y = DIS_WIDTH // 2, DIS_HEIGHT // 2
    dx, dy = 0, 0
    snake = []
    length = 1
    food = random_food()
    running = True
    game_over = False

    while running:
        DISPLAY.fill(BLUE)

        if game_over:
            msg = FONT.render("You lost! C=Play Again Q=Quit", True, RED)
            DISPLAY.blit(msg, (DIS_WIDTH // 6, DIS_HEIGHT // 3))
        else:
            if [x, y] in snake[:-1] or x < 0 or x >= DIS_WIDTH or y < 0 or y >= DIS_HEIGHT:
                game_over = True

            if [x, y] == food:
                food = random_food()
                length += 1

            snake.append([x, y])
            if len(snake) > length:
                del snake[0]

            pygame.draw.rect(DISPLAY, GREEN, [food[0], food[1], SNAKE_BLOCK, SNAKE_BLOCK])
            draw_snake(snake)
            score = FONT.render(f"Score: {length - 1}", True, YELLOW)
            DISPLAY.blit(score, (0, 0))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_c:
                        game_loop()
                    elif event.key == pygame.K_q:
                        running = False
                else:
                    if event.key == pygame.K_UP and dy == 0:
                        dx, dy = (0, -SNAKE_BLOCK)
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dx, dy = (0, SNAKE_BLOCK)
                    elif event.key == pygame.K_LEFT and dx == 0:
                        dx, dy = (-SNAKE_BLOCK, 0)
                    elif event.key == pygame.K_RIGHT and dx == 0:
                        dx, dy = (SNAKE_BLOCK, 0)

        if not game_over:
            x += dx
            y += dy

        CLOCK.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
