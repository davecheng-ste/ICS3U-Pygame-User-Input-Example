"""
Author: D. Cheng
Date: 2024-05-23
Description: Pygame user input demonstration with fish animation. Press UP/DOWN arrows
             to adjust depth, SPACE to release bubbles, 0-9 to change speed, mouse-click 
             to drop anchors.
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

# Define constant colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load font and define instruction text display
font = pygame.font.Font(None, 18)
instructions_text = "Press UP/DOWN arrows to adjust depth, SPACE to release bubbles, 0-9 to change speed, mouse-click to drop anchors."
text_surface = font.render(instructions_text, True, WHITE)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 10))

# Load images with error handling
def load_image(file_path):
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Error loading image: {file_path} - {e}")
        sys.exit(1)

ocean_background = load_image("images/water_background.png")
ocean_background = pygame.transform.scale(ocean_background, (WIDTH, HEIGHT))
anchor_sprite = load_image("images/anchor.png")
fish_sprite = load_image("images/fish.png")
fish_sprite = pygame.transform.scale2x(fish_sprite)

# Create Rect object to manipulate fish_sprite
dory = fish_sprite.get_rect()
dory.x = 400
dory.y = 300

# Define direction, speed, and lists
direction = -1
speed = 5
bubble_list = []
anchor_positions_list = []
debounce_time = 200
last_bubble_time = 0

# Mapping keys to speeds
speed_keys = {
    pygame.K_0: 1, pygame.K_1: 3, pygame.K_2: 5, pygame.K_3: 7, pygame.K_4: 9,
    pygame.K_5: 11, pygame.K_6: 13, pygame.K_7: 15, pygame.K_8: 17, pygame.K_9: 19
}

# Define functions
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            handle_mouse_click()
    return True

def handle_mouse_click():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    anchor_weight = random.randint(5, 20)
    anchor_positions_list.append([mouse_x, mouse_y, anchor_weight])

def update_bubbles():
    for bubble_item in bubble_list:
        bubble_item[1] -= 5
        if bubble_item[1] <= 0:
            bubble_list.remove(bubble_item)

def update_anchors():
    for anchor_item in anchor_positions_list:
        anchor_item[1] += anchor_item[2]
        if anchor_item[1] >= HEIGHT:
            anchor_positions_list.remove(anchor_item)

def draw_elements():
    screen.blit(ocean_background, (0, 0))
    for bubble_item in bubble_list:
        pygame.draw.circle(screen, WHITE, (bubble_item[0], bubble_item[1]), bubble_item[2])
    for anchor_item in anchor_positions_list:
        screen.blit(anchor_sprite, (anchor_item[0], anchor_item[1]))
    screen.blit(fish_sprite, dory)
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def adjust_fish_speed(keys):
    global speed
    for key, value in speed_keys.items():
        if keys[key]:
            speed = value

def move_fish(keys):
    global direction, fish_sprite
    dory.x += speed * direction
    if keys[pygame.K_DOWN]:
        dory.y = min(HEIGHT - dory.height, dory.y + 5)
    elif keys[pygame.K_UP]:
        dory.y = max(0, dory.y - 5)
    if dory.left <= 0:
        direction = 1
        fish_sprite = pygame.transform.flip(fish_sprite, True, False)
    elif dory.right >= WIDTH:
        direction = -1
        fish_sprite = pygame.transform.flip(fish_sprite, True, False)

def release_bubble(keys):
    global last_bubble_time
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and (current_time - last_bubble_time) >= debounce_time:
        bubble_x, bubble_y = dory.midright if direction == 1 else dory.midleft
        bubble_diameter = random.randint(3, 10)
        bubble_list.append([bubble_x, bubble_y, bubble_diameter])
        last_bubble_time = current_time

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    running = handle_events()
    keys = pygame.key.get_pressed()
    adjust_fish_speed(keys)
    move_fish(keys)
    release_bubble(keys)
    update_bubbles()
    update_anchors()
    draw_elements()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
