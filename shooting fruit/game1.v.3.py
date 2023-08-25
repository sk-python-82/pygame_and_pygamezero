import pgzrun
from random import randint
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

pineapple.x = randint(50,750)
pineapple.y = randint(50,450)
orange.x = randint(50,750)
orange.y = randint(50,450)
apple.x = randint(50,750)
apple.y = randint(50,450)

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()
    
def place_pineapple():
    pineapple.x = randint(50,750)
    pineapple.y = randint(50,450)

def place_apple():
    apple.x = randint(50,750)
    apple.y = randint(50,450)
    
def place_orange():
    orange.x = randint(50,750)
    orange.y = randint(50,450)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("good shoot on apple!!!!")
        place_apple()
    elif orange.collidepoint(pos):
        print("good shoot on orange!!!!")
        place_orange()
    elif pineapple.collidepoint(pos):
        print("good shoot on pineapple!!!!")
        place_pineapple()

    else:
        print("you missed !!!!....")
        quit()
    
pgzrun.go()
