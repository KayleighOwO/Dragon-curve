import math
import pygame
from sys import exit

pygame.init()
width, height = 800, 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Get user choice
iteration = 20  #int(input('Enter iteration:'))  
length = 2     #int(input('Enter length of each segment:'))  

white = (255, 255, 255)

# Set up the line properties
line_x = width // 2
line_y = height // 2
line_angle = 0  # Initial angle (0 degrees)

left, right = "l", "r"

# Set the first iteration to right
old = right
new = old

# Keep track of the amount of cycles
cycle = 1

# Function to draw a line in the specified direction
def draw_line(direction):
    global line_x, line_y, line_angle
    if direction == "r":
        line_angle += 90
    elif direction == "l":
        line_angle -= 90
    
    x2 = line_x + length * math.cos(math.radians(line_angle))
    y2 = line_y - length * math.sin(math.radians(line_angle))
    pygame.draw.line(screen, white, (line_x, line_y), (x2, y2), 2)
    line_x = x2
    line_y = y2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Iterate until the desired amount is reached
        if cycle < iteration:
            # Add right to the iteration
            new = old + right
            # Flip the old iteration
            old = old[::-1]

            for char in range(0, len(old)):
                # Change character to it's opposite (left <=> right)
                if old[char] == right:
                    old = old[:char] + left + old[char + 1:]
                elif old[char] == left:
                    old = old[:char] + right + old[char + 1:]

            # Concatenate and print
            new = new + old
            #print(new)
            old = new
            cycle += 1

            # Draw lines
            for char in range(0, len(new)):
                if new[char] == "r":
                    draw_line("r")
                elif new[char] == "l":
                    draw_line("l")

        # Calculate FPS
        fps = clock.get_fps()
        pygame.display.set_caption(f"Dragon Curve - FPS: {fps:.2f}")

        pygame.display.update()
        clock.tick()