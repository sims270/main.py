"""
This script is a Pygame-based game where the player controls a dinosaur character
navigating through a series of obstacles. Pygame is a set of Python modules
designed for writing video games, providing functionalities for creating graphics,
sound, and handling user input.

Key Components:
1. Initialization: Pygame is initialized using `pygame.init()`, preparing the
   framework for use.

2. Game Settings: Global variables like `game_speed`, `x_pos_bg`, `y_pos_bg`,
   and `points` are defined for tracking game dynamics and scoring.

3. Main Game Loop: The `main` function contains the core game loop. This loop
   continuously checks for events (like key presses or the window closing),
   updates game state, and redraws the screen.

    a. Event Handling: Pygame's event system is used to respond to key presses
       and window closing events.
    b. Graphics Rendering: Game entities like the dinosaur, clouds, and obstacles
       are drawn onto the game window (`SCREEN`). Pygame functions like `blit`
       are used for drawing.
    c. Collision Detection: Pygame's rectangle collision feature is used to
       detect collisions between the dinosaur and obstacles.
    d. Scoring: Points are incremented based on game progress.

4. Game Pause and Unpause: Functions `paused` and `unpause` manage the game's
   pause state. During a pause, the game loop halts its usual update and draw
   cycle.

5. Background Management: The `background` function handles the scrolling
   background effect, giving a sense of movement.

6. Obstacle Management: Obstacles are dynamically generated and managed,
   offering variety and challenge in the gameplay.

7. Menu System: The `menu` function provides a start/restart interface and
   displays the player's score. It's also responsible for initiating the main
   game loop.

Pygame Functions:
- `pygame.init()`: Initializes all imported Pygame modules.
- `pygame.time.Clock()`: Creates an object to help track time.
- `clock.tick(fps)`: Limits the game loop to a maximum framerate.
- `pygame.display.update()`: Updates the contents of the entire display.
- `pygame.key.get_pressed()`: Gets the state of all keyboard buttons.
- `pygame.event.get()`: Retrieves all events from the event queue.
- `pygame.quit()`: Uninitializes all Pygame modules.
- `SCREEN.blit()`: Draws one image onto another.

This game is a simple yet engaging implementation demonstrating various aspects
of game development using Pygame, including graphics rendering, event handling,
collision detection, and game state management.
"""
import os

from resources import RUNNING
import pygame
import random
import threading
from settings import SCREEN_WIDTH, SCREEN, SCREEN_HEIGHT, GAME_SPEED
from dinosaur import Dinosaur2, Stitch
from cloud import Cloud
from obstacles import SmallCactus, LargeCactus, Bird
from resources import BG, SMALL_CACTUS, LARGE_CACTUS, BIRD
import datetime
from multiplayer import Multiplayer
import time
pygame.mixer.init()
mp3_file_path = "Lied.mp3"
pygame.mixer.music.load(mp3_file_path)
pygame.mixer.music.play()# Spiele die MP3-Datei ab

# Initialize Pygame
pygame.init()

# List to store obstacles
obstacles = []

def load_highscore():
    with open("highscore.txt" , "r") as f:
        content = f.read()
        return int(content)

def save_highscore(points):
    with open("highscore.txt" , "w") as f:
       f.write(str(points))

skin_wert = 1
def shop_layout():
    global points,skin_wert
    run_shop = True

    while run_shop:
        SCREEN.fill((128, 128, 128))  # Fülle den Bildschirm mit einer Hintergrundfarbe für den Shop

        # Zeige die verfügbaren Gegenstände im Shop an
        font = pygame.font.Font("freesansbold.ttf", 30)
        shop_text = font.render("Welcome to the Shop", True, FONT_COLOR)

        dino =  pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
        stitch = pygame.image.load(os.path.join("assets/Stitch", "stitch1sprung.png"))
        SCREEN.blit(dino, (400, 200))
        SCREEN.blit(stitch, (600, 200))


        item1_text = font.render("1", True, FONT_COLOR)
        item2_text = font.render("2", True, FONT_COLOR)

        back_text = font.render("Press 'B' to go back", True, FONT_COLOR)

        shop_text_rect = shop_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        item1_text_rect = item1_text.get_rect(center=(450, 330))
        item2_text_rect = item2_text.get_rect(center=(650, 330))
        back_text_rect = back_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))

        SCREEN.blit(shop_text, shop_text_rect)
        SCREEN.blit(item1_text, item1_text_rect)
        SCREEN.blit(item2_text, item2_text_rect)
        SCREEN.blit(back_text, back_text_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run_shop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:  # Beispiel: B als Taste zum Zurückgehen
                    run_shop = False
                if event.key == pygame.K_1:
                    skin_wert = 1
                if event.key == pygame.K_2:
                    skin_wert = 2




def main_menu():

    run = True
    selected = 0  # 0 for 'Start Game', 1 for Muliplayer, 2 for 'Quit'

    while run:
        SCREEN.fill((0, 0, 0))  # Black background for the menu

        font = pygame.font.Font("freesansbold.ttf", 30)
        title = font.render("Dinosaur Game", True, FONT_COLOR)

        # Options text
        if selected == 0:
            start_game = font.render("Solo Game <--", True, FONT_COLOR)
            multiplayer_game = font.render("Multiplayer", True, FONT_COLOR)
            shop = font.render("Shop", True, FONT_COLOR)

            quit_game = font.render("Quit", True, FONT_COLOR)
        elif selected == 1:
            start_game = font.render("Solo Game", True, FONT_COLOR)
            multiplayer_game = font.render("Multiplayer<--", True, FONT_COLOR)
            shop = font.render("Shop", True, FONT_COLOR)

            quit_game = font.render("Quit", True, FONT_COLOR)
        elif selected == 2:
            start_game = font.render("Solo Game", True, FONT_COLOR)
            multiplayer_game = font.render("Multiplayer ", True, FONT_COLOR)
            shop = font.render("Shop <--", True, FONT_COLOR)

            quit_game = font.render("Quit", True, FONT_COLOR)



        else:
            start_game = font.render("Solo Game", True, FONT_COLOR)
            multiplayer_game = font.render("Multiplayer", True, FONT_COLOR)
            shop = font.render("Shop", True, FONT_COLOR)
            setting = font.render("Setting", True, FONT_COLOR)
            quit_game = font.render("Quit <--", True, FONT_COLOR)

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        start_game_rect = start_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5))
        multiplayer_game_rect = multiplayer_game.get_rect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 ))
        shop_rect = shop.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 35))

        quit_game_rect = quit_game.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

        SCREEN.blit(title, title_rect)
        SCREEN.blit(start_game, start_game_rect)
        SCREEN.blit(multiplayer_game, multiplayer_game_rect)
        SCREEN.blit(shop, shop_rect)

        SCREEN.blit(quit_game, quit_game_rect)

        pygame.display.update()

        # Switch between the options
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % 4
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % 4

                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        run = False
                        main()
                    if selected == 1:

                        multiplayer_game = Multiplayer()
                        multiplayer_game.multiplayer_menu()
                    elif selected == 2:
                        shop_layout()

                    else:
                        pygame.quit()
                        quit()



