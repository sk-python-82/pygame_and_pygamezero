import pygame
from pygame.locals import *
import random
import time

pygame.init()
running = True

width, height = 800, 567
x, y = width / 2, height / 2

screen = pygame.display.set_mode((width, height))
pygame.display.update()

# Load the song
pygame.mixer.music.load("C:/Users/Asus/Desktop/game_holloween/songs/song.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# Load the scream sound
scream_sound = pygame.mixer.Sound("C:/Users/Asus/Desktop/game_holloween/sounds2/scream.wav")

# Load the images
bg = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/garden.png")
girl = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/girl.png")
flower1 = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/purple_flower.png")
pink_flower = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/pink_flower.png")
scary_image = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/scary.png")
blood_image = pygame.image.load("C:/Users/Asus/Desktop/game_holloween/images/blood.png")

girl_rect = girl.get_rect(center=(x, y))
blood_displayed = False

# Create a list of Rect objects for the flowers with random positions (including the pink flower)
flowers = [flower1.get_rect(topleft=(random.randint(0, width - 50), random.randint(0, height - 50))) for _ in range(10)]

font = pygame.font.Font(None, 36)  # Create a font object for flower counter
timer_font = pygame.font.Font(None, 36)  # Create a font object for the timer

flowers_collected = 0  # Initialize the count of collected flowers

# Countdown timer variables
countdown_timer = 20  # Initial value of the timer
timer_location = (width - 150, 10)  # Top right corner for timer display
timer_color = (0, 0, 0)  # Timer text color
countdown_delay = 1000  # Countdown delay in milliseconds
last_countdown_time = pygame.time.get_ticks()

# Control girl movement
movement_delay = 200  # Adjust this value for smoother movement
girl_movable = True

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if girl_movable:
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

    # Update the countdown timer
    if current_time - last_countdown_time >= countdown_delay and countdown_timer > 0:
        countdown_timer -= 1
        last_countdown_time = current_time

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # Display "HAPPY HALLOWEEN" text at the top of the screen
    halloween_text = font.render("HAPPY HALLOWEEN", True, (255, 165, 0))  # Orange color
    text_rect = halloween_text.get_rect(center=(width / 2, 20))
    screen.blit(halloween_text, text_rect)

    # Display each remaining flower
    for flower in flowers:
        screen.blit(flower1, flower)

    if blood_displayed:
        screen.blit(blood_image, blood_image.get_rect(center=(width / 2, height / 2)))

    if flowers_collected >= 10 or countdown_timer == 0:
        girl_movable = False
        pygame.mixer.music.stop()
        scream_sound.play()
        screen.blit(blood_image, blood_image.get_rect(center=(width / 2, height / 2)))
        screen.blit(scary_image, scary_image.get_rect(center=(width / 2, height / 2)))

    else:
        screen.blit(girl, girl_rect)

    # Display the "flowers collected" text
    flower_text = font.render(f"Flowers collected: {flowers_collected}", True, (0, 0, 0))
    screen.blit(flower_text, (10, 10))  # Position the flower counter in the top-left corner

    # Display the countdown timer in the top right corner
    timer_text = timer_font.render(f"Timer: {countdown_timer}", True, timer_color)
    screen.blit(timer_text, timer_location)

    pygame.display.update()

pygame.quit()