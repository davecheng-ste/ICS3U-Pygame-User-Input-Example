# Pygame Animations
## Learning Objectives
In this task, you will learn about handling user input in Pygame.

### Review: Pygame Structure
Recall the basic structure of a Pygame program:

```python
import pygame
import sys

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()  # Create a Clock object for controlling frame rate

# Define main loop
running = True

# All events, updates, and graphics happen in this `while` loop below
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw graphics
    screen.fill(WHITE) 

    # Update display
    pygame.display.flip()
    clock.tick(30)  # Frame rate limit

# Quit Pygame   
pygame.quit()
sys.exit()
```

Note the all-important `while` loop. This loop refreshes many times per second. With every loop, a typical Pygame program does the following structure:

- HANDLE EVENTS. Pygame constantly monitors for "events" such as keypresses, mouse movement, and quitting. So far, our programs have only looked for the `pygame.QUIT` event, which is triggered when the user closes the Pygame graphics window.
- UPDATE STATES. Next, the program should update the state of objects as necessary (e.g. sprite positions, counters, etc.) Some states may be dependent on conditions (e.g. if sprite has reached the screen edge, change direction). It is good practice to organize all of your updates in one section.
- DRAW GRAPHICS. Finally, based on the events and updated states above, the program should draw the graphics.


## Handling Mouse Events
To detect mouse events, we'll add code to the event loop after the `pygame.QUIT` type. For example, this code checks for a mouse button press using the event type `pygame.MOUSEBUTTONDOWN`:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("Mouse button pressed")
```

### Mouse Position
In Pygame, you can get the current mouse position using `pygame.mouse.get_pos()`, which returns the `(x, y)` coordinates.

```python
mouse_x, mouse_y = pygame.mouse.get_pos()
print(f"Mouse position: ({mouse_x}, {mouse_y})")
```

### Mouse Button States
To check the state of the mouse buttons, use `pygame.mouse.get_pressed()`. This function returns a tuple of three **boolean values** corresponding to the left, middle, and right buttons.

```python
left_button, middle_button, right_button = pygame.mouse.get_pressed()
```

### Mouse Events
Pygame provides various mouse events:

- `MOUSEBUTTONDOWN`: Triggered when a mouse button is pressed.
- `MOUSEBUTTONUP`: Triggered when a mouse button is released.
- `MOUSEMOTION`: Triggered when the mouse is moved.

Example:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("Mouse button pressed")
    elif event.type == pygame.MOUSEBUTTONUP:
        print("Mouse button released")
    elif event.type == pygame.MOUSEMOTION:
        print("Mouse moved")
```

### Mouse Examples
Putting it all together, let's have a look at a simple example in the [example_mouse.py](example_mouse.py) in this repo:


```python
"""
Description: Example of mouse event handling.
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

# Initialize variables to track moues states
mouse_x, mouse_y = 0, 0
button_left, button_middle, button_right = False, False, False

# Define main loop
running = True
clock = pygame.time.Clock()  # Initialize clock object to cap frame rate

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position, unpack tuple of coordinates (int)
            mouse_x, mouse_y = pygame.mouse.get_pos()  
            # Get mouse button states, unpack tuple of button states (bool)
            button_left, button_middle, button_right = pygame.mouse.get_pressed()    

    # Draw graphics and output
    screen.fill(WHITE)

    if button_left:
        print(f"Left button pressed at position ({mouse_x}, {mouse_y})", end="\r")
    if button_right:
        print(f"Right button pressed at position ({mouse_x}, {mouse_y})", end="\r")

    # Update display
    pygame.display.flip()
    clock.tick(30)  # Limit frame rate to 30 fps

# Quit Pygame   
pygame.quit()
sys.exit()
```

Note the adherence in the program to the loop structure of *input* (handling events), *processing* (updating states), and *output* (draw graphics or print statements).

<br><br>

## Handling Keyboard Input
There are many ways to handle keyboard input. The most basic is to detect single keypressed with keyboard events:

- `KEYDOWN`: Triggered when a key is pressed.
- `KEYUP`: Triggered when a key is released.

Example:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        print(f"Key pressed")
    elif event.type == pygame.KEYUP:
        print(f"Key released")
```

### Detecting Individual Keys
To detect specific keys, compare `event.key` with constants defined in [this list](https://www.pygame.org/docs/ref/key.html#module-pygame.key) (e.g., `pygame.K_SPACE`, `pygame.K_DOWN`, `pygame.K_A`, etc.)

Example:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_A:
            print("Key 'A' pressed")
        elif event.key == pygame.K_SPACE:
            print("Spacebar pressed")
```

### Detecting Individual Keys - Alternate Method
It is also possible to detect the state of *all keys* in each iteration of the main loop by invoking `pygame.key.get_pressed()`. This function returns a sequence of boolean values representing the state of every key pressed or not pressed. 

You can then check the state of specific keys by *indexing* into this sequence with the key constants.

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    print("Spacebar is pressed")
```

Note the index used for the sequence `keys[]` are not integers, as one would expect of lists and tuples. Here, we use the named [key constants](https://www.pygame.org/docs/ref/key.html#module-pygame.key) as the sequence indices.

### Detecting Multiple Keys - Alternate Method
We can then use the above `pygame.key.get_pressed()` method to handle multiple keys.

For example, the program [example_keys.py](example_keys.py) handles multiple keys to move a rectangle on the screen:

```python
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
```

<br><br>

## Task Description

Create a program that draws graphics for a scene or design. The graphics should change based on various user inputs. 

For example, you could create a garden drawing program in which:

- left-clicking creates flowers of random sizes and colors, 
- right-clicking spawns animated butterflies, and
- keyboard arrows up and down change the brightness of the sky, 
- keyboard numbers 1 through 9 change the speed of a lawnmower moving across the screen.

You can re-use methods from previous tasks defined to draw items to the screen (i.e flowers, clouds, etc). You can also incorporate sprites and background downloaded from [Open Game Art](https://opengameart.org/).

The objective is to demonstrate your ability to handle as many of the different input events as possible:

- mouse position
- mouse button clicks and releases
- key presses

## Assessment
### Level 1
Code features one (1) type of visual or behavioural change based on mouse and key events.

### Level 2
Code features two (2) unique types of visual or behavioural change based on mouse and key events. 

### Level 3
Code features three (3) unique types of visual or behavioural change based on mouse and key events. 

### Level 4
Code features four (4) or more unique types of visual or behavioural change based on mouse and key events. 

<br><br>

## Template File
The template file `main.py` has already been set up for you with a 800 by 600 screen. You can modify this as necessary.


<br><br>
## Submission
- Commit changes as you make incremental progress. Make sure to write meaningful commit messages.
- Sync or push your changes at the end of every work session or class.
- Finally, take a screenshot or video capture of your finished output window showing your design(s). Upload the screenshot or video to Classroom.
