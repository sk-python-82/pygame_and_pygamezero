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

font = pygame.font.Font(None, 36)  # Create a font object

flowers_collected = 0  # Initialize the count of collected flowers
pink_flower_displayed = False  # To track if the pink flower has been displayed

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Get a list of keys that are currently pressed

    if keys[K_RIGHT] and girl_rect.right < width:
        # Check for collision with the pink flower
        girl_rect_right = girl_rect.move(10, 0)
        pink_flower_rect = pink_flower.get_rect(center=(width / 2, height / 2))
        pink_flower_buffer = pink_flower_rect.inflate(40, 40)  # Add a buffer zone around the pink flower
        if not pink_flower_displayed or not (girl_rect_right.colliderect(pink_flower_buffer) and pink_flower_buffer.colliderect(pink_flower_rect)):
            girl_rect = girl_rect_right
    if keys[K_LEFT] and girl_rect.left > 0:
        # Check for collision with the pink flower
        girl_rect_left = girl_rect.move(-10, 0)
        pink_flower_rect = pink_flower.get_rect(center=(width / 2, height / 2))
        pink_flower_buffer = pink_flower_rect.inflate(40, 40)  # Add a buffer zone around the pink flower
        if not pink_flower_displayed or not (girl_rect_left.colliderect(pink_flower_buffer) and pink_flower_buffer.colliderect(pink_flower_rect)):
            girl_rect = girl_rect_left
    if keys[K_UP] and girl_rect.top > 0:
        # Check for collision with the pink flower
        girl_rect_up = girl_rect.move(0, -10)
        pink_flower_rect = pink_flower.get_rect(center=(width / 2, height / 2))
        pink_flower_buffer = pink_flower_rect.inflate(40, 40)  # Add a buffer zone around the pink flower
        if not pink_flower_displayed or not (girl_rect_up.colliderect(pink_flower_buffer) and pink_flower_buffer.colliderect(pink_flower_rect)):
            girl_rect = girl_rect_up
    if keys[K_DOWN] and girl_rect.bottom < height:
        # Check for collision with the pink flower
        girl_rect_down = girl_rect.move(0, 10)
        pink_flower_rect = pink_flower.get_rect(center=(width / 2, height / 2))
        pink_flower_buffer = pink_flower_rect.inflate(40, 40)  # Add a buffer zone around the pink flower
        if not pink_flower_displayed or not (girl_rect_down.colliderect(pink_flower_buffer) and pink_flower_buffer.colliderect(pink_flower_rect)):
            girl_rect = girl_rect_down

    # Check for collisions between the girl and flowers
    for flower in flowers[:]:  # Use a copy of the list to avoid modifying it while iterating
        if girl_rect.colliderect(flower):
            flowers.remove(flower)
            flowers_collected += 1

    # Display the pink flower when 10 flowers are collected
    if flowers_collected >= 10 and not pink_flower_displayed:
        pink_flower_displayed = True

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Display each remaining flower
    for flower in flowers:
        screen.blit(flower1, flower)

    screen.blit(girl, girl_rect)

    # Display the "flowers collected" text
    text = font.render(f"Flowers collected: {flowers_collected}", True, (0, 0, 0))
    screen.blit(text, (10, 10))  # Position the text in the top-left corner

    # Display the pink flower in the center of the screen
    if pink_flower_displayed:
        screen.blit(pink_flower, pink_flower.get_rect(center=(width / 2, height / 2)))

    pygame.display.update()

pygame.quit()