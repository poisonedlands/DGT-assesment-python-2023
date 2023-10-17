
# credit to https://github.com/baraltech/Menu-System-PyGame for the base code, Ronan Cantwell for the background art, and Torbjorn Olykan and William Chisnall for the music.
# also credit to everybody at luscious locks game dev (now collapsed XD) who helped with the panning stages.

#import modules 
import pygame, sys
from button import Button
import os
import subprocess

#Starts the modules I'm working with
pygame.init()
pygame.mixer.init()

#Creates and sets the size of the window
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#Scales and sets the background
DEFAULT_IMAGE_SIZE= (1280,720)
BG = pygame.image.load("Background.png")
BG = pygame.transform.scale(BG,DEFAULT_IMAGE_SIZE)

#Retrive the font file
def get_font(size): 
    return pygame.font.Font("font.ttf", size)

# music loop setup    
pygame.mixer.music.load('Area_theme.wav')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops=1000000)

        
#options screen Game loop
def options():
    while True:
        # Retrieves the mouse position on the options screen so the buttons can detect a click event
        options_mouse_pos = pygame.mouse.get_pos()
        #clears the screen
        SCREEN.blit(BG, (0, 0))
        #Setup for the back button
        options_back = Button(image=None, pos=(640, 600),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Gold")
        #setup for the play button
        pause = Button(image=None, pos = (640, 300),
                            text_input="PAUSE MUSIC", font=get_font(75), base_color="White", hovering_color="Gold")
    
        #setup for the pause button
        play = Button(image=None, pos = (640, 450),
                            text_input="PLAY MUSIC", font=get_font(75), base_color="White", hovering_color="Gold")
        
        #updates the screen with the buttons
        for button in [options_back, pause, play]:
            button.changeColor(options_mouse_pos)
            button.update(SCREEN)

        #detects if player exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #detects if the back button is pressed and goes back to main menu if it is
                if options_back.checkForInput(options_mouse_pos):
                    main_menu()
                #detects if the pause button is pressed and pauses the music if it is
                if pause.checkForInput(options_mouse_pos):
                    pygame.mixer.music.pause()
                
                #detects if the play button is pressed and plays the music if it is
                if play.checkForInput(options_mouse_pos):
                    pygame.mixer.music.play()

        #updates the screen
        pygame.display.update()

#main screen loop
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        #Retrives the menu mouse position for events such as button actions
        menu_mouse_pos = pygame.mouse.get_pos()

        #setup for the play button
        play_button = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 300),
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        #setup for the options button
        options_button = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 450),
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        #setup for the quit button
        quit_button = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 600),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")

        #updates the screen with the buttons
        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(SCREEN)
        
        #test for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    #returns if play is clicked
                    return
                if options_button.checkForInput(menu_mouse_pos):
                    #runs option screen if options is clicked
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    #quits the game if quit is pressed
                    pygame.quit()
                    sys.exit()

        #updates the screen        
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
    subprocess.call([sys.executable , "lorelei_logic.py"])  # Run the game screen after Main_Menu() returns