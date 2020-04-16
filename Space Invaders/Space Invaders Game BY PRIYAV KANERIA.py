import turtle
import math
import random
import time


#variables
fired=False
bullet=[]
enemy=[]
index=-1
maxenemy=7
enemyindex=0
count=1

#get screen resolution
import ctypes
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


#get mouse coordinates on click()
def mouseclick(x,y):
	global clickx,clicky
	clickx=x
	clicky=y
	fire()

def fire():
	global fired,bullet,index
	index+=1
	bullet.append(turtle.Turtle())
	bullet[index].speed(0)
	bullet[index].penup()
	bullet[index].shape('laser.gif')
	bullet[index].color('red')
	bullet[index].left(90)
	bullet[index].setposition(fighter.xcor(),fighter.ycor()+80)
	fired=True

def collision(object,tobecollidedwith):
	dist=math.sqrt(math.pow(object.xcor()-tobecollidedwith.xcor(),2)+math.pow(object.ycor()-tobecollidedwith.ycor()+70,2))
	if dist<35:
		return True

def end():
	border.penup()
	border.setposition(0,0)
	border.pendown()
	border.write('Oops!!You Failed',False,align='center',font=('monospace',30,'bold'))
	time.sleep(4)
	wn.bye()

def win():
	border.penup()
	border.setposition(0,0)
	border.pendown()
	border.color('green')
	border.write('Congratulations!!You Have WON ',False,align='center',font=('monospace',30,'bold'))
	time.sleep(4)
	wn.bye()

turtle.onscreenclick(mouseclick)

#set up screen
wn=turtle.Screen()
wn.bgcolor('white')
wn.tracer(1.5)

turtle.register_shape('player.gif')
turtle.register_shape('invader.gif')
turtle.register_shape('laser.gif')

border=turtle.Turtle()
border.speed(0)
border.hideturtle()
border.penup()
border.color('red')
border.setposition(-380,-320)
border.pendown()
for somevar in range(4):
	if somevar%2==0:
		border.forward(760)
		border.left(90)
	else:
		border.forward(650)
		border.left(90)
border.left(90)
border.forward(120)
border.right(90)
border.forward(760)

fighter=turtle.Turtle()
fighter.color('red')
fighter.shape('player.gif')
fighter.penup()
fighter.left(90)
fighter.speed(0)
fighter.setposition(0,-290)
starttime=time.time()

#main game code
while count>0:
	if enemyindex<=maxenemy:
		enemy.append(turtle.Turtle())
		enemy[enemyindex].penup()
		enemy[enemyindex].speed(0)
		enemy[enemyindex].shape('invader.gif')
		enemy[enemyindex].setposition(-320+(enemyindex*70),200)
		enemyindex+=1
	else:
		queryMousePosition()
		# fighter.setposition(-777+x,460-y)
		newx=x-(screensizex/2)
		if newx<380 and newx>-380:
			fighter.setposition(newx,-290)
		enemlist=enemy
		bulllist=bullet
		if fired==True:
			for enem in enemlist:
				for bull in bulllist:
					if collision(bull,enem):
						bull.hideturtle()
						bullet.remove(bull)
						enem.hideturtle()
						enemy.remove(enem)
						index-=1
					else:
						if bull.ycor()<300:
							bull.forward(8)
							if count%40==0:
								for enem in enemy:
									enem.forward(30)
									if enemy[-1].xcor()>320:
										for enem in enemy:
											enem.right(90)
											enem.forward(40)
											enem.right(90)
											enem.forward(30)
									if enemy[0].xcor()<-320:
										for enem in enemy:
											enem.left(90)
											enem.forward(40)
											enem.left(90)
											enem.forward(30)
										if len(enemy)!=1:
											enemy[0].setposition(enemy[1].xcor()-40,enemy[1].ycor())
							count+=1
						else:
							bull.hideturtle()
							bullet.remove(bull)
							index-=1
		
		if count%40==0:
			for enem in enemy:
				if enem.ycor()<-180:
					end()
				enem.forward(30)
				if enemy[-1].xcor()>320:
					for enem in enemy:
						enem.right(90)
						enem.forward(40)
						enem.right(90)
						enem.forward(30)
				if enemy[0].xcor()<-320:
					for enem in enemy:
						enem.left(90)
						enem.forward(40)
						enem.left(90)
						enem.forward(30)
					if len(enemy)!=1:
						enemy[0].setposition(enemy[1].xcor()-40,enemy[1].ycor())
		count+=1
	if len(enemy)==0:
		win()
		

delay=input('nothing')
