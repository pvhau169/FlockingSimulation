from p5 import *
import random

def setup():
  size(640, 360);
  


def draw():
	r = 2
	fill(200, 100)
	stroke(255)
	pushMatrix()
	position = Vector(100, 100)
	translate(position.x, position.y)
	rotate(theta)
	beginShape(TRIANGLES)
	vertex(0, -r*2)
	vertex(-r, r*2)
	vertex(r, r*2)
	endShape()
	popMatrix()
	
run()
	