"""
Author: D. Cheng
Date: 2024-05-23
Description: Pygame user input demonstration with fish animation. Press UP/DOWN arrows
             to adjust depth, SPACE to release bubbles, 0-9 to change speed, mouse-click 
             to drop anchors."
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Aquarium")

# Define constant colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load font and define instruction text display
font = pygame.font.Font(None, 18)  # None uses the default system font, 12 size
instructions_text = "Press UP/DOWN arrows to adjust depth, SPACE to release bubbles, 0-9 to change speed, mouse-click to drop anchors."
text_surface = font.render(instructions_text, True, WHITE)  # Render text onto a surface

# Define text position
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 10))  # Position text at the bottom center

# Load background image
ocean_background = pygame.image.load("images/water_background.png")
ocean_background = pygame.transform.scale(ocean_background, (WIDTH, HEIGHT))

# Load anchor image
anchor_sprite = pygame.image.load("images/anchor.png")

# Load fish.png image into fish_sprite, facing left (default)
fish_sprite = pygame.image.load("images/fish.png")
fish_sprite = pygame.transform.scale2x(fish_sprite)

# Create Rect object to manipulate fish_sprite
dory = fish_sprite.get_rect()

# Set initial position of dory (top right corner) using .x and .y attributes
dory.x = 400
dory.y = 300

# Define direction, -1 for left-moving, 1 for right-moving
direction = -1

# Define initial horizontal speed
speed = 5

# Define empty list for bubbles
bubble_list = []

# Define list for anchor positions
anchor_positions_list = []

# Define debounce time in ms and initialize last bubble time
debounce_time = 200
last_bubble_time = 0


# Define main game loop
running = True
clock = pygame.time.Clock()  # Create a Clock object for controlling frame rate

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left button click
                mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position, unpack tuple of coordinates (int)
                anchor_weight = random.randint(5, 20)  # Random anchor "weight" or sinking speed
                anchor_positions_list.append([mouse_x, mouse_y, anchor_weight])  # Add position to list

    # Handle key presses
    keys = pygame.key.get_pressed()
    
    # Handle fish speed increase/decrease
    if keys[pygame.K_0]:
        speed = 1
    if keys[pygame.K_1]:
        speed = 3
    elif keys[pygame.K_2]:
        speed = 5
    elif keys[pygame.K_3]:
        speed = 7
    elif keys[pygame.K_4]:
        speed = 9
    elif keys[pygame.K_5]:
        speed = 11
    elif keys[pygame.K_6]:
        speed = 13
    elif keys[pygame.K_7]:
        speed = 15
    elif keys[pygame.K_8]:
        speed = 17
    elif keys[pygame.K_9]:
        speed = 19

    # Handle fish depth change with up/down arrow keys
    if keys[pygame.K_DOWN]:
        dory.y = min(HEIGHT - dory.height, dory.y + 5)  # Increase depth, ensure within screen bounds
    elif keys[pygame.K_UP]:
        dory.y = max(0, dory.y - 5)  # Decrease depth, ensure within screen bounds
 
    # Handle fish bubble release with space, limiting rate with debounce_time calculation
    current_time = pygame.time.get_ticks()

    if keys[pygame.K_SPACE] and (current_time - last_bubble_time) >= debounce_time:
        if direction == 1:
            bubble_x, bubble_y = dory.midright
        else:
            bubble_x, bubble_y = dory.midleft
        bubble_diameter = random.randint(3, 10)
        bubble_list.append([bubble_x, bubble_y, bubble_diameter])
        last_bubble_time = current_time

    # Calculate change in position 
    dory.x += speed * direction  # Move sprite horizontally based on speed and direction

    # Manage screen edge contact
    if dory.left <= 0:
        direction = 1
        fish_sprite = pygame.transform.flip(fish_sprite, True, False)
    elif dory.right >= WIDTH:
        direction = -1
        fish_sprite = pygame.transform.flip(fish_sprite, True, False)

    # Draw background
    screen.blit(ocean_background, (0, 0))
    
    # Draw bubbles
    for bubble_item in bubble_list:
        bubble_x, bubble_y, bubble_diameter = bubble_item
        pygame.draw.circle(screen, WHITE, (bubble_x, bubble_y), bubble_diameter)
        bubble_item[1] -= 5  # Update bubble position
        if bubble_y <= 0:  # Remove bubbles from list at top of screen
            bubble_list.remove(bubble_item)
    
    # Draw anchors
    for anchor_item in anchor_positions_list:
        anchor_x, anchor_y, anchor_weight = anchor_item
        screen.blit(anchor_sprite, (anchor_x, anchor_y))
        anchor_item[1] += anchor_weight
        if anchor_y >= HEIGHT:
            anchor_positions_list.remove(anchor_item)

    # Draw fish
    screen.blit(fish_sprite, dory)

    # Draw text
    screen.blit(text_surface, text_rect)

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame   
pygame.quit()
sys.exit()
