from random import random, choice, uniform

TRIALS = 9000000
ALPHA = 0.25
INPUTS = [(0.01, 2, -1, 0, 0), (2, 0.01, -1, 0, 0), (-0.01, 2, -1, 0, 1), (-2, 0.01, -1, 0, 1), (-2, -0.01, -1, 1, 1), (-0.01, -2, -1, 1, 1), (0.01, -2, -1, 1, 0), (2, -0.01, -1, 1, 0)]
TEST = INPUTS + [(1, 1, -1, 0, 0), (1, 1, -1, 0, 1), (-1, -1, -1, 1, 1), (1, -1, -1, 1, 0)]

def f(w, x):
        return [int( (w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0), int( (w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0) ]

def trained(w):
	for x in INPUTS:
		if(not (f(w,x) == [x[3], x[4]])):
			return False
	return True

def verifyNetwork(w, epochs):
	print("Epochs\t =", epochs)
	print("w\t =", w)
	print()
	for x in INPUTS:
		y = f(w, x)
		t = [x[3], x[4]]
		if(y == t):
			print("True", t, x)
		else:
			print("False", t, x)

	print("\nEquation:","y", ">",-w[0][0]/w[1][0], "*", "x", "+", w[2][0]/w[1][0])
	print("Equation:","y", ">",-w[0][1]/w[1][1], "*", "x", "+", w[2][1]/w[1][1])



def trainPerceptronWeights():
	epochs = 0
	w = [[uniform(-1, 1), uniform(-1, 1)] for i in range(3)]
	while(not trained(w)):
		for x in INPUTS:
			if(epochs > TRIALS):
				return w, epochs
			epochs += 1
			y = f(w, x)
			t = [x[3], x[4]]
			w = delta(w, y, t, x)
	return w, epochs

def delta(w, y, t, x):
	w[0][0] = w[0][0] - ALPHA*(y[0] - t[0])*x[0]
	w[1][0] = w[1][0] - ALPHA*(y[0] - t[0])*x[1]
	w[2][0] = w[2][0] - ALPHA*(y[0] - t[0])*x[2]
	w[0][1] = w[0][1] - ALPHA*(y[1] - t[1])*x[0]
	w[1][1] = w[1][1] - ALPHA*(y[1] - t[1])*x[1]
	w[2][1] = w[2][1] - ALPHA*(y[1] - t[1])*x[2]
	return w


def main():
	w, epochs = trainPerceptronWeights()
	verifyNetwork(w, epochs)


if __name__ == '__main__':
	main()
