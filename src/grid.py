import pygame
import random

from src.config.colors import Colors
from src.config.status import Status


class Cell():
    """Grid cells class."""
    def __init__(
        self, 
        status: Status, 
        weight: int=1
    ):
        """
        Args:
            status: cell status
            weight: weight of the cell (default unweighted)
        """
        self.status = status
        self.weight = weight


class Grid():
    """Grid for traveling."""
    def __init__(
        self, 
        screen,
        height: int, 
        width: int, 
        cell_size: int,
    ):
        """        
        Args:
            screen: pygame GUI
            height: height of GUI
            width: width of GUI
            cell_size: size of cells
            walls: coords containing dead ends
        """
        self.screen = screen
        self.height = height
        self.width = width
        self.cell_size = cell_size
        self.font = pygame.font.SysFont(None, size=(self.cell_size // 2))

        self.num_rows = self.height // self.cell_size
        self.num_cols = self.width // self.cell_size
        self.values = None          # grid of cell objects
        self.weighted = False       # weighted flag

    def draw_lines(self, color: tuple[int]) -> None:
        """Draws grid lines.

        Args:
            color: (r, g, b)
        """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, color, (x, 0), (x, self.height))

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, color, (0, y), (self.width, y))

    def draw_weight(self, r: int, c: int, color=(255, 255, 255)) -> None:
        """Draws the weight text on the cell.

        Args:
            r: row
            c: col
            color: rgb color
        """
        if not self.weighted:
            return

        cell = self.values[r][c]
        if cell.status in (Status.W, Status.E):
            return
        
        text = self.font.render(str(cell.weight), True, color)
        x = c * self.cell_size + (self.cell_size - text.get_width()) // 2
        y = r * self.cell_size + (self.cell_size - text.get_height()) // 2
        self.screen.blit(text, (x, y))

    def set_background(self, color: tuple[int]) -> None:
        """Sets GUI background. Make sure to set before draw.
        
        Args:
            color: (r, g, b)
        """
        self.screen.fill(color)

    def generate_walls(self, color: tuple[int], walls: int=20) -> None:
        """Blocks off random grids.
        
        Args:
            walls: number of walls
            color: color of wall
        """
        for _ in range(walls):
            r = random.randint(0, self.num_rows - 1)
            c = random.randint(0, self.num_cols - 1)
            rect = pygame.Rect(c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, color, rect)
            
            current_cell = self.values[r][c]
            if current_cell.status != Status.E:
                current_cell.status = Status.W

    def generate_grid(self, weighted: bool=False) -> None:
        """Generates a weighted or unweighted grid (weight of 1).
        
        Args:
            weighted: weighted grid flag
        """
        vals = []
        for _ in range(self.num_rows):
            row = []
            for _ in range(self.num_cols):
                if weighted:
                    rand = random.randint(1, 10)
                    row.append(Cell(Status.U, rand))
                else:
                    row.append(Cell(Status.U))

            vals.append(row)

        self.values = vals

    def generate_end(self, color: tuple[int]):
        """Generates a target value / cell.
        
        Args:
            color: color of target
        """
        r = random.randint(0, self.num_rows - 1)
        c = random.randint(0, self.num_cols - 1)
        rect = pygame.Rect(c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, color, rect)

        current_cell = self.values[r][c]
        current_cell.status = Status.E

    def reset(self, weighted: bool=False):
        """Resets grid to preset defaults.
        
        Args:
            weighted: weighted grid flag.
        """
        wall_count = int((self.height + self.width) * 2 / 8)
        self.weighted=weighted
        self.generate_grid(weighted)
        self.set_background(Colors.BLACK)
        self.draw_lines(Colors.WHITE)
        self.generate_walls(Colors.WHITE, wall_count)
        self.generate_end(Colors.BLUE)

        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.draw_weight(r, c)