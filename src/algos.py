import pygame
from collections import deque
from src.grid import Grid
from src.config.colors import Colors

def bfs(grid: Grid, color: tuple[int], r: int=0, c: int=0) -> bool:
    """BFS traveler.

    Args:
        grid: grid world
        color: color of traveler
        c: start r
        r: start c
    """
    clock = pygame.time.Clock()
    completed = False
    
    neighbors = deque()
    visited = []
    neighbors.append((r, c))
    visited.append((r, c))

    grid.values[r][c] = 0

    while neighbors:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True

        pygame.event.pump()
        clock.tick(80)

        r, c = neighbors.popleft()
        visited.append((r, c))

        rect = pygame.Rect(c * grid.cell_size, r * grid.cell_size, grid.cell_size, grid.cell_size)
        pygame.draw.rect(grid.screen, color, rect)
        pygame.display.update(rect)

        if grid.values[r][c] == 2:
            completed = True
            break

        directions = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
        for dx, dy in directions:
            if 0 <= dx < grid.num_rows and 0 <= dy < grid.num_cols:

                if grid.values[dx][dy] == 1:
                    grid.values[dx][dy] = -1
                    neighbors.append((dx, dy))

                elif grid.values[dx][dy] == 2:
                    neighbors.append((dx, dy))

    status = Colors.GREEN if completed else Colors.RED
    trace(grid, visited, status)
    return False


def dfs(grid: Grid, color: tuple[int], r: int=0, c: int=0) -> bool:
    """DFS traveler.

    Args:
        grid: grid world
        color: color of traveler
        r: start x
        c: start y
    """
    clock = pygame.time.Clock()
    completed = False
    visited = []

    if grid.values[r][c] == 0 or grid.values[r][c] == -1:
        return False

    stack = [(r, c)]

    if grid.values[r][c] == 1:
        grid.values[r][c] = -1

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True

        pygame.event.pump()
        clock.tick(80)

        curr_r, curr_c = stack.pop()
        cell = grid.values[curr_r][curr_c]

        rect = pygame.Rect(curr_c * grid.cell_size, curr_r * grid.cell_size, grid.cell_size, grid.cell_size)
        pygame.draw.rect(grid.screen, color, rect)
        pygame.display.update(rect)
        visited.append((curr_r, curr_c))

        if cell == 2:
            completed = True
            break
    
        directions = ((curr_r + 1, curr_c), (curr_r - 1, curr_c), (curr_r, curr_c + 1), (curr_r, curr_c - 1))
        for dx, dy in directions:
            if 0 <= dx < grid.num_rows and 0 <= dy < grid.num_cols:
                if grid.values[dx][dy] == 1:
                    grid.values[dx][dy] = -1
                    stack.append((dx, dy))
                elif grid.values[dx][dy] == 2:
                    stack.append((dx, dy))
    
    status = Colors.GREEN if completed else Colors.RED
    trace(grid, visited, status)
    return False


def trace(grid: Grid, visited: set, color: tuple[int]) -> None:
    """Tracer to highlight traveler.
    
    Args:
        grid: grid world. 
        color: color of travelor
    """
    clock = pygame.time.Clock()
    for r, c in visited:
        clock.tick(240)
        rect = pygame.Rect(c * grid.cell_size, r * grid.cell_size, grid.cell_size, grid.cell_size)
        pygame.draw.rect(grid.screen, color, rect)
        pygame.display.update(rect)