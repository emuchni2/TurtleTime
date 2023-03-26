
# libraries 
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
import numpy as np



def interpolatePoints(matrixInput):
	x = list(matrixInput[:,0])
	y = list(matrixInput[:,1])

	# x.append(x[0])
	# y.append(y[0])
	print(x,y)
	tck, _ = splprep([x, y], s = 0, per = True)

	xx, yy = splev(np.linspace(0, 1, 100), tck, der = 0)
	newMatrix = np.vstack((xx.flatten(),yy.flatten())).T #Dumb method

	return newMatrix

if __name__ == "__main__":

	inputArray = np.array([[0, 5, 0, -6],[-4, 0, 2, 0]]).T

	#print(inputArray)

	output = interpolatePoints(inputArray)




	fig, ax = plt.subplots()

	ax.scatter(inputArray[:,0],inputArray[:,1])
	ax.scatter(output[:,0],output[:,1])

	plt.show()