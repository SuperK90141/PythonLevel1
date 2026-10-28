import turtle
import random
t = turtle.Turtle()
t.speed(1)
s = turtle.Screen()
s.bgcolor("white")
t.color("black")

def move_up():
    t.goto(t.xcor(), t.ycor() + 100)
s.onkeypress(move_up, "Up")

def move_down():
    t.goto(t.xcor(), t.ycor() - 100)
s.onkeypress(move_down, "Down")

def move_left():
    t.goto(t.xcor() - 100, t.ycor())
s.onkeypress(move_left, "Left")

def move_right():
    t.goto(t.xcor() + 100, t.ycor())
s.onkeypress(move_right, "Right")

def move_1():
    t.goto(t.xcor() + 100, t.ycor())
    t.goto(t.xcor(), t.ycor() + 100) 
    t.goto(t.xcor() - 100, t.ycor())
    t.goto(t.xcor(), t.ycor() - 100)
s.onkeypress(move_1, "1")

def move_2():
    t.circle(50)

s.onkeypress(move_2, "2")

def move_3():
    t.color("white")

s.onkeypress(move_3, "3")

def move_4():
    t.color("black")

s.onkeypress(move_4, "4")

def move_5():
    t.clear()

s.onkeypress(move_5, "5")

def move_6():
    t.goto(t.xcor() + 100, t.ycor())
    t.goto(t.xcor() - 100, t.ycor())
    t.right(-60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(-60)
s.onkeypress(move_6, "6")

def move_7():
    t.write('''..  -.-. .- -.  -  -... . .-.. .. ...- .  - .... .- -  -.-- --- ..-  .-- .- ... - . -..  . -. --- ..- --. ....  - .. -- .  - ---  ..-. .. --. ..- .-. .  --- ..- -  .-- .... .- -  - .... .. ...  ... . -. - . -. -.-. .  ... .- .. -..

''')
s.onkeypress(move_7, "7")

def move_8():
    t.goto(t.xcor() + 100, t.ycor())
    t.goto(t.xcor(), t.ycor() + 100) 
    t.goto(t.xcor() - 100, t.ycor())
    t.goto(t.xcor(), t.ycor() - 100)
    t.goto(t.xcor(), t.ycor() + 100)
    t.right(-60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(-60)
s.onkeypress(move_8, "8")


s.listen()
s.mainloop()
