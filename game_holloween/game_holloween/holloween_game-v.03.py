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

girl_rect = girl.get_rect(center=(x, y))

# Create a list of Rect objects for the flowers with random positions
flowers = [flower1.get_rect(topleft=(random.randint(0, width - 50), random.randint(0, height - 50))) for _ in range(10)]

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Get a list of keys that are currently pressed

    if keys[K_RIGHT]:
        girl_rect = girl_rect.move(10, 0)
    if keys[K_LEFT]:
        girl_rect = girl_rect.move(-10, 0)
    if keys[K_UP]:
        girl_rect = girl_rect.move(0, -10)
    if keys[K_DOWN]:
        girl_rect = girl_rect.move(0, 10)

    # Check for collisions between the girl and flowers
    for flower in flowers[:]:  # Use a copy of the list to avoid modifying it while iterating
        if girl_rect.colliderect(flower):
            flowers.remove(flower)

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Display each remaining flower
    for flower in flowers:
        screen.blit(flower1, flower)

    screen.blit(girl, girl_rect)

    pygame.display.update()

pygame.quit()