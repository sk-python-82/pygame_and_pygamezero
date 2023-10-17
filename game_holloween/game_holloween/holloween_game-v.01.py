import pygame
from pygame.locals import *
from pygame import mixer
import sys
mixer.init()
pygame.init()
running = True
scare = False
screen = pygame.display.set_mode((800, 567))
pygame.display.update()

width = 800
height = 567

x = width/2 
y = height/2 

# Load the song
mixer.music.load("C:/Users/Asus/Desktop/game_holloween/songs/song.mp3")

# Set the volume (adjust as needed, a value between 0 and 1)
mixer.music.set_volume(0.5)

# Play the song in an infinite loop
mixer.music.play(-1)

# Load the image
image_path = "C:/Users/Asus/Desktop/game_holloween/images/garden.png"
bg = pygame.image.load(image_path)

image_path2 = "C:/Users/Asus/Desktop/game_holloween/images/girl.png"
girl = pygame.image.load(image_path2)

image_path3 = "C:/Users/Asus/Desktop/game_holloween/images/purple_flower.png"
flower1 = pygame.image.load(image_path3)

flower1_loc = flower1.get_rect()
flower1_loc.center = x + 300,y + 200
girl_loc = girl.get_rect()
girl_loc.center = x , y
while running:
    for event in pygame.event.get():


        if event.type == QUIT:
            running = False

        # checking if keydown event happened or not
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                girl_loc = girl_loc.move(10,0)
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                girl_loc = girl_loc.move(-10,0)
        if event.type == KEYDOWN:
            if event.key == K_UP:
                girl_loc = girl_loc.move(0,-10)
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                girl_loc = girl_loc.move(0,10)

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with a black background color

    # Blit (draw) the image on the screen
    screen.blit(bg, (0, 0))

    screen.blit(girl,girl_loc)

    screen.blit(flower1,flower1_loc)

    

    # Update the display to show the image
    pygame.display.update()

pygame.quit()