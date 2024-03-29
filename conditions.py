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

def cond_2(points, epsilon):
	for i in range(len(points) - 2):
		p1, p2, p3 = points[i], points[i+1], points[i+2]
		theta = angle(p1, p2, p3)
		if theta < (np.pi - epsilon) or theta > (np.pi + epsilon):
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

def cond_8(points, a_pts, b_pts, radius):
	if len(points) < 5:
		return False
	for i in range(len(points) - a_pts - b_pts - 2):
		p1, p2, p3 = points[i], points[i+a_pts+1], points[i+a_pts+b_pts+2]
		if not circ_can_contain(radius, p1, p2, p3):
			return True
	return False

def cond_9(points, c_pts, d_pts, epsilon):
	if len(points) < 5:
		return False
	for i in range(len(points) - c_pts - d_pts - 2):
		p1, p2, p3 = points[i], points[i + c_pts + 1], points[i + c_pts + d_pts + 2]
		if angle(p1, p2, p3) < d.PI - epsilon or angle(p1, p2, p3) > d.PI + epsilon:
			if not(p2 == p1 or p2 == p3):
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

def cond_12(points, k_pts, length1, length2):
	if len(points) < 3:
		return False
	cond1 = False
	cond2 = False
	for i in range(len(points) - k_pts -1):
		if dist(points[i], points[i + k_pts + 1]) > length1:
			cond1 = True
		if dist(points[i], points[i + k_pts + 1]) < length2:
			cond2 = True
		if cond1&cond2:
			return True
	return False

def cond_13(points, a_pts, b_pts, radius1, radius2):
	# contained in radius 1
	condition1 = False
	# contained in radius 2
	condition2 = False

	if len(points) < 5:
		return False
	# 3 points, first and second seperated exactly by a, second and third separated exactly by b. So i would arrive to n-a-b-1
	# example, a=2, b=3, n=10, i would range from 0 to 3
	for i in range(0, len(points) - a_pts - b_pts - 2):
		p1 = points[i]
		p2 = points[i + a_pts + 1]
		p3 = points[i + a_pts + b_pts + 2]
		if (not circ_can_contain(radius1, p1, p2, p3)):
			condition1 = True
		if circ_can_contain(radius2, p1, p2, p3):
			condition2 = True

	return condition1 and condition2


def cond_14(points, e_pts, f_pts, area1, area2):
	cond_1, cond_2 = False, False
	if len(points) < 5:
		return False
	for i in range(len(points) - e_pts - f_pts - 2):
		p1, p2, p3 = points[i], points[i + e_pts + 1], points[i + e_pts + f_pts + 2]
		if area(p1, p2, p3) > area1:
			cond_1 = True
		if area(p1, p2, p3) < area2:
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

