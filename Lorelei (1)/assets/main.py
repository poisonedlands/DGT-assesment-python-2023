
# credit to https://github.com/baraltech/Menu-System-PyGame for the base code, Ronan Cantwell for the background art, and Torbjorn Olykan and William Chisnall for the music.

#import modules 
import pygame, sys
from button import Button
import os

#Starts the modules I'm working with
pygame.init()
pygame.mixer.init()

#Creates and sets the size of the window
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

#Scales and sets the background
DEFAULT_IMAGE_SIZE= (1280,720)
BG = pygame.image.load("assets/Background.png")
BG = pygame.transform.scale(BG,DEFAULT_IMAGE_SIZE)

#Retrive the font file
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

# music loop setup    
pygame.mixer.music.load('assets/Area_theme.wav')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops=1000000)

        
#options screen Game loop
def options():
    while True:
        # Retrives the mous position on the options screen so the buttons can detect a click event
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        #clears the screen
        SCREEN.blit(BG, (0, 0))

        #Setup for the back button
        OPTIONS_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Gold")

        #setup for the play button
        PLAY = Button(image=None, pos = (640, 300),
                            text_input="PAUSE MUSIC", font=get_font(75), base_color="White", hovering_color="Gold")
    
        #setup for the pause button
        PAUSE = Button(image=None, pos = (640, 450),
                            text_input="PLAY MUSIC", font=get_font(75), base_color="White", hovering_color="Gold")
        
        #updates the screen with the buttons
        for button in [OPTIONS_BACK, PAUSE, PLAY]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        #detects if player exits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #detects if the back button is pressed and goes back to main menu if it is
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                #detects if the pause button is pressed and pauses the music if it is
                if PAUSE.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.pause()
                
                #detects if the play button is pressed and plays the music if it is
                if PLAY.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.music.play()

        #updates the screen
        pygame.display.update()

#main screen loop
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        #Retrives the menu mouse position for events such as button actions
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #setup for the play button
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 300), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        #setup for the options button
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 450), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        #setup for the quit button
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 600), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")

        #updates the screen with the buttons
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        #test for button clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #returns if play is clicked
                    return
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #runs option screen if options is clicked
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #quits the game if quit is pressed
                    pygame.quit()
                    sys.exit()

        #updates the screen        
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
    os.system("python assets/lorelei_logic.py")  # Run the game screen after Main_Menu() returns