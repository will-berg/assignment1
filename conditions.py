import declarations as d
import numpy as np

# Globals
x = d.X
y = d.Y
numpoints = d.NUMPOINTS
points = []
for i in range(numpoints):
	points.append((x[i], y[i]))

params = d.PARAMETERS


# Conditions to check
def cond_0():
	for i in range(numpoints - 1):
		if dist(points[i], points[i+1]) > params.length1:
			return True
	return False

def cond_1():
	for i in range(numpoints - 2):
		p1, p2, p3 = points[i], points[i+1], points[i+2]
		if not circ_can_contain(params.radius1, p1, p2, p3):
			return True
	return False

def cond_2():
	for i in range(numpoints - 2):
		p1, p2, p3 = points[i], points[i+1], points[i+2]
		if p2 == p1 or p2 == p3:
			return False
		theta = angle(p1, p2, p3)
		if theta < d.PI - params.epsilon or theta > d.PI + params.epsilon:
			return True
	return False

def cond_3():
	for i in range(numpoints - 2):
		p1, p2, p3 = points[i], points[i+1], points[i+2]
		if area(p1, p2, p3) > params.area1:
			return True
	return False

def cond_4():
	return True

def cond_5():
	for i in range(numpoints - 1):
		xi, xj = x[i], x[i+1]
		if xi - xj < 0:
			return True
	return False

def cond_6():
	return True

def cond_7():
	return True

def cond_8():
	if numpoints < 5:
		return False
	for i in range(numpoints - params.a_pts - params.b_pts):
		p1, p2, p3 = points[i], points[i+params.a_pts], points[i+params.a_pts+params.b_pts]
		if not circ_can_contain(params.radius1, p1, p2, p3):
			return True
	return False

def cond_9():
	return True

def cond_10():
	return True

def cond_11():
	return True

def cond_12():
	return True

def cond_13():
	return True

def cond_14():
	return True


# Helper functions

# Calculate Euclidean distance between two points in 2D
def dist(p1, p2):
	return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Calculates the angle formed by the three points p1, p2 (vertex), and p3
# https://stackoverflow.com/questions/1211212/how-to-calculate-an-angle-from-three-points
def angle(p1, p2, p3):
	return np.arctan2(p3[1] - p1[1], p3[0] - p1[0]) - np.arctan2(p2[1] - p1[1], p2[0] - p1[0])

# Calculates the area of a triangle given three points (shoelace formula)
def area(p1, p2, p3):
	x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
	return 0.5 * np.abs(x1 * y2 - x3 * y2  + x3 * y1 - x1 * y3 + x2 * y3 - x2 * y1)

# Determines if the circle with radius r can contain the points p1-p3
def circ_can_contain(r, p1, p2, p3):
	if dist(p1, p2) > 2 * r or dist(p1, p3) > 2 * r or dist(p2, p3) > 2 * r:
		return False
	return True






