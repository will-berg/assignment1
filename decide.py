import declarations as d
import conditions as c
import numpy as np


# Generates a Boolean signal which determines whether an interceptor should be launched
# Based upon input radar tracking information in PARAMETERS
def decide():
	CMV = set_CMV()
	PUM = set_PUM(CMV, d.LCM)
	FUV = set_FUV(PUM, d.PUV)

	if np.all(FUV):
		launch = True
	else:
		launch = False

	return launch


# CMV is a boolean vector whose elements have a one-to-one correspondence with the LICs
# If the radar tracking data satisfy a certain LIC, then the corresponding element of the CMV is set to true.
def set_CMV():
	CMV = np.full(shape=d.DIMENSION, fill_value=False)
	CMV[0] = c.cond_0(d.POINTS, d.PARAMETERS.length1)
	CMV[1] = c.cond_1(d.POINTS, d.PARAMETERS)
	CMV[2] = c.cond_2(d.POINTS, d.PARAMETERS.radius1)
	CMV[3] = c.cond_3(d.POINTS, d.PARAMETERS.area1)
	CMV[4] = c.cond_4(d.POINTS, d.PARAMETERS.q_pts, d.PARAMETERS.quads)
	CMV[5] = c.cond_5(d.POINTS)
	CMV[6] = c.cond_6(d.POINTS, d.PARAMETERS.n_pts, d.PARAMETERS.dist)
	CMV[7] = c.cond_7(d.POINTS, d.PARAMETERS.k_pts, d.PARAMETERS.length1)
	CMV[8] = c.cond_8(d.POINTS, d.PARAMETERS)
	CMV[9] = c.cond_9(d.POINTS, d.PARAMETERS)
	CMV[10] = c.cond_10(d.POINTS, d.PARAMETERS.e_pts, d.PARAMETERS.f_pts, d.PARAMETERS.area1)
	CMV[11] = c.cond_11(d.POINTS, d.PARAMETERS.g_pts)
	CMV[12] = c.cond_12(d.POINTS, d.PARAMETERS)
	CMV[13] = c.cond_13(d.POINTS, d.PARAMETERS)
	CMV[14] = c.cond_14(d.POINTS, d.PARAMETERS)
	return CMV


# Every element of the boolean PUM corresponds to an element of the LCM.
# If the logical connection dictated by the LCM element gives the value “true”, the corresponding PUM element is set to true.
def set_PUM(CMV, LCM):
	PUM = np.full(shape=(d.DIMENSION, d.DIMENSION), fill_value=False)
	for i in range(d.DIMENSION):
		for j in range(d.DIMENSION):
			PUM[i, j] = set_PUM_element(CMV, LCM, i, j)
	return PUM

def set_PUM_element(CMV, LCM, i, j):
	if LCM[i, j] == "NOTUSED":
		return True
	elif LCM[i, j] == "ANDD":
		return CMV[i] and CMV[j]
	else:
		return CMV[i] or CMV[j]


# FUV is a boolean vector which is the basis for deciding whether to launch
# If all elements of the FUV are true, a launch should occur.
def set_FUV(PUM, PUV):
	FUV = np.full(shape=d.DIMENSION, fill_value=False)
	for i in range(d.DIMENSION):
		FUV[i] = set_FUV_element(PUM, PUV, i)
	return FUV

def set_FUV_element(PUM, PUV, i):
	if PUV[i] == False or np.all(PUM[i]):
		return True
	else:
		return False


if __name__ == "__main__":
	signal = decide()
	if signal:
		print("YES")
	else:
		print("NO")
