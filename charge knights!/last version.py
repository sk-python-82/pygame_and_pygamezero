import time
import pygame
import pgzero
import pgzrun
from random import randint
WIDTH = 900
GOAL = 100
HEIGHT = 600
CENTER_X =WIDTH/2 
CENTER_Y = HEIGHT/2
CENTER = (CENTER_Y+100,CENTER_X-100)
CENTERR = (CENTER_Y-180,CENTER_X+130)
CENTERRR = (WIDTH-250,HEIGHT-50)
KNIGHT_START = (200,400)
lives = 10
movement_speed =4
game_over = False
game_complete = False
hero = Actor("hero",pos = KNIGHT_START)
red_knight = Actor("enemy",pos =(WIDTH - 100,randint(0,600)))
red_knight1 = Actor("enemy",pos =(WIDTH - 100,randint(0,600)))
yellow_knight = Actor("enemy2",pos =(WIDTH - 90,randint(0,600)))
green_knight = Actor("enemy3",pos =(WIDTH - 100,randint(0,600)))
def draw():
    global lives,game_complete,game_over
    screen.blit("dungeon",(0,0))
    screen.draw.text("lives:"+str(lives) ,fontsize = 70 ,center = CENTERR ,color = "black")
    screen.draw.text("movement speed:"+str(movement_speed) ,fontsize = 40 ,center = CENTERRR ,color = "black") 
    if game_over == True:
        sounds.loose.play()
        screen.draw.text("GAME OVER!",fontsize = 70,center = CENTER,color = "red")
        lives = 0
    elif lives >= GOAL:
        screen.draw.text("YOU WON!",fontsize = 70,center = CENTER,color = "blue") 
        game_complete = True
        red_knight.x = 910
        red_knight1.x = 910
        green_knight.x = 910
        yellow_knight.x = 910

    else:
        hero.draw()
        red_knight.draw()
        red_knight1.draw()
        yellow_knight.draw()
        green_knight.draw()
def update():
    global game_complete,game_over
    if keyboard.up:
        hero.y -= movement_speed
    if keyboard.down:
        hero.y += movement_speed
    check_hero_collision()
    knights_movement()
def check_hero_collision():
    global lives,movement_speed,game_over,game_complete
    if hero.colliderect(red_knight):
        lives -= 3
    if hero.colliderect(red_knight1):
        lives -= 3

    if hero.colliderect(yellow_knight):
        lives -= 2

    if lives <= 0 or movement_speed <= 0:
        movement_speed = 0
        game_over = True 
        movement_reduction()
        if movement_speed <= 0:
            game_over = True
    if hero.colliderect(green_knight):
        lives += 1
        reset()
        if lives >= GOAL:
            lives = 100        
def movement_reduction():
    global movement_speed
    movement_speed -= 2
    
clock.schedule(movement_reduction,10.0)  
def knights_movement():
    red_knight.x -= 5
    if red_knight.x <= 0:
        red_knight.x = WIDTH
        red_knight.y = randint(0,600)

    red_knight1.x -= 5
    if red_knight1.x <= 0:
        red_knight1.x = WIDTH
        red_knight1.y = randint(0,600)

    yellow_knight.x -= 5
    if yellow_knight.x <= 0:
        yellow_knight.x = WIDTH
        yellow_knight.y = randint(0,600)

    green_knight.x -= 5
    if green_knight.x <= 0:
        green_knight.x = WIDTH 
        green_knight.y = randint(0,600)

# if red_knight.y == green_knight.y or red_knight.y == yellow_knight.y or red_knight.y == green_knight.y or red_knight.y == red_knight1.y:
        # red_knight.y += 50   
    
    if game_over == True:
        red_knight.x = 910
        red_knight1.x = 910
        green_knight.x = 910
        yellow_knight.x = 910
    
def reset():
    global movement_speed
    movement_speed = 4
music.play("game")

pgzrun.go()