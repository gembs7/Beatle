import pygame
import sys
import os
import datetime
import asyncio

async def main():
    
    # Initialize Pygame
    pygame.init()
    game = True
    now = datetime.datetime.now()
    day_of_week = now.weekday()
    i = day_of_week


    # Constants
    WIDTH = 480
    HEIGHT = 800
    RECT_WIDTH = 300
    RECT_HEIGHT = 50

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255,0,0)
    GREEN = (0,255,0)

    def copy_to_clipboard(text):
        cmd = 'echo ' + text.strip() + '| clip'
        os.system(cmd)

    def play_audio(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def play_audio3(file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        pygame.time.delay(3000)
        pygame.mixer.music.pause()


    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Beatle by Pogdensburg")

    # Font
    font = pygame.font.Font(None, 24)
    songs = [{"title": "Vampire", "year": 2023, "chart_position": 1, "genre": "Pop", "full_song_file": "or1.mp3", "image": "or1.png", "artist": "Olivia Rodrigo"},
    {"title": "Three Little Birds", "year": 1977, "chart_position": 17, "genre": "Reggae", "full_song_file": "bm1.mp3", "image": "bm1.jpg", "artist": "Bob Marley and The Wailers"},
    {"title": "The Sweet Escape", "year": 2006, "chart_position": 2, "genre": "Pop", "full_song_file": "gs1.mp3", "image": "gs1.jpg", "artist": "Gwen Stefani Featuring Akon"},
    {"title": "Pump It", "year": 2005, "chart_position": 18, "genre": "Pop/Dance", "full_song_file": "bep1.mp3", "image": "bep1.png", "artist": "Black Eyed Peas"},
    {"title": "Somebody's Watching Me", "year": 1984, "chart_position": 2, "genre": "Pop", "full_song_file": "rw1.mp3", "image": "rw1.jpg", "artist": "Rockwell featuring Michael Jackson"},
    {"title": "Back in Black", "year": 1980, "chart_position": 37, "genre": "Rock", "full_song_file": "ac1.mp3", "image": "ac1.jpg", "artist": "AC/DC"},
    {"title": "Radioactive", "year": 2012, "chart_position": 3, "genre": "Rock/Pop", "full_song_file": "id1.mp3", "image": "id1.jpg", "artist": "Imagine Dragons"}]

    song = songs[i]
    # Set up audio
    audio_folder = "musicdata"
    image_folder = "image"
    full_file = song["full_song_file"] # Change this to your audio file
    full_path = os.path.join(audio_folder, full_file)
    image_file = song["image"]
    image_path = os.path.join(image_folder, image_file)  # Replace this with the path to your image file
    try:
        image = pygame.image.load(image_path)
    except:
        image = pygame.image.load(os.path.join(image_folder, "whoops.jpg"))
    image = pygame.transform.scale(image, (150, 150))

    header = pygame.image.load(os.path.join(image_folder,"Beatle.JPG"))
    header = pygame.transform.scale(header, (320, 110))

    share = pygame.image.load(os.path.join(image_folder,"share.png"))
    share = pygame.transform.scale(share, (110, 80))
    share_rect = share.get_rect()
    share_rect.center = (240,750)

    def draw_button(rect, text):
        pygame.draw.rect(screen, (200,40,175), rect)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    def draw_centered_text(text, rect):
        # Render the text
        text_surface = font.render(text, True, BLACK)

        # Get the rectangle for the text surface
        text_rect = text_surface.get_rect()

        # Center the text rectangle within the given rectangle
        text_rect.center = rect.center

        # Draw the text surface onto the screen
        screen.blit(text_surface, text_rect)

    # Rectangle
    rect = pygame.Rect((WIDTH - RECT_WIDTH) // 2, 110, RECT_WIDTH, RECT_HEIGHT)
    rect1 = pygame.Rect((WIDTH - RECT_WIDTH) // 2, 180, RECT_WIDTH, RECT_HEIGHT)
    rect2 = pygame.Rect((WIDTH - RECT_WIDTH) // 2, 250, RECT_WIDTH, RECT_HEIGHT)
    rect3 = pygame.Rect((WIDTH - RECT_WIDTH) // 2, 320, RECT_WIDTH, RECT_HEIGHT)
    rect4 = pygame.Rect((WIDTH - RECT_WIDTH) // 2, 390, RECT_WIDTH, RECT_HEIGHT)
    currentrect = rect
    info_rect = pygame.Rect((WIDTH - 350) // 2, 600, 350, 100)
    border = pygame.Rect(0, 0, WIDTH, HEIGHT)


    # Text input
    text_input = ''
    correct_answer = song["title"]

    info = "Year: " + str(song["year"]) + ", Chart Peak: " + str(song["chart_position"])

    # Congratulations message

    
    

    rect_colors = [RED,BLACK,BLACK,BLACK,BLACK]
    guess_colors = [WHITE,WHITE,WHITE,WHITE,WHITE]
    guess = 0

    #help
    font1 = pygame.font.Font(None, 50)
    help = font1.render(" ? ", True, (10,10,10))
    help_rect = help.get_rect(center=(435,40))


    sharecolor = WHITE
    spam = ""
    spam = font.render(spam,True,WHITE)

    font2 = pygame.font.Font(None, 16)

    def draw_help():
        helper_rect = pygame.Rect(80, 220, 320, 300)
        pygame.draw.rect(screen, WHITE, helper_rect)
        pygame.draw.rect(screen, BLACK, helper_rect, 2)
        font3 = pygame.font.Font(None, 13)
        text_lines = ["Welcome to the Beatle!", "You have five guesses to find the song that matches the clues. The clues are:",
                    "1. Year and Billboard Top 100 Chart Position", "2. Song Genre", "3. The song's intro (click to play)",
                    "4. Song Artist", "5. Song" ]
        text_surfaces = [font3.render(line, True, BLACK) for line in text_lines]
        for i, text_surface in enumerate(text_surfaces):
            text_rect = text_surface.get_rect(center=(WIDTH // 2, 250 + i * 40))
            screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
        pygame.time.delay(5000)

    def do_share():
        sharetext = "Beatle: "
        correct = False
        x = 0
        for i in guess_colors:
            x = x+1
            if i == GREEN:
                z = x
                correct = True
                sharetext1 = sharetext + "🟩"
            elif i == RED:
                sharetext1 = sharetext + "🟥"
            elif i == BLACK:
                sharetext1 = sharetext + "⬛"
            elif i == WHITE:
                sharetext1 = sharetext + "⬜"
        if correct:
            sharetext = sharetext + "Correct! " + (str(z)) + "/5. Wow"
        else:
            sharetext = sharetext + "WRONG! " + (str(0)) + "/5. Wow"


        copy_to_clipboard(sharetext)
        spam = "Copied to Clipboard!"
        spam = font.render(spam,True,WHITE)
        sharecolor = (0,155,0)
        spam_rect = spam.get_rect(center=(380, 740))
        pygame.draw.rect(screen, sharecolor, spam_rect)
        screen.blit(spam, spam_rect.topleft)
        pygame.display.flip()
        pygame.time.delay(4000)
        
        sharecolor = WHITE
        


    def congrats():
        congratulations_text = font2.render("Congratulations! The song was: " + song["title"] + ", by " + song["artist"], True, BLACK)
        congratulations_rect = congratulations_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        # Display Congratulations message
        screen.fill(WHITE)
        guess_colors[guess] = GREEN
        screen.blit(congratulations_text, congratulations_rect.topleft)
        
        
        pygame.draw.rect(screen, guess_colors[0], rect)
        pygame.draw.rect(screen, guess_colors[1], rect1)
        pygame.draw.rect(screen, guess_colors[2], rect2)
        pygame.draw.rect(screen, guess_colors[3], rect3)
        pygame.draw.rect(screen, guess_colors[4], rect4)
        
        pygame.draw.rect(screen, WHITE, help_rect)
        pygame.draw.rect(screen, BLACK, help_rect, 2)

        image_rect = image.get_rect(center = info_rect.center)
        screen.blit(image, image_rect)

        header_rect = header.get_rect()
        header_rect.topleft = (66, 0)

        
        screen.blit(header, header_rect)
        
        screen.blit(help,help_rect)

        pygame.draw.rect(screen, (200,40,175), border, 15)

        
        share_rect = share.get_rect()
        share_rect.center = (240,750)
        screen.blit(share,share_rect)

        spam_rect = spam.get_rect(center=(WIDTH // 2, 700))
        pygame.draw.rect(screen, sharecolor, spam_rect)
        screen.blit(spam, spam_rect.center)

        pygame.display.flip()
        game = False

    def idiot():
        idiot_text = font2.render("You lose chump! The song was: " + song["title"] + ", by " + song["artist"], True, BLACK)
        idiot_rect = idiot_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
        screen.fill(WHITE)
        screen.blit(idiot_text, idiot_rect.topleft)
        
        image_rect = image.get_rect(center = info_rect.center)
        screen.blit(image, image_rect)
        header_rect = header.get_rect()
        header_rect.topleft = (66, 0)
        screen.blit(header, header_rect)
        pygame.draw.rect(screen, guess_colors[0], rect)
        pygame.draw.rect(screen, guess_colors[1], rect1)
        pygame.draw.rect(screen, guess_colors[2], rect2)
        pygame.draw.rect(screen, guess_colors[3], rect3)
        pygame.draw.rect(screen, guess_colors[4], rect4)
        pygame.draw.rect(screen, (200,40,175), border, 15)
        pygame.draw.rect(screen, WHITE, help_rect)
        pygame.draw.rect(screen, BLACK, help_rect, 2)
        screen.blit(help,help_rect)

        share_rect = share.get_rect()
        share_rect.center = (240,750)
        screen.blit(share,share_rect)

        spam_rect = spam.get_rect(center=(WIDTH // 2, 700))
        pygame.draw.rect(screen, sharecolor, spam_rect)
        screen.blit(spam, spam_rect.center)
        pygame.display.flip()
        game = False

    def drawgame():
        # Clear the screen
        screen.fill(WHITE)

        if guess == 2:
            play_button_rect = info_rect
            draw_button(play_button_rect, "Song Intro")
        if guess == 4:
            play_button_rect = info_rect
            draw_button(play_button_rect, "Full Song")


        #header
        header_rect = header.get_rect()
        header_rect.topleft = (66, 0)
        screen.blit(header, header_rect)

        #help
        
        pygame.draw.rect(screen, WHITE, help_rect)
        pygame.draw.rect(screen, BLACK, help_rect, 2)
        screen.blit(help,help_rect)

        #border
        pygame.draw.rect(screen, (200,40,175), border, 15)

        #color rectangles
        pygame.draw.rect(screen, guess_colors[0], rect)
        pygame.draw.rect(screen, guess_colors[1], rect1)
        pygame.draw.rect(screen, guess_colors[2], rect2)
        pygame.draw.rect(screen, guess_colors[3], rect3)
        pygame.draw.rect(screen, guess_colors[4], rect4)

        # Draw rectangle
        pygame.draw.rect(screen, rect_colors[0], rect, 2)
        pygame.draw.rect(screen, rect_colors[1], rect1, 2)
        pygame.draw.rect(screen, rect_colors[2], rect2, 2)
        pygame.draw.rect(screen, rect_colors[3], rect3, 2)
        pygame.draw.rect(screen, rect_colors[4], rect4, 2)

        pygame.draw.rect(screen, BLACK, info_rect, 2)

        # Render and blit text
        text_surface = font.render(text_input, True, BLACK)
        text_rect = text_surface.get_rect(center=currentrect.center)
        screen.blit(text_surface, text_rect)

        draw_centered_text(info, info_rect)

        # Update the display
        pygame.display.flip()
    
    drawgame()
    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                    try:
                        if info_rect.collidepoint(event.pos):
                            if guess == 2:
                                play_audio3(full_path)
                            else:
                                play_audio(full_path)
                    except:
                        pass
                    if help_rect.collidepoint(event.pos):
                        
                        draw_help()
                        
                        
                    if share_rect.collidepoint(event.pos):
                        
                        do_share()
                        await asyncio.sleep(4)
                        

                        
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check if Enter key is pressed
                    if text_input.upper() == correct_answer.upper():
                        
                        congrats()
                        game = False
                        
                    else:
                        rect_colors[guess] = BLACK
                        try:    
                            rect_colors[guess+1] = RED
                        except:
                            pass
                        if text_input == "":
                            guess_colors[guess] = BLACK
                        else: guess_colors[guess] = RED
                        
                        guess += 1
                        text_input = ''
                        if guess == 1:
                            currentrect = rect1
                            info = "Genre: " + song["genre"]
                        elif guess == 2:
                            currentrect = rect2
                            info = ""
                            
                        elif guess == 3: 
                            currentrect = rect3
                            info = "Artist: " + song["artist"]
                        
                        elif guess == 4:
                            currentrect = rect4
                            info = ""
                        else: 
                            idiot()
                            game = False
                            await asyncio.sleep(5)

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

                if game:
                    drawgame()
        await asyncio.sleep(0)

asyncio.run(main())
