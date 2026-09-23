import turtle
import random
t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.bgcolor("black")

for i in range(99):
  X = random.randint(-255,255)
  Y = random.randint(-255,255)
  C = random.randint(1,10)
  R = random.randint(0,255)
  G = random.randint(0,255)
  B = random.randint(0,255)
  t.color(R,G,B)
  t.penup()
  t.goto(X,Y)
  t.pendown()
  t.begin_fill()
  t.circle(C)
  t.end_fill()
