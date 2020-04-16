import turtle
import time
import math
import random

#variables
startgame=False
space=0
index=0
index2=0
index3=0
index4=0
index5=0
objindex=0
probjindex=0
once=False
speed=5
upclicked=False
downclicked=False
rightclicked=False
leftclicked=False
replay=True
score=0

#screen set up
wn=turtle.Screen()
wn.bgcolor('black')
wn.title('Priyav\'s game - Piano Tiles')
wn.tracer(1.9)

turtle.register_shape('arrowright.gif')
turtle.register_shape('arrowleft.gif')
turtle.register_shape('arrowup.gif')
turtle.register_shape('arrowdown.gif')

#functions
def start():
	global startgame,space
	startgame=True
	space+=1
	replay=False

def speedup():
	global speed
	speed+=0.5
	wn.ontimer(speedup,10500)

def end():
	global startgame,replay
	border.setposition(-10,0)
	border.write('Oops!!You Failed',False,align='center',font=('monospace',30,'bold'))
	time.sleep(3)
	wn.bye()

def clicked(object):
	global rightclicked,leftclicked,upclicked,downclicked,score
	if object in rightT:
		if rightclicked==True:
			rightclicked=False
			upclicked=False
			downclicked=False
			leftclicked=False
			score+=1
		else:
			end()
	elif object in leftT:
		if leftclicked==True:
			rightclicked=False
			upclicked=False
			downclicked=False
			leftclicked=False
			score+=1
		else:
			end()
	elif object in upT:
		if upclicked==True:
			rightclicked=False
			upclicked=False
			downclicked=False
			leftclicked=False
			score+=1
		else:
			end()
	elif object in downT:
		if downclicked==True:
			rightclicked=False
			upclicked=False
			downclicked=False
			leftclicked=False
			score+=1
		else:
			end()
	border.undo()
	border.penup()
	border.setposition(-290,302)
	scorestr='Score: %s'%score
	border.write(scorestr, False, align='Left', font=('Arial',14, 'normal'))

def right():
	global rightclicked,leftclicked,upclicked,downclicked
	rightclicked=True
	leftclicked=False
	upclicked=False
	downclicked=False

def left():
	global rightclicked,leftclicked,upclicked,downclicked
	leftclicked=True
	rightclicked=False
	upclicked=False
	downclicked=False

def up():
	global rightclicked,leftclicked,upclicked,downclicked
	upclicked=True
	downclicked=False
	rightclicked=False
	leftclicked=False

def down():
	global rightclicked,leftclicked,upclicked,downclicked
	downclicked=True
	upclicked=False
	rightclicked=False
	leftclicked=False

def reached(object,ycor):
	if ycor<-290:
		obj.remove(object)
		object.hideturtle()
		clicked(object)

def makeobj():
	global index,index2,index3,index4,index5,objindex
	tiles.append(random.randint(0,3))
	if tiles[index]==0:
		rightT.append(turtle.Turtle())
		rightT[index2].speed(0)
		rightT[index2].hideturtle()
		rightT[index2].color('white')
		rightT[index2].shape('arrowright.gif')
		rightT[index2].penup()
		rightT[index2].setposition(0,310)
		rightT[index2].showturtle()
		rightT[index2].right(90)
		obj.append(rightT[index2])
		index2+=1
	elif tiles[index]==1:
		leftT.append(turtle.Turtle())
		leftT[index3].speed(0)
		leftT[index3].hideturtle()
		leftT[index3].color('white')
		leftT[index3].shape('arrowleft.gif')
		leftT[index3].penup()
		leftT[index3].setposition(0,310)
		leftT[index3].showturtle()
		leftT[index3].right(90)
		obj.append(leftT[index3])
		index3+=1
	elif tiles[index]==2:
		upT.append(turtle.Turtle())
		upT[index4].speed(0)
		upT[index4].hideturtle()
		upT[index4].color('white')
		upT[index4].shape('arrowup.gif')
		upT[index4].penup()
		upT[index4].setposition(0,310)
		upT[index4].showturtle()
		upT[index4].right(90)
		obj.append(upT[index4])
		index4+=1
	elif tiles[index]==3:
		downT.append(turtle.Turtle())
		downT[index5].speed(0)
		downT[index5].hideturtle()
		downT[index5].color('white')
		downT[index5].shape('arrowdown.gif')
		downT[index5].penup()
		downT[index5].setposition(0,310)
		downT[index5].showturtle()
		downT[index5].right(90)
		obj.append(downT[index5])
		index5+=1

def replayfunc():
	global replay
	replay=True

#screen extras
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

border.penup()
border.setposition(-10,0)
border.write('Let\'s play the game',False,align='center',font=('monospace',30,'bold'))
border.setposition(-15,-50)
border.write('Press space twice to start',False,align='center',font=('monospace',30,'bold'))

#keyboard instructions
turtletp=turtle.Turtle()
turtletp.hideturtle()
turtle.listen()
turtle.onkey(start,'space')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')
turtle.onkey(up,'Up')
turtle.onkey(down,'Down')

#maingame code
tiles=[]
obj=[]


#maingame turtles

#right
rightT=[]

#left
leftT=[]

#up
upT=[]

#down
downT=[]

starttime=time.time()
while True:
	if space==2:
		timenow=time.time()
		if int(timenow-starttime)==1 :
			once=True
		if int(timenow-starttime)==3:
			once=False
	if startgame==True and space<=1:
		border.undo()
		border.undo()
		border.undo()
		startgame=False
	if startgame==True and space>=2:
		if len(obj)<=1:
			makeobj()
			index+=1
		if len(obj)>=2:
			objindex=probjindex+1
		if objindex!=probjindex:
			if abs(obj[probjindex].ycor()-obj[objindex].ycor())>=10:
				makeobj()
				index+=1
			for x in range(int(50/speed)):
				for i in obj:
					i.forward(speed)
					reached(i,i.ycor())
		if len(obj)==2:
			obj[1].setposition(0,obj[0].ycor()-50)
		speedup()
	else:
		turtletp.forward(0.0001)

delay=input('press enter to quit')
