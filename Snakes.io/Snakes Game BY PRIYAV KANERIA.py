import math
import time
import turtle
import random
import ctypes

#variables
snake=[]
snake.append(turtle.Turtle())
food=[]
maxfood=5
speed=1.5
index=0
snakindex=1
i=1
angle=0
score=0

#functions
def turnright():
	global angle
	snake[0].right(5)
	angle-=5
    
def turnleft():
	global angle
	snake[0].left(5)
	angle+=5
    
def speedup():
    global speed
    if speed<=15:
    	speed+=1
    else:
    	wn.tracer(1.999)
        
def speeddown():
    global speed
    if speed>=2:
        speed-=1

def foodeaten():
	global index,score
	for fod in food[:]:
		if collision(snake[0],fod):
			fod.hideturtle()
			food.remove(fod)
			index-=1
			score+=1
			return True

def end():
	border.penup()
	border.setposition(0,0)
	border.pendown()
	border.write('Oops!!You Failed',False,align='center',font=('monospace',30,'bold'))
	time.sleep(3)
	wn.bye()

def distance(object,tobecollidedwith):
	global dist
	dist=int(math.sqrt(math.pow(object.xcor()-tobecollidedwith.xcor(),2)+math.pow(object.ycor()-tobecollidedwith.ycor(),2)))

def collision(object,tobecollidedwith):
    distance(object,tobecollidedwith)
    if dist<15:
    	return True

def follow():
	global i,speed
	i=1
	for snak in snake[1:]:
		# snak.speed(2)
		if len(snake)>=2:
			distance(snake[0],snak)
			if dist<=5:
				end()
		distance(snak,snake[i-1])
		if dist>35:
			snak.setheading(snak.towards(snake[i-1]))
			snak.forward(speed-0.5)
		i+=1
	wn.ontimer(follow,10)

#get screen resolution
user32 = ctypes.windll.user32
screensizex = user32.GetSystemMetrics(0)
screensizey = user32.GetSystemMetrics(1)

#get mouse coordinates
from ctypes import windll, Structure, c_long, byref


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
	global x,y
	pt = POINT()
	windll.user32.GetCursorPos(byref(pt))
	x=pt.x
	y=pt.y


#screen set up
wn=turtle.Screen()
wn.bgpic('hexamatrix.gif')
wn.tracer(1.9)

turtle.register_shape('smiley.gif')

border=turtle.Turtle()
border.speed(0)
border.hideturtle()
border.penup()
border.color('white')
border.setposition(-380,-320)
border.pendown()
for somevar in range(4):
	if somevar%2==0:
		border.forward(760)
		border.left(90)
	else:
		border.forward(650)
		border.left(90)

# border coordinates
# 380    -320
# 380    330
# -380    330
# -380    -320

turtle.listen()
# turtle.onkeypress(turnleft, 'Left')
# turtle.onkeypress(turnright, 'Right')
turtle.onkeypress(speedup, 'Up')
turtle.onkeypress(speeddown, 'Down')

snake[0].penup()
snake[0].shape('smiley.gif')
snake[0].color('cyan')

if len(snake)!=1:
	wn.listen()
	follow()

#main game code
while True:
	queryMousePosition()
	xrandno=random.randint(-370,370)
	yrandno=random.randint(-310,320)
	if len(food)<maxfood:
		food.append(turtle.Turtle())
		food[index].speed(0)
		food[index].penup()
		food[index].shape('circle')
		food[index].color('green')
		food[index].setposition(xrandno,yrandno)
		index+=1
	if snake[0].xcor()<380 and snake[0].xcor()>-380 and snake[0].ycor()>-320 and snake[0].ycor()<330:
		snake[0].setheading(snake[0].towards(-(screensizex/2)-28+x,(screensizey/2)+20-y))
		snake[0].forward(speed)
	else:
		end()
	if foodeaten():
		snake.append(turtle.Turtle())
		snake[snakindex].penup()
		snake[snakindex].shape('smiley.gif')
		snake[snakindex].color('cyan')
		snake[snakindex].speed(0)
		snake[snakindex].setposition(snake[snakindex-1].xcor()-(20*math.cos(angle/math.pi)),snake[snakindex-1].ycor()-(20*math.sin(angle/math.pi)))
		follow()
		border.undo()
		border.penup()
		border.setposition(-290,302)
		scorestr='Score: %s'%score
		border.write(scorestr, False, align='Left', font=('Arial',14, 'normal'))
		snakindex+=1
	if len(snake)>2:
		wn.ontimer(speedup,3500)

delay=input('press enter to exit')