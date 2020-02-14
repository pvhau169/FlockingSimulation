from p5 import *

def setup():
    size(640, 360)
    no_stroke()
    background(204)

def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle((mouse_x, mouse_y), 20)

def key_pressed(event):
    background(204)

run()