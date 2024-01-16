import pygame
import sys
import os
import threading
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Pad")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Define button properties
button_width = width // 4
button_height = height // 4

# Define the folder for sound files
sound_folder = os.path.join(os.path.dirname(__file__), "musicdata")

# Get a list of sound files in the folder
sound_files = [os.path.join(sound_folder, file) for file in os.listdir(sound_folder) if file.endswith(".wav")]
sounds = [pygame.mixer.Sound(file) for file in sound_files]

# Create buttons
buttons = []
for row in range(4):
    for col in range(4):
        rect = pygame.Rect(col * button_width, row * button_height, button_width, button_height)
        buttons.append(rect)

# Function to change button color and revert after a delay
def change_button_color(button, color):
    pygame.draw.rect(screen, color, button, 0)
    pygame.display.flip()
    time.sleep(2)
    pygame.draw.rect(screen, black, button, 2)
    pygame.display.flip()

# Main game loop
while True:
    # Draw buttons
    screen.fill(white)
    for button in buttons:
        pygame.draw.rect(screen, black, button, 2)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = event.pos
                for i, button in enumerate(buttons):
                    if button.collidepoint(mouse_x, mouse_y):
                        # Play sound
                        sounds[i].play()

                        # Use threading to change button color without blocking the main loop
                        threading.Thread(target=change_button_color, args=(button, red)).start()

    

    # Update the display
    pygame.display.flip()
