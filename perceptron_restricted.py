from random import random, choice, uniform

TRIALS = 1000000
ALPHA = 0.25
INPUTS = [(0,4,-1,0), (4,0,-1,0), (2.01,2.01,-1,1)]
TEST = INPUTS + [(4.1,0,-1,1), (0,4.1,-1,1)]

def f(w, x):
	return int( (w[0]*x[0] + w[1]*x[1] + w[2]*x[2]) > 0)

def trained(w):
	for x in INPUTS:
		if(not (f(w,x) == x[3])):
			return False
	return True

def verifyNetwork(w, epochs):
	print("Epochs\t =", epochs)
	print("w\t =", w)
	print()
	for x in TEST:
		y = f(w, x)
		t = x[3]
		if(y == t):
			print("True", t, x)
		else:
			print("False", t, x)

	print("\nEquation:","y", ">",-w[0]/w[1], "*", "x", "+", w[2]/w[1])

def trainPerceptronWeights():
	epochs = 0
	w = [uniform(-1, 1) for i in range(3)]
	while(epochs < TRIALS and not trained(w)):
		for x in INPUTS:
			y = f(w, x)
			t = x[3]
			w = delta(w, y, t, x)
		epochs += 1
	return w, epochs

def delta(w, y, t, x):
	w[0] = w[0] - ALPHA*(y-t)*x[0]
	w[1] = w[1] - ALPHA*(y-t)*x[1]
	w[2] = w[2] - ALPHA*(y-t)*x[2]
	return w

def main():
	w, epochs = trainPerceptronWeights()
	verifyNetwork(w, epochs)

if __name__ == '__main__':
	main()
