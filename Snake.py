import pygame
import sys
import random
import math
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1072, 603
CELL_SIZE = 32
FPS = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake initial state
snake = [(100, 100), (80, 100), (60, 100)]  # List of segments (x, y)
snake_dir = (CELL_SIZE, 0)  # Moving right initially
score = 0

# Food position
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):  # Prevent reverse
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake = [new_head] + snake[:-1]  # Add new head and remove tail

    # Check for collisions (with self or walls)
    if (new_head in snake[1:] or  # Self-collision
        new_head[0] < 0 or new_head[0] >= WIDTH or  # Wall collision (x-axis)
        new_head[1] < 0 or new_head[1] >= HEIGHT):  # Wall collision (y-axis)
        print("Game Over!")
        running = False

    # Check for food collision
    distance = math.sqrt( math.pow( new_head[0] - food[0], 2) + math.pow( new_head[1] - food[1], 2) )
    
    if distance < 27:
        snake.append(snake[-1])  # Add a segment to the tail
        food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        score += 1

    # Drawing everything
    screen.fill(BLACK)  # Clear the screen
    head = pygame.image.load(r"C:\Users\krish\OneDrive\ドキュメント\First Year\Wids Project\Sprites\png\snake_green_head_32.png")
    body = pygame.image.load(r"C:\Users\krish\OneDrive\ドキュメント\First Year\Wids Project\Sprites\png\snake_green_blob_32.png")
    apple = pygame.image.load(r"C:\Users\krish\OneDrive\ドキュメント\First Year\Wids Project\Sprites\png\apple_alt_32.png")
    score_text = font.render(f"Score : {score}", True, WHITE)
    screen.blit(head,snake[0])

    for i in range(1,len(snake)):
        screen.blit(body,snake[i])
    screen.blit(apple,food)
    screen.blit(score_text,(10,10))


    pygame.display.flip()  # Update the display
    clock.tick(FPS)  # Control the frame rate

pygame.quit()
sys.exit()
