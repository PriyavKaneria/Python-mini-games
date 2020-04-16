import turtle
import random
import math
import time

#Set up screen
wn=turtle.Screen()
wn.bgcolor('black')
wn.title('Priyav\'s game')
wn.tracer(1)
wn.bgpic('space.gif')

#player and food img
turtle.register_shape("player.gif")
turtle.register_shape('player.gif')

#border
border=turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-300,-300)
border.pendown()
for i in range(4):
    border.forward(600)
    border.left(90)

maxfood=6
endgam=False

#score
score=0

#movement
speed=1
foodspeed=3

#food
foods=[]
for f in range(maxfood):
    foods.append(turtle.Turtle())
    foods[f].color('green')
    foods[f].penup()
    foods[f].shape('circle')
    foods[f].speed(0)
    foods[f].setposition(random.randint(-292,292),random.randint(-292,292))
    foods[f].left(random.randint(0,360))


#player
player=turtle.Turtle()
player.penup()
player.color('white')
player.shape('triangle')
player.speed(0)


#functions
def turnright():
    player.right(15)
    
def turnleft():
    player.left(15)
    
def speedup():
    global speed
    if speed<=5:
        speed+=1
        
def speeddown():
    global speed
    if speed>=2:
        speed-=1

def collision(t1,t2):
    d=math.sqrt(math.pow((t1.xcor())-(t2.xcor()),2)+math.pow((t1.ycor())-(t2.ycor()),2))
    if d<=20:
        return(True)
    else:
        return(False)

def endgame():
    wn=turtle.Screen()
    wn.bgcolor('black')
    wn.title('You won')
    eg=turtle.Turtle()
    eg.hideturtle()
    eg.penup()
    eg.color('White')
    eg.setposition(0,0)
    eg.write('You win!!', False, align='Center', font=('Monospace',30, 'normal'))
    time.sleep(3)
    turtle.bye()
    
#keyboard control
turtle.listen()
turtle.onkeypress(turnleft, 'Left')
turtle.onkeypress(turnright, 'Right')
turtle.onkeypress(speedup, 'Up')
turtle.onkeypress(speeddown, 'Down')

while endgam==False:
    for f in range(maxfood):
        player.forward(speed)
        foods[f].forward(foodspeed)
        if player.xcor() > 300 or player.xcor() < -300:
            player.left(180)
        if player.ycor() > 300 or player.ycor() < -300:
            player.left(180)
        if foods[f].xcor() > 292 or foods[f].xcor() < -292:
            foods[f].left(180)
        if foods[f].ycor() > 292 or foods[f].ycor() < -292:
            foods[f].left(180)
        if collision(foods[f],player):
            foods[f].setposition(random.randint(-292,292),random.randint(-292,292))
            foods[f].left(random.randint(0,360))
            score+=1
            border.undo()
            border.penup()
            border.setposition(-290,300)
            scorestr='Score: %s'%score
            border.write(scorestr, False, align='Left', font=('Arial',14, 'normal'))
##        for c in range(0,maxfood):
##            if collision(foods[f],foods[c]):
##                foods[f].left(90)
##                foods[c].left(90)
    if score>=5:
        endgame()
        endgam=True
        break

delay=input('Press enter to exit')
        
