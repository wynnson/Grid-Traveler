import pygame
import random
from src.config.colors import Colors
from src.config.display import Display
from src.grid import Grid
from src.algos import bfs, dfs

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

                if not has_run and (event.key in (pygame.K_d, pygame.K_b)):
                    invalid = True
                    while invalid:
                        start_r = random.randint(0, grid.num_rows - 1)
                        start_c = random.randint(0, grid.num_cols - 1)
                        starting_position = grid.values[start_r][start_c]
                        invalid = (starting_position == 0 or starting_position == 2)
                    
                    if event.key == pygame.K_d:
                        run_again = dfs(grid, color=Colors.YELLOW, r=start_r, c=start_c)
                    
                    if event.key == pygame.K_b:
                        run_again = bfs(grid, color=Colors.YELLOW, r=start_r, c=start_c)

                    if run_again:
                        grid.reset()
                        has_run = False
                    else:
                        has_run = True

            pygame.display.update()

except KeyboardInterrupt:
    print("Exited successfully")

finally:
    pygame.quit()