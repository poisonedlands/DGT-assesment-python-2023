#https://chat.openai.com

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Platform sizes
platform_width = 64
platform_height = 64

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")

# Load the background image (same as before)
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the ground image
ground_image = pygame.image.load("ground.jpg")
ground_image = pygame.transform.scale(ground_image, (SCREEN_WIDTH, platform_height))

# Load the platform image
platform_image = pygame.image.load("platform.jpg")
platform_image = pygame.transform.scale(platform_image, (platform_width, platform_height))

# Function to draw the player (same as before)

# Function to draw a platform using the platform image
def draw_platform(x, y):
    screen.blit(platform_image, (x, y))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player settings
player_width = 40
player_height = 60
player_velocity = 5
player_jump_power = 10

# Platform settings
platform_width = 100
platform_height = 20

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_width, player_height))

# Function to draw a platform
def draw_platform(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, platform_width, platform_height))

# Main game loop (same as before)
def main():
    # Initial player position
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y = SCREEN_HEIGHT - player_height - platform_height

    # Initial player velocity
    player_dx = 0
    player_dy = 0

    # Platforms in the sky
    platforms = [
        (200, 400),
        (400, 300),
        (600, 200)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get the state of all keyboard buttons
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_LEFT]:
            player_dx = -player_velocity
        elif keys[pygame.K_RIGHT]:
            player_dx = player_velocity
        else:
            player_dx = 0

        # Vertical movement (jumping)
        if keys[pygame.K_SPACE] and player_y >= SCREEN_HEIGHT - player_height - platform_height:
            player_dy = -player_jump_power

        # Apply gravity
        player_dy += 1

        # Update player position
        player_x += player_dx
        player_y += player_dy

        # Collide with the ground and platforms
        if player_y >= SCREEN_HEIGHT - player_height - platform_height:
            player_y = SCREEN_HEIGHT - player_height - platform_height
            player_dy = 0
        for platform_x, platform_y in platforms:
            if player_x + player_width > platform_x and player_x < platform_x + platform_width and \
               player_y + player_height >= platform_y and player_y + player_dy < platform_y:
                player_y = platform_y - player_height
                player_dy = 0

        # Clear the screen
        screen.fill(BLACK)

        # Draw ground and platforms
        pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - platform_height, SCREEN_WIDTH, platform_height))
        for platform_x, platform_y in platforms:
            draw_platform(platform_x, platform_y)

        # Draw the player
        draw_player(player_x, player_y)

        # Update the display
        pygame.display.update()



def main():   
    # Start the game (same as before)
    if __name__ == "__main__":
        main()