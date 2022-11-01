from turtle import *
from random import randint
import colorsys

def square_spiral():                                                                #function to draw a spiral using squares
    speed(400)
    bgcolor("black")
    x=1
    while(x< 1000):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        colormode(255)
        pencolor(r,g,b)
        fd(50+x)
        rt(90.911)
        x+=1
    exitonclick()


def tur_tree():                                                                     #main function to design a tree
    tu.screen.bgcolor("black")
    tu.pensize(2)
    tu.color("green")
    tu.left(90)
    tu.backward(100)
    tu.speed(2000)
    tu.shape('turtle')
    tree(100)
    done()

def tree(i):
    if i<10:
        return
    else:
        tu.forward(i)
        tu.color('pink')
        tu.circle(2)
        tu.color("brown")
        tu.left(30)
        tree(3*i/4)
        tu.right(60)
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)


def cir_des():                                                                      #main function for the circular design
    bgcolor("black")
    speed(100)
    pensize(2)
    pencolor("blue")
    draw_des()
    done()
def drawcircle(rad):
    for i in range(10):
        circle(rad)
        rad-=4
def draw_des():
    for i in range(10):
        drawcircle(150)
        right(36)


def dan_des():
    bgcolor('black')
    speed(0)
    pensize(2)

    hue=0.0
    for i in range(300):
        color=colorsys.hsv_to_rgb(hue,1,1)
        pencolor(color)
        hue+=0.005
        right(i)
        circle(50,i)
        forward(i)
        left(91)
    done()


def sun_flw():                                                                    #function to draw a flower
    setup(800,800)
    speed(0)
    tracer(10)
    width(2)
    bgcolor('black')

    for j in range(25):
        hue=0.0
        for i in range(15):
            color(colorsys.hsv_to_rgb(hue,1,1))
            hue+=0.005
            right(90)
            circle(200-j*4,90)
            left(90)
            circle(200-j*4,90)
            right(180)
            circle(50,24)

    done()


def star():                                                                         #function to draw a star
    colors=['yellow','green','red','white','cyan','blue']
    s.bgcolor('black')
    tu.speed(30)
    for i in range(100):
        tu.color(colors[i%6])
        tu.fd(i*5)
        tu.left(200)
        tu.width(2)
    done()


def ninja():

    tu.getscreen().bgcolor('black')

    tu.penup()
    tu.goto(-200,100)
    tu.pendown()
    tu.color('yellow')

    tu.speed(25)
    nst(369)
    done
def nst(size):
    if size<=10:
        return
    else:
        tu.begin_fill()
        for i in range(5):
            tu.forward(size)
            nst(size/3)
            tu.left(216)
            tu.end_fill()

def hexa():
    colors=['red','purple','blue','green','yellow','orange']
    bgcolor('black')
    for i in range(369):
        pencolor(colors[i%6])
        width(i/100)
        forward(i)
        left(59)
        speed(100)

def clock():

    tu.speed(0)
    tu.ht()
    for i in range(25):
        gra()
        tu.goto(0,0)
        tu.lt(-15)
def gra():
    for i in range(2):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        colormode(255)
        tu.fillcolor(r,g,b)
        tu.begin_fill()
        tu.fd(100)
        tu.lt(45)
        tu.fd(100)
        tu.lt(135)
        tu.end_fill()

def corona():

    s.bgcolor('black')
    tu.pencolor('green')
    a=0
    b=0
    tu.speed(0)
    tu.penup()
    tu.goto(0,200)
    tu.pendown()
    while(True):
        tu.forward(a)
        tu.right(b)
        a+=3
        b+=1
        if b==210:
            break
        tu.hideturtle()
    done()

#main
tu=Turtle()
s=Screen()
print('---MENU---')
print('1.Square spiral')
print('2.Tree design')
print('3.Circle design')
print('4.Dancing line')
print('5.sunflower')
print('6.Star')
print('7,Ninja')
print('8.Hexagon')
print('9.clock')
print('10.corona')
ch=int(input("Enter your choice:"))
if(ch==1):
    square_spiral()
elif(ch==2):
    tur_tree()
elif(ch==3):
    cir_des()
elif(ch==4):
    dan_des()
elif(ch==5):
    sun_flw()
elif(ch==6):
    star()
elif(ch==7):
    ninja()
elif(ch==8):
    hexa()
elif(ch==9):
    clock()
elif(ch==10):
    corona()
else:
    print('Inappropriate Choice')
