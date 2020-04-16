import turtle
import time
import random
import os
import math

coorx=None
coory=None
prcoorx=coorx
prcoory=coory


#functions
def mouse(x,y):
	global coorx,coory,prcoory,prcoorx
	prcoorx=coorx
	prcoory=coory
	coorx=x
	coory=y

def spacebar():
	global space
	space+=1

def finalmakewall():
	global space,coory,coory,prcoory,prcoorx
	if coorx!=prcoorx and coory!=prcoory:
		if space%2==1:
			verticlewall()
		elif space%2==0:
			horizontalwall()

def verticlewall():
	global coorx,coory,prcoory,prcoorx
	if coorx in range(-100,101) and coory in range(-100,101):
		if coorx!=prcoorx and coory!=prcoory:
			wall.penup()
			wall.setposition(coorx,coory)
			wall.pendown()
			wall.color('white')
			wall.left(90)
			wall.forward(abs(100-coory))
			wall.setposition(coorx,coory)
			wall.left(180)
			wall.forward(abs(100+coory))
			wall.penup()
			wall.setposition(0,0)
			wall.left(90)
			prcoorx=coorx
			prcoory=coory

def horizontalwall():
	global coorx,coory,prcoory,prcoorx
	if coorx in range(-100,101) and coory in range(-100,101):
		if coorx!=prcoorx and coory!=prcoory:
			wall.penup()
			wall.setposition(coorx,coory)
			wall.pendown()
			wall.color('white')
			wall.left(180)
			wall.forward(abs(100+coorx))
			wall.setposition(coorx,coory)
			wall.left(180)
			wall.forward(abs(100-coorx))
			wall.penup()
			wall.setposition(0,0)
			prcoorx=coorx
			prcoory=coory

def end():
    wn=turtle.Screen()
    wn.bgcolor('black')
    wn.title('You won')
    eg=turtle.Turtle()
    eg.hideturtle()
    eg.penup()
    eg.color('White')
    eg.setposition(0,-150)
    eg.write('You win!!', False, align='Center', font=('Monospace',30, 'normal'))
    time.sleep(3)
    turtle.bye()

#screen setup
wn=turtle.Screen()
turtle.screensize(1000,1000,'black')
wn.title('Mind Boggler By- Priyav')
wn.tracer(3)

#border setup
border=turtle.Turtle()
border.hideturtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-100,-100)
border.pendown()
for i in range(4):
    border.forward(200)
    border.left(90)
border.penup()
border.setposition(0,200)
border.write('Let\'s play', False, align='Center', font=('Monospace',30, 'normal'))
border.penup()
border.setposition(40,140)
border.pendown()
border.write('Take the ball to center\nPress space to change direction\nMouse click to make wall', False, align='Center', font=('Monospace',13, 'normal'))
border.penup()

#angle
angle=random.randint(10,45)

#ball
ball=turtle.Turtle()
ball.penup()
ball.color('white')
ball.shape('circle')
ball.left(angle)
ball.speed(0)
finalspeed=0
turtle.listen()
turtle.onscreenclick(mouse)
turtle.onkey(spacebar, 'space')
timed=1


#box collider for ball
boxmaxx=88
boxminx=-88
boxmaxy=88
boxminy=-88

#wallmake
wall=turtle.Turtle()
wall.hideturtle()
times=1
space=1


#speed
speed=0.025

starttime=time.time()

while True:
	ball.forward(speed)
	presenttime=time.time()
	if ball.xcor() > boxmaxx or ball.xcor() < boxminx:
		if angle > (angle/2):
			angle=90-angle
			ball.left(2*angle)
		else:
			angle=90-angle
			ball.right(2*angle)
	if ball.ycor() > boxmaxy or ball.ycor() < boxminy:
		if angle > (angle/2):
			angle=90-angle
			ball.left(2*angle)
		else:
			angle=90-angle
			ball.right(2*angle)
	if coorx!=prcoorx and coory!=prcoory:
		if space%2==1:
			if coorx<boxmaxx and coorx>0:
				boxmaxx=coorx-12
			if coorx>boxminx and coorx<0:
				boxminx=coorx+12
		if space%2==0:
			if coory<boxmaxy and coory>0:
				boxmaxy=coory-12
			if coory>boxminy and coory<0:
				boxminy=coory+12	
	if presenttime-starttime>=3:
		while ball.xcor()>-20 and ball.xcor()<20 and ball.ycor()>-20 and ball.ycor()<20:
			timed+=1
			ball.forward(speed)
			if ball.xcor() > boxmaxx or ball.xcor() < boxminx:
				if angle > (angle/2):
					angle=90-angle
					ball.left(2*angle)
				else:
					angle=90-angle
					ball.right(2*angle)
			if ball.ycor() > boxmaxy or ball.ycor() < boxminy:
				if angle > (angle/2):
					angle=90-angle
					ball.left(2*angle)
				else:
					angle=90-angle
					ball.right(2*angle)
			if coorx!=prcoorx and coory!=prcoory:
				if space%2==1:
					if coorx<boxmaxx and coorx>0:
						boxmaxx=coorx-12
					if coorx>boxminx and coorx<0:
						boxminx=coorx+12
				if space%2==0:
					if coory<boxmaxy and coory>0:
						boxmaxy=coory-12
					if coory>boxminy and coory<0:
						boxminy=coory+12	
			if timed>5000:
				end()
				break
	timed=0
	finalmakewall()


delay=input('Press enter to exit ')