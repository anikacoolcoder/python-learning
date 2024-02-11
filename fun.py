# Import turtle package
from turtle import *
import turtle as tur
  
# Creating a turtle object(pen)
pen = tur.Turtle()
pen.speed(100)
# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)

def square():
    pen.fillcolor('light green')
    for i in range(4):
        pen.forward(100)
        pen.left(90)


def triangle():
    pen.forward(100)
    pen.left(120)
    pen.forward(100)6tg6 
    pen.left(120)ä''
    pen.forward(100)   
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    pen.fillcolor('light pink')
  
    # Start filling the color
    pen.begin_fill()
  
    # Draw the left line
    pen.left(140)
    pen.forward(113)
  
    # Draw the left curve
    curve()
    pen.left(120)
  
    # Draw the right curve
    curve()
  
    # Draw the right line
    pen.forward(112)
  
    # Ending the filling of the color
    pen.end_fill()
  
# Defining method to write text
def txt():
  
    # Move turtle to air
    pen.up()
  
    # Move turtle to a given position
    pen.setpos(-68, 95)
  
    # Move the turtle to the ground
    pen.down()
  
    # Set the text color to lightgreen
    pen.color('lightgreen')
  
    # Write the specified text in 
    # specified font style and size
    pen.write("hallo", font=(
      "Verdana", 12, "bold"))
  
  
# Draw a heart
triangle()
  
# Write text
txt()
  
# To hide turtle
tur.hideturtle()
tur.done()






