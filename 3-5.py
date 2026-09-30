import turtle
import random
t = turtle.Turtle()
t.speed(1)
s = turtle.Screen()
s.bgcolor("black")
T = 0
OPQR = 2
IS = 62.000000000000000000000000000000000000001
PO = 62
while True:
  X = random.randint(-255,255)
  Y = random.randint(-300,270)
  C = random.randint(IS,PO)
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
  T += 1
  if T % 10 == 0:
    OPQR += 1
    IS -= 10
    PO -= 10
    t.speed(OPQR)
