import numpy as np

# Constants
PI = np.pi

# Inputs to the decide() function
class Parameters:
	def __init__(
			self,
			length1=0,
			radius1=1,
			epsilon=2,
			area1=3,
			q_pts=4,
			quads=4,
			dist=6,
			n_pts=6,
			k_pts=7,
			a_pts=8,
			b_pts=8,
			c_pts=9,
			d_pts=9,
			e_pts=10,
			f_pts=10,
			g_pts=11,
			length2=12,
			radius2=13,
			area2=14
		):

		self.length1 = length1
		self.radius1 = radius1
		self.epsilon = epsilon
		self.area1 = area1
		self.q_pts = q_pts
		self.quads = quads
		self.dist = dist
		self.n_pts = n_pts
		self.k_pts = k_pts
		self.a_pts = a_pts
		self.b_pts = b_pts
		self.c_pts = c_pts
		self.d_pts = d_pts
		self.e_pts = e_pts
		self.f_pts = f_pts
		self.g_pts = g_pts
		self.length2 = length2
		self.radius2 = radius2
		self.area2 = area2

# Global variable declarations
PARAMETERS = Parameters()

X = np.ones(shape=(100))
Y = np.ones(shape=(100))
NUMPOINTS = 100

LCM_MATRIX = np.full(shape=(15, 15), fill_value=1)

