import turtle
T = turtle.Turtle()
T.speed(123456789)
VAR = 0
while True:
    T.forward(45)
    T.right(44)
    T.forward(45)
    T.right(43)
    VAR+=1
    T.color(VAR*0.3,VAR*30,VAR)
