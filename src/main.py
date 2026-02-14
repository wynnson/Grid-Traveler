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

grid.set_background(Colors.BLACK)
grid.draw_lines(Colors.WHITE)
grid.generate_walls(Colors.WHITE, 50)
grid.generate_end(Colors.BLUE)

running = True
started = False

try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

        if not started:
            invalid = True
            while invalid:
                start_x = random.randint(0, grid.num_rows - 1)
                start_y = random.randint(0, grid.num_cols - 1)
                starting_position = grid.values[start_x][start_y]
                invalid = (starting_position == 1 or starting_position == 2)

            bfs(grid, x=start_x, y=start_y, color=Colors.YELLOW)
            started = True

except KeyboardInterrupt:
    print("Exited successfully")

finally:
    pygame.quit()