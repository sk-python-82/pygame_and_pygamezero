import pygame
from pygame.locals import *
import random

pygame.init()
running = True

width, height = 800, 567
x, y = width / 2, height / 2

screen = pygame.display.set_mode((width, height))
pygame.display.update()

# Load the song
pygame.mixer.music.load("C:/Users/Asus/Desktop/game_holloween/songs/song.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Load the image
bg = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/garden.png")
girl = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/girl.png")
flower1 = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/purple_flower.png")
pink_flower = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/pink_flower.png")

girl_rect = girl.get_rect(center=(x, y))

# Create a list of Rect objects for the flowers with random positions
flowers = [flower1.get_rect(topleft=(random.randint(0, width - 50), random.randint(0, height - 50))) for _ in range(10)]

font = pygame.font.Font(None, 36)  # Create a font object for flower counter
timer_font = pygame.font.Font(None, 36)  # Create a font object for the timer

flowers_collected = 0  # Initialize the count of collected flowers
pink_flower_displayed = False  # To track if the pink flower has been displayed

# Countdown timer variables
countdown_timer = 20  # Initial value of the timer
timer_location = (width - 150, 10)  # Top right corner for timer display
timer_color = (0, 0, 0)  # Timer text color
countdown_delay = 1000  # Countdown delay in milliseconds
last_countdown_time = pygame.time.get_ticks()

# Control girl movement
movement_delay = 200  # Adjust this value for smoother movement

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[K_RIGHT] and girl_rect.right < width:
        girl_rect.move_ip(3, 0)
    if keys[K_LEFT] and girl_rect.left > 0:
        girl_rect.move_ip(-3, 0)
    if keys[K_UP] and girl_rect.top > 0:
        girl_rect.move_ip(0, -3)
    if keys[K_DOWN] and girl_rect.bottom < height:
        girl_rect.move_ip(0, 3)

    # Check for collisions between the girl and flowers
    for flower in flowers[:]:
        if girl_rect.colliderect(flower):
            flowers.remove(flower)
            flowers_collected += 1

    # Display the pink flower when 10 flowers are collected
    if flowers_collected >= 10 and not pink_flower_displayed:
        pink_flower_displayed = True

    # Update the countdown timer
    if current_time - last_countdown_time >= countdown_delay and countdown_timer > 0:
        countdown_timer -= 1
        last_countdown_time = current_time

    # Display the timer text
    timer_text = timer_font.render(f"Timer: {countdown_timer}", True, timer_color)

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Display each remaining flower
    for flower in flowers:
        screen.blit(flower1, flower)

    screen.blit(girl, girl_rect)

    # Display the "flowers collected" text
    flower_text = font.render(f"Flowers collected: {flowers_collected}", True, (0, 0, 0))
    screen.blit(flower_text, (10, 10))  # Position the flower counter in the top-left corner

    # Display the countdown timer in the top right corner
    screen.blit(timer_text, timer_location)

    # Display the pink flower in the center of the screen
    if pink_flower_displayed:
        screen.blit(pink_flower, pink_flower.get_rect(center=(width / 2, height / 2)))

    pygame.display.update()

pygame.quit()