import pgzrun
import random
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'
from random import randint
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
score = 0
QUESTION_1 ="shoot the appple!" 
QUESTION_2 = "shoot the orange!"
QUESTION_3 ="shoot the pineapple!"
questions = [QUESTION_1,QUESTION_2,QUESTION_3]
for i in range(0,100):
        random.shuffle(questions)
        q = questions.pop(0)
        questions.append(q)
game_over = False
pineapple.x = randint(50,750)
pineapple.y = randint(50,450)
orange.x = randint(50,750)
orange.y = randint(50,450)
apple.x = randint(50,750)
apple.y = randint(50,450)

def draw(): 
    screen.clear()
    screen.draw.text("game name : naughty fruits!",(350,50),color = "blue")         
    screen.draw.text(q,(100,200),color = "white")
    screen.draw.text(str(score),(600,100),color = "green")
    if game_over == True:
        screen.clear()
        screen.draw.text("you lost!!!",(250,50),color = "blue")
    apple.draw()
    orange.draw()
    pineapple.draw() 

def place_pineapple():
    pineapple.x = randint(300,750)
    pineapple.y = randint(50,450)

    

def place_apple():
    apple.x = randint(300,750)
    apple.y = randint(50,450)
    
def place_orange():
    orange.x = randint(300,750)
    orange.y = randint(50,450)


def on_mouse_down(pos):
    global score,q
    if q == QUESTION_1: 
        if apple.collidepoint(pos):
            place_apple()
            place_orange()
            place_pineapple()
            score+=1
        if pineapple.collidepoint(pos):
            score -= 10
            place_apple()
            place_orange()
            place_pineapple()
        if orange.collidepoint(pos):
            score -= 5
            place_apple()
            place_orange()
            place_pineapple()
    if q == QUESTION_2 :
        if orange.collidepoint(pos):
            place_orange()
            place_pineapple()
            place_apple()
            score+=5
        if apple.collidepoint(pos):
            place_apple()
            place_orange()
            place_pineapple()
            score-=1
        if pineapple.collidepoint(pos):           
            place_orange()
            place_apple()
            place_pineapple()
            score-=10
    if q == QUESTION_3:
        if pineapple.collidepoint(pos):
            place_pineapple()
            place_apple()
            place_orange()
            score += 10
        if apple.collidepoint(pos):
            place_pineapple()
            place_apple()
            place_orange()
            score -= 1
        if orange.collidepoint(pos):
            place_pineapple()
            place_apple()
            place_orange()
            score -= 5
    if score <= 0:
        global game_over
        game_over = True
pgzrun.go()
