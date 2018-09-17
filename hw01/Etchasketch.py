#!/usr/bin/env python3
#EtchaSketch from Vinzenz Felder
# For ECE497 class Homework 1

import turtle

w =int (input('Which width'+ '\n'))

h =int( input('Which height'+'\n'))

#Inital
turtle.setup(w, h)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Etch A Sketch")
#setting for turtle and pensize
player = turtle.Turtle()
player.color("black")
player.shape("turtle")
player.pensize(5)

playerspeed = 20
# Turn left function
def move_left():
    x = player.xcor()
    x -= playerspeed
    player.setx(x)

# Turn right function 
def move_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)
# Turn up function
def move_up():
    y = player.ycor()
    y += playerspeed
    player.sety(y)
#Turn down function
def move_down():
    y = player.ycor()
    y -= playerspeed
    player.sety(y)
def bkcolor_white():
    wn.bgcolor("white")
# Clear the drawing area (delete drawing) function
def resetscreen():
    turtle.resetscreen()
# Exit the App function
def quit():
    print ("quit")
    turtle.bye()
#turtle action moving Methods
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(resetscreen, "space")
turtle.onkey(quit, "Q")
turtle.onkey(quit, "q")
#primary key for endless loop like While 1:
turtle.mainloop()
