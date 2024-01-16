import os
import pygame
import random
import sys

# Function to play audio
def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Function to check guesses
def check_guess(guess, answer):
    return guess.lower() == answer.lower()

# Pygame initialization
pygame.init()

# Define screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
RECT_WIDTH = 600
RECT_HEIGHT = 80
SPACE_BETWEEN = 20
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Guess the Song")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.Font(None, 20)

# Define a list of songs with associated information
songs = [
    {"title": "Song1", "year": 2000, "chart_position": 1, "genre": "Pop", "intro_file": "song1_intro.wav", "full_song_file": "song1_full.wav"},
    {"title": "Song2", "year": 1995, "chart_position": 3, "genre": "Rock", "intro_file": "song2_intro.wav", "full_song_file": "song2_full.wav"},
    # Add more songs...
]

# Select a random song
selected_song = random.choice(songs)
text_input = ''
correct_answer = "answer1"

rect = pygame.Rect((SCREEN_WIDTH - RECT_WIDTH) // 2, 20, RECT_WIDTH, RECT_HEIGHT)

# Congratulations message
congratulations_text = font.render("Congratulations!", True, BLACK)
congratulations_rect = congratulations_text.get_rect(center=(RECT_WIDTH // 2, RECT_HEIGHT // 2 + 50))

playing = False

# Game loop
attempts = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Check if Enter key is pressed
                if text_input == correct_answer:
                    # Display Congratulations message
                    screen.blit(congratulations_text, congratulations_rect.topleft)
                    pygame.display.flip()
                    pygame.time.delay(2000)  # Display message for 2 seconds
                    pygame.quit()
                    sys.exit()
                else:
                    rect = pygame.Rect((SCREEN_WIDTH - RECT_WIDTH) // 2, 20 + 100*attempts, RECT_WIDTH, RECT_HEIGHT)
                    attempts += 1
                    pygame.display.flip()

            elif event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]
            else:
                text_input += event.unicode

    pygame.draw.rect(screen, BLACK, rect, 2)

    # Render and blit text
    text_surface = font.render(text_input, True, BLACK)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    

# Quit Pygame
pygame.quit()
