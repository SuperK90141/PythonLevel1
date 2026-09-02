import turtle
T = turtle.Turtle()
T.speed(0)
VAR = 0

for i in range(-200, -123456, -1):
	T.circle(i)
	T.left(i)
	T.forward(i)
	T.left(i)
	T.color(100,i*0,i*0)
