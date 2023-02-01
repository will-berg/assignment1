import declarations as d
import numpy as np


# Conditions to check
def cond_0(points, length):
	for i in range(len(points) - 1):
		if dist(points[i], points[i+1]) > length:
			return True
	return False

def cond_1(points, radius):
	for i in range(len(points) - 2):
		p1, p2, p3 = points[i], points[i+1], points[i+2]
		if not circ_can_contain(radius, p1, p2, p3):
			return True
	return False

def cond_2(points, parameters):
	for i in range(len(points) - 2):
		p1, p2, p3 = points[i], points[i+1], points[i+2]
		theta = angle(p1, p2, p3)
		if theta < (np.pi - parameters.epsilon) or theta > (np.pi + parameters.epsilon):
			if not(p2 == p1 or p2 == p3):
				return True
	return False

def cond_3(points, area1):
	for i in range(len(points) - 2):
		p1, p2, p3 = points[i], points[i+1], points[i+2]
		if area(p1, p2, p3) > area1:
			return True
	return False

def cond_4(points, q_pts, quad):
	for i in range(len(points) - q_pts):
		quadrant_used =[0, 0, 0, 0]
		sum = 0
		cond = False
		sum = 0
		for j in range(0, q_pts):
			quadj = quadrant(points[i+j])
			if quadrant_used[quadj] == 0:
				quadrant_used[quadj] = 1
				sum +=1
		if sum >= quad :
			return True
	return False

def cond_5(points):
	for i in range(len(points) - 1):
		xi, xj = points[i][0], points[i+1][0]
		if xi - xj < 0:
			return True
	return False

def cond_6(points, n, distance):
	if len(points) < 3:
		return False

	for i in range(0, len(points) - n + 1):
		firstPoint = points[i]
		lastPoint = points[i + n - 1]
		# 2 cases
		compareToPoint = False
		# If first and last point concide, compare dist with these points
		if firstPoint == lastPoint:
			compareToPoint = True
		else:
			# equation line of the form y = m*x + b
			m = (lastPoint[1] - firstPoint[1]) / (lastPoint[0] - firstPoint[0])
			b = firstPoint[1] - m*firstPoint[0]

		for j in range(i + 1, i + n - 1):
			if compareToPoint:
				d = dist(points[j], firstPoint)
			else:
				d = dist_point_line(points[j], m, b)
			if distance < d:
				return True
	return False

def cond_7(points, k_pts, length1):
	if len(points) < 3:
		return False
	for i in range(len(points) - k_pts - 1):
		p1, p2 = points[i], points[i + k_pts + 1]
		if dist(p1, p2) > length1:
			return True
	return False

def cond_8():
	if numpoints < 5:
		return False
	for i in range(numpoints - params.a_pts - params.b_pts):
		p1, p2, p3 = points[i], points[i+params.a_pts], points[i+params.a_pts+params.b_pts]
		if not circ_can_contain(params.radius1, p1, p2, p3):
			return True
	return False

def cond_9(points, params):
	if len(points) < 5:
		return False
	for i in range(len(points) - params.c_pts - params.d_pts):
		p1, p2, p3 = points[i], points[i+params.c_pts], points[i+params.c_pts+params.d_pts]
		if angle(p1, p2, p3) < d.PI - params.epsilon or angle(p1, p2, p3) > d.PI + params.epsilon:
			return True
	return False

def cond_10(points, e_pts, f_pts, area1):
	if len(points) < 5:
		return False
	for i in range(len(points) - e_pts - f_pts - 2):
		p1, p2, p3 = points[i], points[i + e_pts + 1], points[i + e_pts + f_pts + 2]
		if area(p1, p2, p3) > area1:
			return True
	return False

def cond_11(points, g_pts):
	if len(points) < 3:
		return False
	for i in range(len(points) - g_pts -1):
		if (points[i][0] - points[i + g_pts + 1][0]) < 0:
			return True
	return False

def cond_12():
	if numpoints < 3:
		return False
	cond1 = False
	cond2 = False
	for i in range(numpoints - params.k_pts -1):
		if dist(points[i], points[i + params.k_pts + 1]) > params.length1:
			cond1 = True
		if dist(points[i], points[i + params.k_pts + 1]) < params.length2:
			cond2 = True
		if cond1&cond2:
			return True
	return False

def cond_13():
	return True

def cond_14():
	cond_1, cond_2 = False, False
	if numpoints < 5:
		return False
	for i in range(numpoints - params.e_pts - params.f_pts):
		p1, p2, p3 = points[i], points[i+params.e_pts], points[i+params.e_pts+params.f_pts]
		if area(p1, p2, p3) > params.area1:
			cond_1 = True
		if area(p1, p2, p3) < params.area2:
			cond_2 = True
	return cond_1 and cond_2


# Helper functions

# Calculate Euclidean distance between two points in 2D
def dist(p1, p2):
	return np.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Calculates the angle formed by the three points p1, p2 (vertex), and p3
# https://stackoverflow.com/questions/1211212/how-to-calculate-an-angle-from-three-points
def angle(p1, p2, p3):
	return (np.arctan2(p2[1] - p1[1], p2[0] - p1[0]) - np.arctan2(p3[1] - p2[1], p3[0] - p2[0]) )% np.pi 

# Calculates the area of a triangle given three points (shoelace formula)
def area(p1, p2, p3):
	x1, y1, x2, y2, x3, y3 = p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]
	return 0.5 * np.abs(x1 * y2 - x3 * y2  + x3 * y1 - x1 * y3 + x2 * y3 - x2 * y1)

# Determines if the circle with radius r can contain the points p1-p3
def circ_can_contain(r, p1, p2, p3):
	if dist(p1, p2) > 2 * r or dist(p1, p3) > 2 * r or dist(p2, p3) > 2 * r:
		return False
	return True

# Calculates the distance between a 2d point p and a line of the form y=m*x + b
def dist_point_line(p, m, b):
	return np.abs( (m*p[0] - p[1] + b) / np.sqrt(m*m + 1) )

# Return the quadrant of a point
def quadrant(p):
	x, y = p[0], p[1]
	if y >=0 :
		if x >=0 :
			return 1
		else:
			return 2
	else :
		if x <=0 :
			return 3
		else:
			return 4

