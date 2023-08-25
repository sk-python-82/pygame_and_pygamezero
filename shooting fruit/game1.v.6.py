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
game_over = False
pineapple.x = randint(100,750)
pineapple.y = randint(300,450)
orange.x = randint(100,750)
orange.y = randint(300,450)
apple.x = randint(100,750)
apple.y = randint(300,450)

def draw(): 
    global q
    flag = 0
    screen.clear()
    screen.draw.text("game name : naughty fruits!",(350,50),fontsize = 30 ,color = "orange") 
    if flag == 0 :
        random.shuffle(questions)
        q = questions.pop(0)
        questions.append(q)
        flag += 1
    if flag % 2 == 0 :
        random.shuffle(questions) 
        q = questions.pop(0)
        questions.append(q)
        flag += 1
    else :
        random.shuffle(questions)
        q = questions.pop(0)
        questions.append(q)
        flag += 1        
    screen.draw.text(q,(10,200),fontsize = 70,color = "white")
    screen.draw.text(str(score),(600,100),color = "green")
    apple.draw()
    orange.draw()
    pineapple.draw()
    if game_over == True:
         screen.clear()
         screen.draw.text("you lost!!!",(250,250),fontsize=70,color = "red")
 

def place_pineapple():
    pineapple.x = randint(100,750)
    pineapple.y = randint(300,450)

    

def place_apple():
    apple.x = randint(100,750)
    apple.y = randint(300,450)
    
def place_orange():
    orange.x = randint(100,750)
    orange.y = randint(300,450)


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