import random
import turtle
import time


def display_hour_label(turtle_object):
   turtle_object.hideturtle()
   turtle_object.penup()
   turtle_object.goto(0, 0)
   turtle_object.setheading(90)
   for i in range(12):
       turtle_object.forward(190)
       turtle_object.pendown()
       turtle_object.forward(20)
       turtle_object.penup()
       turtle_object.goto(0, 0)
       turtle_object.right(30)


def display_minute_label(turtle_object):
   turtle_object.hideturtle()
   turtle_object.penup()
   turtle_object.goto(0, 0)
   turtle_object.setheading(90)
   for i in range(60):
       turtle_object.forward(200)
       turtle_object.pendown()
       turtle_object.forward(10)
       turtle_object.penup()
       turtle_object.goto(0, 0)
       turtle_object.right(6)


def draw_hour_numbers(turtle_object):
   turtle_object.hideturtle()
   angle = 60
   for i in range(1, 13):
       turtle_object.penup()
       turtle_object.goto(0, 0)
       turtle_object.setheading(angle)
       turtle_object.forward(170)
       turtle_object.pendown()
       turtle_object.color("darkblue")
       turtle_object.write(str(i), move=False, align="center", font=("arial", 10, "normal"))
       angle -= 30


def draw_hour_hand(hours, turtle_object):
   turtle_object.hideturtle()
   turtle_object.penup()
   turtle_object.goto(0, 0)
   turtle_object.pencolor("green")
   turtle_object.setheading(90)
   angle = (hours / 12) * 360
   turtle_object.right(angle)
   turtle_object.pendown()
   turtle_object.forward(80)


def draw_minute_hand(minutes, turtle_object):
   turtle_object.hideturtle()
   turtle_object.penup()
   turtle_object.goto(0, 0)
   turtle_object.pencolor("yellow")
   turtle_object.setheading(90)
   angle = (minutes / 60) * 360
   turtle_object.right(angle)
   turtle_object.pendown()
   turtle_object.forward(110)


def draw_second_hand(seconds, turtle_object):
   turtle_object.hideturtle()
   turtle_object.penup()
   turtle_object.goto(0, 0)
   turtle_object.pencolor("red")
   turtle_object.setheading(90)
   angle = (seconds / 60) * 360
   turtle_object.right(angle)
   turtle_object.pendown()
   turtle_object.forward(150)


def description(turtle_object):
   turtle_object.hideturtle()
   turtle_object.penup()
   turtle_object.goto(0, 0)
   turtle_object.color("indigo")
   turtle_object.setheading(268)
   turtle_object.forward(255)
   turtle_object.setheading(0)
   turtle_object.forward(5)
   turtle_object.write("Developed by Bisrat", move=False, align="center", font=("monospace", 25, "normal"))


def draw_container(hours, minutes, seconds, turtle_object):
   turtle_object.penup()
   turtle_object.goto(0, 210)
   turtle_object.setheading(180)
   turtle_object.pencolor("darkblue")
   turtle_object.pendown()
   turtle_object.circle(210)
   turtle_object.hideturtle()

   display_hour_label(turtle_object)
   display_minute_label(turtle_object)
   draw_hour_numbers(turtle.Turtle())

   draw_hour_hand(hours, turtle_object)
   draw_minute_hand(minutes, turtle_object)
   draw_second_hand(seconds, turtle_object)
   description(turtle.Turtle())


display_current_time = turtle.Turtle()
display_current_time.speed(10)
turtle1 = turtle.Turtle()
turtle1.hideturtle()
window = turtle.Screen()
window.title("Clock Assignment, submitted to Kabila Haile")
window.bgcolor("aqua")
window.setup(600, 600)
turtle1.speed(10)
turtle1.pensize(3)
window.tracer(0)

rectangular_box = turtle.Turtle()
rectangular_box.hideturtle()
rectangular_box.penup()
rectangular_box.pensize(3)
rectangular_box.color("darkblue")
rectangular_box.goto(80, 230)
rectangular_box.pendown()
rectangular_box.forward(150)
rectangular_box.setheading(90)
rectangular_box.forward(50)
rectangular_box.setheading(180)
rectangular_box.forward(150)
rectangular_box.setheading(-90)
rectangular_box.forward(50)

button = turtle.Turtle()
button.hideturtle()
button.penup()
button.goto(-250, 230)
button.pensize(3)
button.pencolor("darkblue")
button.pendown()
button.forward(250)
button.left(90)
button.forward(50)
button.left(90)
button.forward(250)
button.left(90)
button.forward(50)
button.penup()
button.goto(-245, 240)
button.pendown()
button.write("Click here, to toggle theme", move=False, font=("monospace", 15, "italic"))

button_x, button_y, button_length, button_width = -250, 230, 250, 50
backgrounds = ["white", "black", "snow", "crimson", "darkorange", "cyan", "powderblue", "skyblue", "silver", "lavender"]


def button_clicked_toggle(x, y):
   if button_x <= x <= button_x + button_length:
       if button_y <= y <= button_y + button_width:
           window.bgcolor(random.choice(backgrounds))


escape = turtle.Turtle()
escape.hideturtle()
escape.penup()
escape.goto(-190, -290)
escape.pendown()
escape.pensize(2)
escape.pencolor("darkblue")
escape.write("Smash escape key to close the turtle window", font=("monospace", 15, "italic"))

window.listen()
window.onclick(button_clicked_toggle)
window.onkeypress(window.bye, "Escape")


while True:
   try:
       hour = int(time.strftime("%I"))
       minute = int(time.strftime("%M"))
       second = int(time.strftime("%S"))

       draw_container(hour, minute, second, turtle1)
       display_current_time.goto(93, 235)
       display_current_time.hideturtle()
       display_current_time.clear()
       display_current_time.pencolor("darkblue")
       display_current_time.write(str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2),
                                  font=("monospace", 25, "normal"))
       window.update()
       time.sleep(1)
       turtle1.clear()

   except:
       break

window.mainloop()
try:
   turtle.done()
except turtle.Terminator:
   pass
