import pygame
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
grid.generate_walls(Colors.WHITE, 60)
grid.generate_end(Colors.BLUE)

running = True
started = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

    if not started:
        bfs(grid, Colors.YELLOW)
        started = True

pygame.quit()