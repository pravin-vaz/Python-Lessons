# Example loads up pygame library and basic shapes in pygame with standard settings.

import pygame
import math # Import math for the arc example

# Initialize Pygame and set up the display
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Shapes Examples")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # 1. Draw a filled rectangle (width=0 by default)
    pygame.draw.rect(screen, RED, [100, 100, 200, 100])

    # 2. Draw a filled circle
    pygame.draw.circle(screen, GREEN, (400, 150), 75)

    # 3. Draw a line (with a thickness of 5 pixels)
    pygame.draw.line(screen, BLUE, (50, 400), (550, 400), 5)

    # 4. Draw a filled polygon (a triangle)
    pygame.draw.polygon(screen, BLACK, [[500, 300], [450, 400], [550, 400]])

    # 5. Draw a hollow ellipse (with a thickness of 4 pixels)
    pygame.draw.ellipse(screen, BLACK, [20, 220, 100, 50], 4)

    # Update the display to show the new shapes
    pygame.display.flip()

# Quit Pygame
pygame.quit()
