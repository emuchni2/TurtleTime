# Fill shape algorithmically then outline



# Import Functions/Tools
from helpers import *



# Define Tortoise Class
class Tortoise(turtle.Turtle):
	def __init__(self,*args,**kwargs):
		super().__init__()

		self.stepSize = 10
		self.pathGoal = 100
		self.odometer = 0
		self.rotateAngle = 122
		self.increaseFactor = 4


# Functions

"""
inputArray = array of tuples (coords)
"""
def executePath(inputTuples,inputTurtle,color):

	# Don't show turtle and go to first point of polygon
	inputTurtle.color(color)
	inputTurtle.hideturtle()
	inputTurtle.penup()
	inputTurtle.setpos(inputTuples[0][0],inputTuples[0][1])

	# Show pen + turtle and iterate through polygon
	inputTurtle.hideturtle()
	inputTurtle.pendown()
	for i in range(1,len(inputTuples)):
		inputTurtle.goto(inputTuples[i][0],inputTuples[i][1])


def iterativeMovement(inputTortoise,boundaryPoly,boundaryLineString):
	
	#Move forward
	headingAngle = inputTortoise.heading() * math.pi/180
	headingVector = np.array([math.cos(headingAngle),math.sin(headingAngle)])
	currentPos = inputTortoise.pos()

	predictedSpot = currentPos + inputTortoise.stepSize*headingVector
	pointNext = Point(predictedSpot)
	futureLegality = pointNext.within(boundaryPoly)     # True


	if futureLegality == True:

		#inputTortoise.color('green')
		inputTortoise.forward(inputTortoise.stepSize)
		inputTortoise.odometer = inputTortoise.odometer + inputTortoise.stepSize


		if inputTortoise.odometer > inputTortoise.pathGoal:
			print('path change')
			inputTortoise.right(inputTortoise.rotateAngle)
			inputTortoise.pathGoal = inputTortoise.pathGoal + inputTortoise.increaseFactor
			inputTortoise.odometer = 0

	if futureLegality == False:

		#inputTortoise.color('red')
		
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


		inputTortoise.right(70) #TODO change

		
def shadePolygon(inputTuples,inputColor,startPos = None,**kwargs):
	A = Tortoise()
	A.color(inputColor)
	A.width(1)

	fillSteps = 200


	boundaryPoly = Polygon(inputTuples)
	boundaryLineString = LineString(inputTuples)

	A.penup()

	if startPos != None:
		A.setpos(startPos)

	A.pendown()
	for i in range(0,fillSteps):
		iterativeMovement(A,boundaryPoly,boundaryLineString)



	executePath(inputTuples,A,color = 'black')

if __name__ == '__main__':
		


	# Setup turtle screen
	turtle.setup(800, 600)
	wn = turtle.Screen()
	wn.bgcolor("white")
	wn.title("Turtle Artist")


	


	boundaryTuples = generate_polygon(center=(0, 0), avg_radius=100, irregularity=0.01,spikiness=0.2,num_vertices=16)
	boundaryTuples.append(boundaryTuples[0])

	print(boundaryTuples)
	shadePolygon(boundaryTuples,'red')
	



	new = generate_polygon(center=(300,300), avg_radius=100, irregularity=0.01,spikiness=0.2,num_vertices=8)
	new.append(new[0])
	print(new)
	shadePolygon(new,'green',startPos = (300,300))
	


	new = generate_polygon(center=(-200,200), avg_radius=100, irregularity=0.01,spikiness=0.2,num_vertices=8)
	new.append(new[0])
	print(new)
	shadePolygon(new,'blue',startPos = (-200,200))
	



	wn.exitonclick()