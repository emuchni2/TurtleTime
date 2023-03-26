# Filling shape with fractals


# Libraries
import turtle
import math
from interpolatePoints import *

from shapely.geometry import Point, Polygon,LineString
import shapely
from mathHelpers import *


class Tortoise(turtle.Turtle):
	def __init__(self,*args,**kwargs):
		super().__init__()
		self.stepSize = 5
		self.pathGoal = 40
		self.odometer = 0
		self.rotateAngle = 0


# Functions

"""
inputArray = array of subarrays (e.g [x,y])
"""
def executePath2(inputTuples,inputTurtle):
	inputTurtle.hideturtle()
	inputTurtle.penup()

	inputTurtle.setpos(inputTuples[0][0],inputTuples[0][1])

	for i in range(1,len(inputTuples)):
		inputTurtle.pendown()

		inputTurtle.goto(inputTuples[i][0],inputTuples[i][1])


def executePath(inputArray,inputTurtle):
	inputTurtle.hideturtle()
	inputTurtle.setpos(inputArray[0,0],inputArray[0,1])

	for i in range(1,inputArray.shape[0]):
		inputTurtle.goto(inputArray[i,0],inputArray[i,1])


def iterativeMovement2(inputTortoise,boundaryPoly,boundaryLineString):
	
	#Move forward
	headingAngle = inputTortoise.heading() * math.pi/180
	headingVector = np.array([math.cos(headingAngle),math.sin(headingAngle)])
	currentPos = inputTortoise.pos()

	predictedSpot = currentPos + inputTortoise.stepSize*headingVector
	pointNext = Point(predictedSpot)
	futureLegality = pointNext.within(boundaryPoly)     # True


	if futureLegality == True:

		inputTortoise.color('green')
		inputTortoise.forward(inputTortoise.stepSize)
		inputTortoise.odometer = inputTortoise.odometer + inputTortoise.stepSize


		if inputTortoise.odometer > inputTortoise.pathGoal:
			print('path change')
			inputTortoise.right(60)
			inputTortoise.pathGoal = inputTortoise.pathGoal + 5
			inputTortoise.odometer = 0

	if futureLegality == False:

		inputTortoise.color('red')
		
		refA = Point(currentPos - headingVector*5)
		refB = Point(currentPos + headingVector*5)
		badLine = shapely.geometry.LineString([refA,refB])
		#print(badLine)
				# intersection = boundaryPoly.intersection(badLine)

		#line = shapely.geometry.LineString([[-10, -5], [15, 5]])

		# inputTortoise.right(60)

		try:
			badLine = shapely.geometry.LineString([currentPos, predictedSpot])
			intersection = boundaryLineString.intersection(badLine)
			hitPoint = [intersection.coords[0,0],intersection.coords[0,1]]
			inputTortoise.setpos(hitPoint)

		except Exception as E:
			print(E)
			print('intersect fail')


		inputTortoise.right(70)
		#s_poly.intersection(s_line)


	# else:
	# 	inputTortoise.color('green')

	# 	if inputTortoise.odometer > inputTortoise.pathGoal:
	# 		print('path change')
	# 		inputTortoise.right(60)
	# 		inputTortoise.pathGoal = inputTortoise.pathGoal + 5
	# 		inputTortoise.odometer = 0








	# Fractal Triggered change

	# Boundary Triggered Change


	#check if near any boundary points 

# def drawTriangleOutline(size, depth,turtle):

# 	turtle.showturtle()
# 	size = int(size)

# 	# Move the turtle to the top of the equilateral triangle:
# 	height = size * math.sqrt(3) / 2
# 	#turtle.penup()
# 	turtle.left(90)  # Turn to face upwards.
# 	turtle.forward(height * (2/3))  # Move to the top corner.
# 	turtle.right(150)  # Turn to face the bottom-right corner.
# 	turtle.pendown()






# Setup turtle screen
turtle.setup(800, 600)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Demo Screen")


# Instantiate a turtle 
A = Tortoise()
A.speed(2)
A.color("green")
A.width(1)

# vertices = 

# print(demoMatrix)


#demoMatrix = np.array([[0,200,300,200,10,0,0],[0,0,-200,-150,-30,-200,0]]).T #issue with going to beginning
# #demoMatrix = np.array([[0,200,200,0,0],[0,0,-200,-200,0]]).T #issue with going to beginning
# boundaryPoints = interpolatePoints(demoMatrix)
# boundaryTuples = list(zip(demoMatrix[:,0], demoMatrix[:,1]))

boundaryTuples = generate_polygon(center=(0, 0),
                            avg_radius=100,
                            irregularity=0.01,
                            spikiness=0.2,
                             num_vertices=16)
boundaryTuples.append(boundaryTuples[0])

boundaryPoly = Polygon(boundaryTuples)
boundaryLineString = LineString(boundaryTuples)
# print(boundaryTuples)
# print(boundaryLineString)

executePath2(boundaryTuples,A)

# now fill in
A.speed(9)
A.penup()
print(np.mean(boundaryTuples))
#A.setpos(np.mean(boundaryPoints, axis=0))
A.pendown()


#Begin shape stuff
for i in range(0,5000):
	iterativeMovement2(A,boundaryPoly,boundaryLineString)






	#demoMatrix = np.array([[0,200,300,200,10,0,0],[0,0,-200,-150,-30,-200,0]]).T #issue with going to beginning
	# #demoMatrix = np.array([[0,200,200,0,0],[0,0,-200,-200,0]]).T #issue with going to beginning
	# boundaryPoints = interpolatePoints(demoMatrix)
	# boundaryTuples = list(zip(demoMatrix[:,0], demoMatrix[:,1]))





wn.exitonclick()