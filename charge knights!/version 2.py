import time
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
movement_speed =20
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
    global game_complete
    if keyboard.up:
        hero.y -= movement_speed
    if keyboard.down:
        hero.y += movement_speed
    check_hero_collision()
    knights_movement()

pgzrun.go()