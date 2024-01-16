# Display attempt number
    attempt_text = font.render(f"Attempt {attempt + 1}/{attempts}", True, BLACK)
    screen.blit(attempt_text, (10, 10))

    # Display relevant information for the current attempt
    if attempt == 0:
        info_text = font.render(f"Year: {selected_song['year']}, Chart Position: {selected_song['chart_position']}", True, BLACK)
        screen.blit(info_text, (10, 50))
    elif attempt == 1:
        info_text = font.render(f"Genre: {selected_song['genre']}", True, BLACK)
        screen.blit(info_text, (10, 50))
    elif attempt == 2:
        info_text = font.render("Listen to the song intro:", True, BLACK)
        screen.blit(info_text, (10, 50))
        intro_file_path = os.path.join("audio", selected_song["intro_file"])
        play_audio(intro_file_path)
        playing = True
    else:
        info_text = font.render("Listen to the full song:", True, BLACK)
        screen.blit(info_text, (10, 50))
        full_song_file_path = os.path.join("audio", selected_song["full_song_file"])
        play_audio(full_song_file_path)
        playing = True

    # Get user input
    if attempt < 2:
        input_text = font.render("What song is it?", True, BLACK)
        screen.blit(input_text, (10, 100))
        pygame.display.flip()
        guess = input()
    else:
        guess = ""

    # Check guess
    if check_guess(guess, selected_song["title"]):
        result_text = font.render("Correct! You've guessed the song.", True, BLACK)
        screen.blit(result_text, (10, 150))
        pygame.display.flip()
        pygame.time.delay(2000)  # Display the result for 2 seconds
        break
    elif attempt == attempts - 1:
        result_text = font.render(f"Game Over. The correct song was: {selected_song['title']}", True, BLACK)
        screen.blit(result_text, (10, 150))
        pygame.display.flip()
        pygame.time.delay(3000)  # Display the result for 3 seconds

    if playing:
        pygame.mixer.music.stop()  # Stop playing audio
        playing = False