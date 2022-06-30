from turtle import Turtle, Screen

from tkinter import messagebox
import random


def display_result(winning_color, user_bet):
    result = Turtle()
    result.hideturtle()
    result.penup()
    result.goto(x=0, y=160)

    if winning_color == user_bet:
        result.write(f"You've WON! The {winning_color} turtle is the winner!",
                align="center", font=("Courier New", 12, "bold"))
    else:
        result.write(f"You've LOST! The {winning_color} turtle is the winner!",
                align="center", font=("Courier New", 12, "bold"))


screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
screen.cv._rootwindow.resizable(False, False)

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
while True:
    user_bet = screen.textinput(
            title="Make your bet",
            prompt="""Which turtle will win the race? Enter a color
[red, orange, yellow, green, blue, purple]:""")
    if user_bet.lower() in colors:
        break
    else:
        messagebox.showinfo("Input is not in the choices", "Wrong Input. Try again.")

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

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
        if turtle.xcor() < 230:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
        else:
            winning_color = turtle.pencolor()
            display_result(winning_color, user_bet)
            is_race_on = False

screen.exitonclick()
