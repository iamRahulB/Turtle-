#####Turtle Intro######

from turtle import Turtle
t=Turtle()
sides=5

def cont(f):
	
	for _ in range(sides):
		angle=360/sides
		t.forward(f)
		t.right(angle)
forwa=50

for _ in range(10):
	cont(forwa)
	forwa+=10