def main():


    # Global variables for game settings
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles,skin_wert


    # Set initial game state
    run = True
    clock = pygame.time.Clock()
    if skin_wert == 1:
        player = Dinosaur2()
    elif skin_wert == 2:
        player = Stitch()
    cloud = Cloud()
    obstacles = []
    game_speed = GAME_SPEED
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    death_count = 0
    pause = False


    # Function to handle scoring
    def score():

        global points, game_speed
        points +=1 #Erhöht score jedes mal wenn updated wird um 1
        old_score = load_highscore() #von funktion alten Punkte werden gelesen und geschaut ob alt oder neu höher ist höheres wird gespeichert
        if old_score> points:
            save_highscore(old_score)
        else:
            save_highscore(points)






    # Function to handle background movement
    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed + 8


    # Function to unpause the game
    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    # Function to pause the game
    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Paused, Press 'u' to Unpause", True, FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()

    # Main game loop
    while run:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused()





        # Wenn es zwischen 6 und 22 Uhr ist, ist es hell- zwischen 22 und 6 Uhr ist es dunkel
        time = datetime.datetime.now()
        time_hour = time.hour
        if time_hour >= 22:
            SCREEN.fill((0, 0, 0))
        elif time_hour >=6:
            SCREEN.fill((255, 255,255))

        # Get user input
        userInput = pygame.key.get_pressed()


        # Update and draw player and cloud
        player.draw(SCREEN)
        player.update(userInput)

        cloud.draw(SCREEN)
        cloud.update()


        # Handle obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2500)
                death_count += 1
                with open("deathfile.txt", "r") as f:
                    f.read(death_count)
                with open("deathfile.txt", "a") as f:
                    f.write(str(1))

                menu(death_count)



        # Update background and score
        background()
        score()


        # Update display and tick clock
        clock.tick(30)
        pygame.display.update()

def menu(death_count):


    global points  # Access the global points variable to display the score.


    global FONT_COLOR  # Access the global font color variable for consistent text color.
    run = True  # Flag to keep the menu loop running.

    while run:
        FONT_COLOR = (255, 255, 255)  # Set the font color to white for visibility.
        SCREEN.fill((128, 128, 128))  # Fill the screen with a grey color as the background of the menu.
        pygame.font.init()  # Initialize Pygame font module.
        font = pygame.font.Font("freesansbold.ttf", 30)  # Set the font and size for the text.

        # Check if it's the start of the game or a restart after death.
        if death_count == 0:
            main_menu()


        elif death_count > 0:
            # Display a message to restart the game and the last score.
            text = font.render("Press any Key to Restart", True, FONT_COLOR)
            # Anzeige für score
            score = font.render("Your Score: " + str(points), True, FONT_COLOR)
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)  # Draw the score on the screen.
            #Anzeige für highscore
            high_score = load_highscore()  # Die Zahl die im Text file "highscore.txt" steht wird aufgerufen
            highscore = font.render("Highscore: " + str(high_score), True, FONT_COLOR)
            highscoreRect = highscore.get_rect()
            highscoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100) # Plaziert highscore auf dem display
            SCREEN.blit(highscore,highscoreRect)

            #Anzeige Tode
            with open("deathfile.txt", "r") as f:
                death = f.read()
            deathcount = font.render("Tode: " + str(len(death)), True, FONT_COLOR)
            deathcountRect = deathcount.get_rect()
            deathcountRect.topleft = (SCREEN_WIDTH // 5 - 200 , SCREEN_HEIGHT // 6 -70)  # Plaziert Tode auf dem display
            SCREEN.blit(deathcount, deathcountRect)






        # Render the text and position it on the screen.
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)  # Draw the text on the screen.

        # Display an image representing the game character.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))

        pygame.display.update()  # Update the entire screen with everything drawn.

        # Event loop to handle window closing and key presses.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                # Quit the game if the window close button is clicked.
                run = False
                with open("deathfile.txt", "w") as f:   # Wenn das Spiel beendet wird die deathfile.txt geleert
                    f.write(str())


                pygame.display.quit()
                pygame.quit()
                exit()


            if event.type == pygame.KEYDOWN:
                # Start the main game loop if any key is pressed.
                main()



t1 = threading.Thread(target=menu(death_count=0), daemon=True)
pygame.init()
t1.start()
