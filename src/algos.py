import pygame
import heapq
import math

from src.config.status import HeuristicCases, Status
from src.grid import Grid
from src.config.colors import Colors


def A_Star(
    grid: Grid, 
    color: tuple[int], 
    r: int = 0, 
    c: int = 0, 
    h: HeuristicCases = None
) -> bool:
    """A* traveler (Dijkstra's + Heuristic / UCS)

    Args:
        grid: grid world
        color: color of traveler
        c: start r
        r: start c
    """

    def heuristic(x1, y1) -> int:
        """Different heuritics to end goal.

        Args:
            x1: row
            y1: col

        Returns:
            int: heuristic scores
        """
        x2 = grid.goal_r
        y2 = grid.goal_c

        if h is None or x2 is None or y2 is None:
            return 0    # Dummy heuristic

        a = abs(x2 - x1)
        b = abs(y2 - y1)
        match h:
            case HeuristicCases.M: return a + b                          # L1
            case HeuristicCases.E: return math.sqrt(a * a + b * b)       # L2
            case _: return 0

    clock = pygame.time.Clock()
    completed = False

    neighbors = []  # pq
    visited = []  # visited path for trace

    starting_cell = grid.values[r][c]
    starting_cell.status = Status.F

    heapq.heappush(neighbors, (starting_cell.weight, r, c))
    visited.append((r, c))

    while neighbors:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True

        pygame.event.pump()
        clock.tick(120)

        _, r, c = heapq.heappop(neighbors)
        current_cell = grid.values[r][c]
        visited.append((r, c))

        if current_cell.status == Status.V:
            continue

        if current_cell.status == Status.E:
            completed = True
            break

        current_cell.status = Status.V
        color_cell(r, c, grid, color)

        directions = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
        for dx, dy in directions:
            if 0 <= dx < grid.num_rows and 0 <= dy < grid.num_cols:
                neighbor_cell = grid.values[dx][dy]
                cost = neighbor_cell.weight + heuristic(dx, dy)

                if neighbor_cell.status == Status.U:
                    neighbor_cell.status = Status.F
                    color_cell(dx, dy, grid, Colors.ORANGE)
                    heapq.heappush(neighbors, (cost, dx, dy))

                elif neighbor_cell.status == Status.E:
                    color_cell(dx, dy, grid, Colors.ORANGE)
                    heapq.heappush(neighbors, (cost, dx, dy))

    status_color = Colors.GREEN if completed else Colors.RED
    trace(grid, visited, status_color)
    return False

def bfs(grid: Grid, color: tuple[int], r: int = 0, c: int = 0) -> bool:
    """BFS (Dijsktra's / UCS) traveler.

    Args:
        grid: grid world
        color: color of traveler
        c: start r
        r: start c
    """
    clock = pygame.time.Clock()
    completed = False
    neighbors = []              # pq
    visited = []                # visited path for trace

    starting_cell = grid.values[r][c]
    starting_cell.status = Status.V

    heapq.heappush(neighbors, (starting_cell.weight, r, c))
    visited.append((r, c))

    while neighbors:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True

        pygame.event.pump()
        clock.tick(120)

        _, r, c = heapq.heappop(neighbors)
        color_cell(r, c, grid, color)
        visited.append((r, c))

        current_cell = grid.values[r][c]
        if current_cell.status == Status.E:
            completed = True
            break

        directions = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
        for dx, dy in directions:
            if 0 <= dx < grid.num_rows and 0 <= dy < grid.num_cols:
                neighbor_cell = grid.values[dx][dy]

                if neighbor_cell.status == Status.U:
                    neighbor_cell.status = Status.V
                    heapq.heappush(neighbors, (neighbor_cell.weight, dx, dy))

                elif neighbor_cell.status == Status.E:
                    heapq.heappush(neighbors, (neighbor_cell.weight, dx, dy))

    status_color = Colors.GREEN if completed else Colors.RED
    trace(grid, visited, status_color)
    return False


def dfs(grid: Grid, color: tuple[int], r: int = 0, c: int = 0) -> bool:
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

    starting_cell = grid.values[r][c]

    if starting_cell.status == Status.W or starting_cell.status == Status.V:
        return False

    stack = [(r, c)]

    if starting_cell.status == Status.U:
        starting_cell.status = Status.V

    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return True

        pygame.event.pump()
        clock.tick(120)

        r, c = stack.pop()
        color_cell(r, c, grid, color)
        visited.append((r, c))

        current_cell = grid.values[r][c]
        if current_cell.status == Status.E:
            completed = True
            break

        directions = ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
        for dx, dy in directions:
            if 0 <= dx < grid.num_rows and 0 <= dy < grid.num_cols:
                neighbor_cell = grid.values[dx][dy]

                if neighbor_cell.status == Status.U:
                    neighbor_cell.status = Status.V
                    stack.append((dx, dy))

                elif neighbor_cell.status == Status.E:
                    stack.append((dx, dy))

    status_color = Colors.GREEN if completed else Colors.RED
    trace(grid, visited, status_color)
    return False


def trace(grid: Grid, visited: set, color: tuple[int]) -> None:
    """Tracer to highlight traveler.

    Args:
        grid: grid world.
        color: color of travelor
    """
    clock = pygame.time.Clock()

    def highlight():
        for r, c in visited:
            clock.tick(360)
            color_cell(r, c, grid, color)

    highlight()


def color_cell(r, c, grid, color):
    """Helper to color a grid cell.

    Args:
        r: row
        c: col
        grid: grid object
        color: cell color
    """
    rect = pygame.Rect(c * grid.cell_size, r * grid.cell_size, grid.cell_size, grid.cell_size)
    pygame.draw.rect(grid.screen, color, rect)
    grid.draw_weight(r, c)
    pygame.display.update(rect)