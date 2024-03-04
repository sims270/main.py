from resources import RUNNING
import pygame
import random
import threading
from settings import SCREEN_WIDTH, SCREEN, SCREEN_HEIGHT, GAME_SPEED
from dinosaur import Dinosaur, Dinosaur2

from cloud import Cloud
from obstacles import SmallCactus, LargeCactus, Bird
from resources import BG, SMALL_CACTUS, LARGE_CACTUS, BIRD
import datetime



class Multiplayer:
    def load_highscore(self):
        with open("highscore_team.txt", "r") as f:
            content = f.read()
            return int(content)

    def save_highscore(self,points):
        with open("highscore_team.txt", "w") as f:
            f.write(str(points))

    def teamplayer_main(self):
        # Global variables for game settings
        global game_speed, x_pos_bg, y_pos_bg, points, obstacles

        # Set initial game state
        run = True
        clock = pygame.time.Clock()
        player = Dinosaur()
        player2 = Dinosaur2()
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
            points += 1  # Erhöht score jedes mal wenn updated wird um 1
            old_score = self.load_highscore()  # von funktion alten Punkte werden gelesen und geschaut ob alt oder neu höher ist höheres wird gespeichert
            if old_score > points:
                self.save_highscore(old_score)
            else:
                self.save_highscore(points)

        # Function to handle background movement
        def background():
            global x_pos_bg, y_pos_bg
            image_width = BG.get_width()
            SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            if x_pos_bg <= -image_width:
                x_pos_bg = 0
            x_pos_bg -= game_speed

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
            elif time_hour >= 6:
                SCREEN.fill((255, 255, 255))

            # Get user input
            userInput = pygame.key.get_pressed()

            # Update and draw player and cloud
            player.draw(SCREEN)
            player.update(userInput)
            player2.draw(SCREEN)
            player2.update(userInput)
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
                    pygame.time.delay(1000)
                    death_count += 1
                    with open("deathfile.txt",
                              "r") as f:
                        f.read(death_count)
                    with open("deathfile.txt", "a") as f:
                        f.write(str(1))
                    self.menu(death_count)

                if player2.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(1000)
                    death_count +=1

                    with open("deathfile.txt","r") as f:
                        f.read(death_count)
                    with open("deathfile.txt", "a") as f:
                        f.write(str(1))
                    self.menu(death_count)

            # Update background and score
            background()
            score()

            # Update display and tick clock
            clock.tick(30)
            pygame.display.update()

    def fightplayer_main(self):
        # Global variables for game settings
        global game_speed, x_pos_bg, y_pos_bg, points, obstacles

        # Set initial game state
        run = True
        clock = pygame.time.Clock()
        player = Dinosaur()
        player2 = Dinosaur2()
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
            points += 1  # Erhöht score jedes mal wenn updated wird um 1
            old_score = self.load_highscore()  # von funktion alten Punkte werden gelesen und geschaut ob alt oder neu höher ist höheres wird gespeichert
            if old_score > points:
                self.save_highscore(old_score)
            else:
                self.save_highscore(points)

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
            elif time_hour >= 6:
                SCREEN.fill((255, 255, 255))

            # Get user input
            userInput = pygame.key.get_pressed()

            # Update and draw player and cloud
            player.draw(SCREEN)
            player.update(userInput)
            player2.draw(SCREEN)
            player2.update(userInput)
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
                    with open("deathfile.txt","r") as f:
                        f.read(death_count)
                    with open("deathfile.txt", "a") as f:
                        f.write(str(1))
                    player.isdead = True

                if player2.dino_rect.colliderect(obstacle.rect):

                    with open("deathfile.txt","r") as f:
                        f.read(death_count)
                    with open("deathfile.txt", "a") as f:
                        f.write(str(1))
                    player2.isdead = True

            if player.isdead and player2.isdead:
                death_count += 1
                self.menu(death_count)



            # Update background and score
            background()
            score()

            # Update display and tick clock
            clock.tick(30)
            pygame.display.update()

    def menu(self,death_count):
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
                self.teamplayer_main()


            elif death_count > 0:
                # Display a message to restart the game and the last score.
                text = font.render("Press any Key to Restart", True, FONT_COLOR)
                # Anzeige für score
                score = font.render("Your Score: " + str(points), True, FONT_COLOR)
                scoreRect = score.get_rect()
                scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
                SCREEN.blit(score, scoreRect)  # Draw the score on the screen.
                # Anzeige für highscore
                high_score = self.load_highscore()  # Die Zahl die im Text file "highscore.txt" steht wird aufgerufen
                highscore = font.render("Highscore: " + str(high_score), True, FONT_COLOR)
                highscoreRect = highscore.get_rect()
                highscoreRect.center = (
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)  # Plaziert highscore auf dem display
                SCREEN.blit(highscore, highscoreRect)

                # Anzeige Tode
                with open("deathfile.txt", "r") as f:
                    death = f.read()
                deathcount = font.render("Tode: " + str(len(death)), True, FONT_COLOR)
                deathcountRect = deathcount.get_rect()
                deathcountRect.topleft = (
                SCREEN_WIDTH // 5 - 200, SCREEN_HEIGHT // 6 - 70)  # Plaziert Tode auf dem display
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
                    with open("deathfile.txt", "w") as f:  # Wenn das Spiel beendet wird die deathfile.txt geleert
                        f.write(str())

                    pygame.display.quit()
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    # Start the main game loop if any key is pressed.
                    self.fightplayer_main()


    def multiplayer_menu(self):
        run = True
        selected = 0  # 0 for 'Start Game', 1 for Muliplayer, 2 for 'Quit'
        FONT_COLOR = (255, 255, 255)

        while run:
            SCREEN.fill((0, 0, 0))  # Black background for the menu

            font = pygame.font.Font("freesansbold.ttf", 30)
            title = font.render("Dinosaur Game", True, FONT_COLOR)

            # Options text
            if selected == 0:
                together = font.render("Team Game <--",True, FONT_COLOR)
                fight = font.render("Fight Game", True, FONT_COLOR)
                back_to_lobby = font.render("Back to Start", True, FONT_COLOR)
            elif selected == 1:
                together = font.render("Team Game ", True, FONT_COLOR)
                fight = font.render("Fight Game <--", True, FONT_COLOR)
                back_to_lobby = font.render("Back to Start", True, FONT_COLOR)

            else:
                together = font.render("Team Game ", True, FONT_COLOR)
                fight = font.render("Fight Game", True, FONT_COLOR)
                back_to_lobby = font.render("Back to Start <--", True, FONT_COLOR)

            title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
            together_rect = together.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.5))
            fight_rect = fight.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            back_to_lobby_rect = back_to_lobby.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

            SCREEN.blit(title, title_rect)
            SCREEN.blit(together,together_rect)
            SCREEN.blit(fight, fight_rect)
            SCREEN.blit(back_to_lobby, back_to_lobby_rect)

            pygame.display.update()

            # Switch between the options
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected = (selected + 1) % 3
                    elif event.key == pygame.K_UP:
                        selected = (selected - 1) % 3

                    elif event.key == pygame.K_RETURN:
                        if selected == 0:
                            run = False
                            self.teamplayer_main()
                        elif selected == 1:
                            run = True
                            self.fightplayer_main()
                        else:
                            return 0








