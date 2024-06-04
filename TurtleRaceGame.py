"""
Turtle Race Game
This Python program simulates a race between six turtles using the Turtle module.

How It Works
The program prompts the user to bet on a turtle's color before starting the race.
Each turtle is assigned a unique color and positioned at the starting line.
Turtles move forward randomly in each iteration of the race.
The race continues until one of the turtles reaches the finish line (x-coordinate > 230).
Upon completion of the race, the program determines the winning turtle's color.
If the user's bet matches the winning turtle's color, they win; otherwise, they lose.
Usage
Clone or download the repository to your local machine.
Make sure you have Python installed.
Open a terminal or command prompt and navigate to the directory containing the Python script.
Run the script using the command: python turtle_race.py.
Follow the on-screen instructions to bet on a turtle and watch the race.
Requirements
Python 3.x
Turtle module (included in the standard library)
Example Output
vbnet
Copy code
Make your bet: (e.g., "red")
You've won! The red turtle is the winner!
"""

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
