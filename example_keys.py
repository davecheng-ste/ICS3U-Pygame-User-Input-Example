"""
Description: Example of key event handling.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Examples")

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize rectangle parameters and starting position
rect_x, rect_y = 400, 300
rect_width, rect_height = 50, 50
rect_speed = 5

# Define main loop
clock = pygame.time.Clock()  # Initialize clock object to cap frame rate
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update rectangle position based on key inputs
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Clear screen
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLACK, (rect_x, rect_y, rect_width, rect_height))
    
    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
