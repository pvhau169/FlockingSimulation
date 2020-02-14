from p5 import *
x = 100
y = 100

xspeed = 1
yspeed = 3.3

def setup():
    size(640, 360)
    background(255)

def draw():
 

    no_stroke()
    fill(255, 10)
    rect((0, 0), width, height)

    stroke(0)
    fill(175)
    a = Vector(100, 200)
    circle((a.x, a.y), 16)

if __name__ == '__main__':
    run()