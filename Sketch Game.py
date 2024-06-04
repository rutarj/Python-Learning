"""
Turtle Control Application
This Python program allows users to control a turtle using keyboard inputs and provides additional functionalities.

How It Works
Upon running the program, a turtle window opens, and a turtle named "tim" is displayed.
Users can control the turtle's movement using the following keys:
W: Move the turtle forward.
S: Move the turtle backward.
A: Rotate the turtle left.
D: Rotate the turtle right.
Additional functionalities:
Backspace: Undo the last action performed by the turtle.
T: Clear the drawing canvas and reset the turtle to its initial position.
Usage
Clone or download the repository to your local machine.
Make sure you have Python installed.
Open a terminal or command prompt and navigate to the directory containing the Python script.
Run the script using the command: python turtle_control.py.
Use the keyboard inputs mentioned above to control the turtle and access additional functionalities.
Requirements
Python 3.x
Turtle module (included in the standard library)
"""
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_upward():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_downward():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def undo():
    tim.undo()

def clear():
    tim.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_upward, "a")
screen.onkey(move_downward, "d")
screen.onkey(undo, "BackSpace")
screen.onkey(clear, "t")


screen.exitonclick()


