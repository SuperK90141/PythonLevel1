import turtle
import random
t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.bgcolor(135, 206, 235)
t.penup()
MTKN = ["red","orange","yellow","green","blue","purple"]
t.goto(-255, 255)
for i in MTKN:
  t.pendown()
  t.color(i)
  t.begin_fill()
  t.forward(510)
  t.right(90)
  t.forward(80)
  t.right(90)
  t.forward(510)
  t.right(90)
  t.forward(80)
  t.right(90)
  t.end_fill()
  t.penup()
  t.right(90)
  t.forward(80)
  t.left(90)
  
