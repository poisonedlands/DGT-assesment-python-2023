
import pygame
import sys
from button import Button

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((1280, 720))


def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)


def main():
    Looped = False
    SCREEN.fill("black")
    while True:
        
        MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("Welcome to Lorelei", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)

        PLAY_TEXT = get_font(45).render("Please select a character", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)

        Wulf_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(380, 600), 
                            text_input="Wulf", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        
        Heidi_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(900, 600), 
                            text_input="Heidi", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        
        for button in [Heidi_BUTTON,Wulf_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Heidi_BUTTON.checkForInput(MOUSE_POS):
                        Heidi_room()

                    if Wulf_BUTTON.checkForInput(MOUSE_POS):
                        Wulf_room()
        Looped = True
    pygame.display.update()
    
def Heidi_room():
    Looped = False
    SCREEN.fill("Pink")
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("Good choice!", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)
        
        PLAY_TEXT = get_font(45).render("Heidi is very intelligent,", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)       
        PLAY_TEXT = get_font(45).render("but not very strong.", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()        

        if Looped == False:
            pygame.time.delay(2000)
        
        PLAY_TEXT = get_font(45).render("Are you happy with ", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("this desiscion?", True, "Black")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)

        YES_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(380, 600), 
                            text_input="Yes", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        
        NO_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(900, 600), 
                            text_input="No", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        
        for button in [YES_BUTTON,NO_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if YES_BUTTON.checkForInput(MOUSE_POS):
                        room_1()

                    if NO_BUTTON.checkForInput(MOUSE_POS):
                        main()

        Looped = True
    pygame.display.update()

def Wulf_room():
    Looped = False
    SCREEN.fill("Blue")
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("Good choice!", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)
        
        PLAY_TEXT = get_font(45).render("Wulf is very strong,", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)       
        PLAY_TEXT = get_font(45).render("but not very intelligent.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()        

        if Looped == False:
            pygame.time.delay(2000)
        
        PLAY_TEXT = get_font(45).render("Are you happy with ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("this desiscion?", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)

        YES_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(380, 600), 
                            text_input="Yes", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        
        NO_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(900, 600), 
                            text_input="No", font=get_font(75), base_color="#d7fcd4", hovering_color="Gold")
        
        for button in [YES_BUTTON,NO_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if YES_BUTTON.checkForInput(MOUSE_POS):
                        room_1()

                    if NO_BUTTON.checkForInput(MOUSE_POS):
                        main()

        Looped = True
    pygame.display.update()      

def room_1():
    Looped=False
    SCREEN.fill("Black")
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("Long ago on the river rhine,", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)
        
        PLAY_TEXT = get_font(45).render("There was once a maiden by ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)       
        PLAY_TEXT = get_font(45).render("the name of Lorelei.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()        

        if Looped == False:
            pygame.time.delay(2000)
        
        PLAY_TEXT = get_font(45).render("But her lover was unfaithful", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("to her,", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 400))

        if Looped == False:
            pygame.time.delay(2000)

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("and so she threw herself", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 450))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("into the river rhine", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 500))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)

        CONTINUE_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 600), 
                            text_input="Continue", font=get_font(45), base_color="#d7fcd4", hovering_color="Gold")
        
        for button in [CONTINUE_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CONTINUE_BUTTON.checkForInput(MOUSE_POS):
                        room_2()
        Looped = True

def room_2():
    Looped=False
    SCREEN.fill("Black")
    while True:
        MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("But death was not the end", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 200))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()
        PLAY_TEXT = get_font(45).render("for she was immortalised", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)       
        PLAY_TEXT = get_font(45).render("As a siren,", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()        

        if Looped == False:
            pygame.time.delay(3000)
        
        PLAY_TEXT = get_font(45).render("forever singing on top ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("of the bank of the river,", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 400))

        if Looped == False:
            pygame.time.delay(2000)

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("Luring sailors ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 450))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        PLAY_TEXT = get_font(45).render("to thier deaths. ", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 500))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        pygame.display.update()

        if Looped == False:
            pygame.time.delay(2000)

        CONTINUE_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 600), 
                            text_input="Continue", font=get_font(45), base_color="#d7fcd4", hovering_color="Gold")
        
        for button in [CONTINUE_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CONTINUE_BUTTON.checkForInput(MOUSE_POS):
                        sys.exit
                        pygame.quit
        Looped = True



main()