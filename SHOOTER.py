import turtle
import random
t = turtle.Turtle()
t.speed(3)
s = turtle.Screen()
s.bgcolor("black")
t.color("white")
t.penup()

while True:
  X56 = random.randint(-255,255)
  Y56 = random.randint(-300,270)
  t.penup()
  t.goto(X56,Y56)
  t.pendown()
  t.color("red")
  t.circle(20)
  t.penup()
  t.speed(0)
  t.color("white")
  t.goto(0,-255)

  X = input("X")
  Y = input("Y")
  t.speed(2)
  t.penup()
  t.goto(X,Y)
  
  if int(X) < X56+3 and int(X) > X56-3:
  	if int(Y) < Y56+3 and int(Y) > Y56-3:
  		t.write("YAY")

  else: 
    t.write(str (X56) + "-" + str (Y56))
      
      
