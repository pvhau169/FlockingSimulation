from p5 import *
import random
class Boid:

    #default constructor
    def __init__(self, width, height): 
        self.position = Vector(random.uniform(0, width), random.uniform(0, height))
		angle = random.uniform(0, TWO_PI)
		
		
        self.velocity = Vector(cos(angle), sin(angle))
        self.acceleration = Vector(0, 0) 
		self.r = 2.0
        self.maxForce = 0.03
        self.maxSpeed = 2

	def run(self, boids, circles):
		flock(boids, circles)
		update()
		edges()
		show()
	
	def applyForce(self, force):
		self.acceleration += force
		
	def flock(self, boids, circles):
        alignment = self.align(boids)
        cohesion  = self.cohesion(boids)
        separation = self.separation(boids)
		
		separation *= 1.5
		alignment *= 1
		cohesion *= 1
		
		self.applyForce(separation)
		self.applyForce(alignment)
		self.applyForce(cohesion)
        
		#avoid = self.avoid(circles)
        #self.applyForce(avoid)

    # def avoid(self, circles):
    #     separation = self.separation(boids)
    #     self.acceleration += alignment
    #     self.acceleration += cohesion
    #     self.acceleration += separation
	
	def update(self):
		self.velocity += self.acceleration
		self.velocity.limit(self.maxSpeed)
		
        self.position += self.velocity
        self.acceleration *=0

	def seek(self, target):
		desired = target - self.position
		desired.normalize()
		desired.mult(self.maxSpeed)
		
		steer = desired - self.velosity
		steer.limit(self.maxForce)
		return steer

    def edges(self, width, height):
        if self.position.x > width:
            self.position.x  = 0
        elif self.position.x <0:
            self.position.x = width
        
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height
			
    def show(self):
        # print('asd')
        circle(self.position, 8)
        # print(self.position)
        # print(self.velocity)
        # stroke(255)

    
    def align(self, boids):
        total = 0
        perceptionRadius = 50
        steering = Vector(0,0)
        for other in boids:
            if dist(self.position, other.position) <=perceptionRadius and other.position != self.position:
                steering += other.velocity
                total +=1
        if total !=0:
            steering/=total
            steering.magnitude = self.maxSpeed
            steering-= self.velocity
            steering.limit(self.maxForce)
        return steering
        # print(avg)
        # print(len(boids))
    
    def cohesion(self, boids):
        total = 0
        perceptionRadius = 50
        steering = Vector(0,0)
        for other in boids:
            if dist(self.position, other.position) <=perceptionRadius and other.position != self.position:
                steering += other.position
                total +=1
        if total !=0:
            steering/=total
            # steering.magnitude = self.maxSpeed
            steering-= self.position
            steering.magnitude = self.maxSpeed
            # print(steering)
            steering-= self.velocity
            steering.limit(self.maxForce)
            # print(steering)
        return steering
        # print(avg)
        # print(len(boids))

    def separation(self, boids):
        total = 0
        perceptionRadius = 50
        steering = Vector(0,0)
        diff = Vector(0, 0)
        for other in boids:
            if dist(self.position, other.position) <=perceptionRadius and other.position != self.position:
                diff = self.position - other.position
                diff /= dist(self.position, other.position)
                steering += diff
                total +=1
        if total !=0:
            steering/=total
            # steering.magnitude = self.maxSpeed
            steering.magnitude = self.maxSpeed
            # print(steering)
            steering-= self.velocity
            steering.limit(self.maxForce)
            # print(steering)
        return steering
        # print(avg)
        # print(len(boids))
	
    def avoid(self, circles):
        total = 0
        perceptionRadius = 50
        steering = Vector(0,0)
        diff = Vector(0, 0)
        for other in circles:
            if dist(self.position, other) <=perceptionRadius:
                diff = self.position - other
                diff /= dist(self.position, other)
                steering += diff
                total +=1
        if total !=0:
            steering/=total
            # steering.magnitude = self.maxSpeed
            steering.magnitude = self.maxSpeed * 2
            # print(steering)
            steering-= self.velocity
            steering.limit(self.maxForce * 2)
            # print(steering)
        return steering
        # print(avg)
        # print(len(boids))

    
        
