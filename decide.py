import declarations as d
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

	return FUV


if __name__ == "__main__":
	signal = decide()
	if signal:
		print("YES")
	else:
		print("NO")
