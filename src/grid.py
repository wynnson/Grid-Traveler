import pygame 

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 40

WHITE = (255, 255, 255)
BLACK = (20, 20, 10)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Grid Traveler')

screen.fill(BLACK)

for x in range(0, SCREEN_WIDTH, GRID_SIZE):
    pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))

for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
    pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()