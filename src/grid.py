import pygame
import random

class Grid():
    """Grid for traveling."""
    def __init__(
        self, 
        screen,
        height: int, 
        width: int, 
        cell_size: int
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
        self.num_rows = self.height // self.cell_size
        self.num_cols = self.width // self.cell_size
        self.values = [
            [1] * (self.num_cols) 
            for i in range(self.num_rows)
        ]

    def draw_lines(self, color: tuple[int]) -> None:
        """Draws grid lines.

        Args:
            color: (r, g, b)
        """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, color, (x, 0), (x, self.height))

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, color, (0, y), (self.width, y))

    def set_background(self, color: tuple[int]) -> None:
        """Sets GUI background. Make sure to set before draw.
        
        Args:
            color: (r, g, b)
        """
        self.screen.fill(color)

    def generate_walls(self, color: tuple[int], amt: int =20) -> None:
        """Blocks off random grids.
        
        Args:
            amt: number of walls
            color: color of wall
        """
        for _ in range(amt):
            r = random.randint(0, self.num_rows - 1)
            c = random.randint(0, self.num_cols - 1)
            rect = pygame.Rect(c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size)
            pygame.draw.rect(self.screen, color, rect)
            if self.values[r][c] != 2:
                self.values[r][c] = 0

    def generate_end(self, color: tuple[int]):
        """Generates a target value / cell.
        
        Args:
            color: color of target
        """
        r = random.randint(0, self.num_rows - 1)
        c = random.randint(0, self.num_cols - 1)
        rect = pygame.Rect(c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, color, rect)
        self.values[r][c] = 2