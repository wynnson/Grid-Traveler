import pygame
from collections import deque
from src.grid import Grid
from src.config.colors import Colors

def bfs(grid: Grid, color: tuple[int], x: int=0, y: int=0) -> None:
    """BFS traveler.

    Args:
        grid: grid world
        color: color of traveler
        x: start x
        y: start y
    """
    clock = pygame.time.Clock()
    completed = False
    
    neighbors = deque()
    visited = []
    neighbors.append((x, y))
    visited.append((x, y))

    grid.values[x][y] = 0

    while neighbors:
        pygame.event.pump()
        clock.tick(30)

        r, c = neighbors.popleft()
        visited.append((r, c))

        rect = pygame.Rect(c * grid.cell_size, r * grid.cell_size, grid.cell_size, grid.cell_size)
        pygame.draw.rect(grid.screen, color, rect)
        pygame.display.update(rect)

        if grid.values[r][c] == 2:
            completed = True
            break

        directions = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
        for neighbor_row, neighbor_col in directions:
            if 0 <= neighbor_row < grid.num_rows and 0 <= neighbor_col < grid.num_cols:

                if grid.values[neighbor_row][neighbor_col] == 1:
                    grid.values[neighbor_row][neighbor_col] = 0
                    neighbors.append((neighbor_row, neighbor_col))

                elif grid.values[neighbor_row][neighbor_col] == 2:
                    neighbors.append((neighbor_row, neighbor_col))

    status = Colors.GREEN if completed else Colors.RED
    bfs_trace(grid, visited, status)
        
def bfs_trace(grid: Grid, visited: set, color: tuple[int]) -> None:
    """BFS tracer to highlight traveler.
    
    Args:
        grid: grid world. 
        color: color of travelor
    """
    clock = pygame.time.Clock()
    for r, c in visited:
        pygame.event.pump()
        clock.tick(160)
        rect = pygame.Rect(c * grid.cell_size, r * grid.cell_size, grid.cell_size, grid.cell_size)
        pygame.draw.rect(grid.screen, color, rect)
        pygame.display.update(rect)