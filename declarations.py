import numpy as np

# Constants
PI = np.pi

# Inputs to the decide() function
class Parameters:
	def __init__(
		# TODO : improve defaults
			self,
			length1=1,
			radius1=1,
			epsilon=1,
			area1=1,
			q_pts=1,
			quads=1,
			dist=1,
			n_pts=1,
			k_pts=1,
			a_pts=1,
			b_pts=1,
			c_pts=1,
			d_pts=1,
			e_pts=1,
			f_pts=1,
			g_pts=1,
			length2=1,
			radius2=1,
			area2=1
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

# Global variable declarationss
PARAMETERS = Parameters()

NUMPOINTS = 100
X = np.ones(shape=(NUMPOINTS))
Y = np.ones(shape=(NUMPOINTS))

DIMENSION = 15
LCM = np.full(shape=(DIMENSION, DIMENSION), fill_value=1)
PUV = np.full(shape=DIMENSION, fill_value=True)
