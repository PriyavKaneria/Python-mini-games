import winsound
import turtle

wn=turtle.Screen()
wn.bgcolor('black')
wn.title('Priyav\'s piano')




#functions
def a():
    freq=261
    winsound.Beep(freq,100)

def b():
    freq=294
    winsound.Beep(freq,100)

def c():
    freq=330
    winsound.Beep(freq,100)

def d():
    freq=349
    winsound.Beep(freq,100)

def e():
    freq=392
    winsound.Beep(freq,100)

def f():
    freq=440
    winsound.Beep(freq,100)

def g():
    freq=494
    winsound.Beep(freq,100)

def h():
    freq=515
    winsound.Beep(freq,100)


turtle2=turtle.Turtle()
turtle.listen()
turtle.onkeypress(a,'a')
turtle.onkeypress(b,'s')
turtle.onkeypress(c,'d')
turtle.onkeypress(d,'f')
turtle.onkeypress(e,'g')
turtle.onkeypress(f,'h')
turtle.onkeypress(g,'j')
turtle.onkeypress(h,'k')

while True:
    turtle2.forward(0.0002)

delay=input('press enter')
