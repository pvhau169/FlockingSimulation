from p5 import *
from Boid import *
boids  = []
circles = []
circles.append(Vector(200,200))
circles.append(Vector(150,300))
circles.append(Vector(450,100))
def setup():
    size(640, 360)
    background(255)
    for i in range(30):
        boids.append(Boid(width, height))
		
def draw():
    background(51)
    for boid in boids:
        boid.edges(width, height)
        # print(boid.position)
        boid.flock(boids, circles)
        boid.update()
        boid.show()

    # if mouse_is_pressed:
    #     fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    # else:
    #     fill(255, 15)

    # circle_size = random_uniform(low=10, high=80)

    # circles.append(Vector(mouse_x, mouse_y))
    for obstructor in circles:
        circle(obstructor, 30)

if __name__ == '__main__':
    
    run(frame_rate = 60)