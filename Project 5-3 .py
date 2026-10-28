import turtle
import random
t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.bgcolor("white")
A = input("CHAPE??")
B = input("COLADOR??")
C = int(input ("LAGENESS??"))

t.color(B)
if A == ("triangle"):
  t.begin_fill()
  t.goto(t.xcor() + C, t.ycor())
  t.goto(t.xcor() - C, t.ycor())
  t.right(-60)
  t.forward(C)
  t.right(120)
  t.forward(C)
  t.right(-60)
  t.end_fill()
