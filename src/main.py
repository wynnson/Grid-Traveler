import pygame
import random
from src.config.colors import Colors
from src.config.display import Display
from src.grid import Grid
from src.algos import bfs

pygame.init()
screen = pygame.display.set_mode((Display.SCREEN_WIDTH, Display.SCREEN_HEIGHT))
pygame.display.set_caption('Grid Traveler')

grid = Grid(
    screen=screen,
    height=Display.SCREEN_HEIGHT,
    width=Display.SCREEN_WIDTH,
    cell_size=Display.CELL_SIZE,
)

grid.reset()

running = True
has_run = False
run_again = False

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid.reset()
                    has_run = False

        pygame.display.update()

        if not has_run:
            invalid = True
            while invalid:
                start_x = random.randint(0, grid.num_rows - 1)
                start_y = random.randint(0, grid.num_cols - 1)
                starting_position = grid.values[start_x][start_y]
                invalid = (starting_position == 1 or starting_position == 2)

            run_again = bfs(grid, x=start_x, y=start_y, color=Colors.YELLOW)

            if run_again:
                grid.reset()
                has_run = False
            else:
                has_run = True

except KeyboardInterrupt:
    print("Exited successfully")

finally:
    pygame.quit()