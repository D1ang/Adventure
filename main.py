import pygame
import sys
from pygame.locals import *
from settings import *
from level import Level


# Pygame setup
pygame.init()
pygame.display.set_caption("Adventure")
screen = pygame.display.set_mode((screen_width, screen_height))

# Video & display
fps = 60
fps_clock = pygame.time.Clock()

level = Level(level_map, screen)

"""
The game loop that runs
the actual game
"""
while True:

    for event in pygame.event.get():
        # Exit when the close window button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    fps_clock.tick(fps)
