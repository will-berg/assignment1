import unittest
import numpy as np

import decide
import conditions as c
import declarations as d

class testDecide(unittest.TestCase):
    def reset_points(self):
        x = d.X
        y = d.Y
        points = []
        for i in range(d.NUMPOINTS):
            points.append((x[i], y[i]))
        return points

    def test_lic0_greater(self):
        """There exists at least one set of two consecutive data points that are a distance greater than the length, LENGTH1, apart."""
        points = self.reset_points()
        length = 1

        points[50] = (4,4)

        self.assertTrue(c.cond_0(points, length))

    def test_lic0_less(self):
        points = self.reset_points()
        length = 1

        points[50] = (1,1)

        self.assertFalse(c.cond_0(points, length))

    # LIC 1 is met if three consecutive points cannot be contained inside a circle of the specified radius.
    def test_lic1_outside(self):
        points = self.reset_points()
        radius = 1

        points[50] = (2*d.PARAMETERS.radius1,2*d.PARAMETERS.radius1)
        points[51] = (4*d.PARAMETERS.radius1,4*d.PARAMETERS.radius1)
        points[52] = (6*d.PARAMETERS.radius1,6*d.PARAMETERS.radius1)
        self.assertTrue(c.cond_1(points, radius))

    # LIC 1 is not met if all sets of three consecutive points can be contained within a circle of the specified radius.
    def test_lic1_inside(self):
        points = self.reset_points()
        radius = 1

        # Within radius
        points[50] = (1,1)
        points[51] = (1,1)
        points[52] = (1,1)
        self.assertFalse(c.cond_1(points, radius))

    # LIC 1 is not met if the three consecutive points lie exactly on the radius of the circle.
    def test_lic1_on(self):
        points = np.zeros(shape=(100, 2))
        radius = 1

        # On the circle
        points[50] = (d.PARAMETERS.radius1, 0)
        points[51] = (0,d.PARAMETERS.radius1)
        points[52] = (0,-d.PARAMETERS.radius1)
        self.assertFalse(c.cond_1(points, radius))

    def test_lic2_angle_smaller(self):
        points = self.reset_points()
        points[50] = (0,0)
        points[51] = (2,0)
        points[52] = (0,-10)
        self.assertTrue(c.cond_2(points, d.PARAMETERS.epsilon))

    def test_lic2_angle_larger(self):
        points = self.reset_points()
        points[50] = (0,0)
        points[51] = (2,0)
        points[52] = (0,10)
        self.assertTrue(c.cond_2(points, d.PARAMETERS.epsilon))

    def test_lic2_angle_undefined(self):
        points = self.reset_points()
        self.assertFalse(c.cond_2(points, d.PARAMETERS.epsilon))

    """ Tests for LIC3 : There exists at least one set of three consecutive data points that are the vertices of a triangle
with area greater than AREA1. AREA1 is fixed to 2."""
    def test_lic3_area_greater_area1(self): #positive instance
        points = self.reset_points()        
        # Negative Coordinates
        points[50]=(-1,0)
        points[51]=(-1,3)
        points[52]=(1,1)
        self.assertTrue(c.cond_3(points, 2))
        # Positive Coordinates
        points[50]=(0,0)
        points[51]=(2,0)
        points[52]=(0,3)
        self.assertTrue(c.cond_3(points, 2))
    
    def test_lic3_area_smaller_area1(self): #negative instance
        points = self.reset_points()        
        #Positive Coordinates
        self.assertFalse(c.cond_3(points, 2))
        # Negative Coordinates
        points[50]=(-1,1)
        points[51]=(-1,0)
        self.assertFalse(c.cond_3(points,2))

    def test_lic3_non_consecutives_coordinates(self): #negative instance
        points = self.reset_points()        
        # Non consecutives Coordinates
        points[50]=(0,2)
        points[51]=(0,0)
        points[52]=(1,1)
        points[53]=(0,2)
        self.assertFalse(c.cond_3(points, 2))

    def test_lic3_area_equal_aerea1(self): #negative instance
        points = self.reset_points()        
        # Negative Coordinates
        points[50]=(-1,1)
        points[51]=(-1,2)
        self.assertFalse(c.cond_3(points,2))
        # Positive Coordinates
        points[50]=(0,0)
        points[51]=(2,0)
        points[51]=(0,2)
        self.assertFalse(c.cond_3(points, 2))

    """ Tests for LIC4 : There exists at least one set of Q PTS consecutive data points that lie in more than QUADS quadrants."""
    def test_lic4_quadrant(self): # all points are in the same quadrant (I)
        points = self.reset_points()      
        self.assertTrue(c.cond_4(points, 10, 1))
        self.assertFalse(c.cond_4(points, 10, 2))
        self.assertFalse(c.cond_4(points, 10, 3))

    def test_lic4_quadrant(self): # points are in two different quadrants
        points = self.reset_points() # quadrant I
        points[50]=(-1,1) #quadrant II
        self.assertTrue(c.cond_4(points, 10, 1))
        self.assertTrue(c.cond_4(points, 10, 2))
        self.assertFalse(c.cond_4(points, 10, 3))

    def test_lic4_quadrant(self): # points are in three different quadrants
        points = self.reset_points() # quadrant I
        points[50]=(-1,1) #quadrant II
        points[51]=(-1,-1) #quadrant III
        self.assertTrue(c.cond_4(points, 10, 1))
        self.assertTrue(c.cond_4(points, 10, 2))
        self.assertTrue(c.cond_4(points, 10, 3))

        #Points in 3 different quadrants but not in the same consecutive group
        points[51]=(1,1) #quadrant I
        points[60]=(-1,-1) #quadrant III
        self.assertFalse(c.cond_4(points, 10, 3))

    def test_lic5_all_points_equal(self):
        points = np.zeros(shape=(100, 2))
        self.assertFalse(c.cond_5(points))

    def test_lic5_two_points_last_larger(self):
        points = [[0, 0], [1, 0]]
        self.assertTrue(c.cond_5(points))

    def test_lic6_less_than_three_points(self):
        points = [[0,0]]
        n = 1
        dist = 1
        self.assertFalse(c.cond_6(points, n, dist))

    def test_lic6_larger_distance(self):
        points = [[0, 0], [1, 2], [2, 0]]
        n = 3
        dist = 1

        self.assertTrue(c.cond_6(points, n, dist))

    def test_lic6_larger_distance_coincident_endpoints(self):
        points = [[0, 0], [2, 0], [0, 0]]
        n = 3
        dist = 1

        self.assertTrue(c.cond_6(points, n, dist))

    def test_lic6_smaller_distance(self):
        points = [[0, 0], [1, 1], [2, 0]]
        n = 3
        dist = 2

        self.assertFalse(c.cond_6(points, n, dist))

    def test_lic6_smaller_distance_coincident_endpoints(self):
        points = [[0,0], [1,0], [0,0]]
        n = 3
        dist = 2

        self.assertFalse(c.cond_6(points, n, dist))

    """Tests for LIC7 : There exists at least one set of two data points separated by exactly K PTS consecutive in-
tervening points that are a distance greater than the length, LENGTH1, apart."""
    def test_lic7(self): 
        points = self.reset_points() #All points are in the same position 
        self.assertFalse(c.cond_7(points, 3, 2))
        points[50]=(3,1)
        self.assertFalse(c.cond_7(points, 3, 2))
        points[50]=(4,1)
        self.assertTrue(c.cond_7(points, 3, 2))

        #The only 2 points separated by length > lenght1 are exactly k_pts points apart
        points[50] = (0,1)
        points[54] = (3,1)
        self.assertTrue(c.cond_7(points, 3, 2))

        # 2 points are separated by length > lenght1 but not k_pts points apart
        points[50] = (0,1)
        points[54] = (1,1)
        points[55] = (3,1)
        self.assertFalse(c.cond_7(points, 3, 2))

    # LIC 8 requires at least five points.
    def test_lic8_less_than_five_points(self):
        points = [[0,0], [1,1], [1,2]]
        a_pts = 1
        b_pts = 1
        radius = 1

        self.assertFalse(c.cond_8(points, a_pts, b_pts, radius))

    # LIC 8 is met if three points are outside the radius of the circle. 
    def test_lic8_points_outside_circle(self):
        points = np.zeros(shape=(10, 2))
        a_pts = 2
        b_pts = 3
        radius = 1

        base = 2
        points[base] = [-radius, 0]
        points[base + a_pts + 1] = [radius, 0]
        points[base + a_pts + 1 + b_pts + 1] = [0, radius + 1]

        self.assertTrue(c.cond_8(points, a_pts, b_pts, radius))

    # LIC 8 is not met if all sets of three points can be within the circle.
    def test_lic8_points_inside_circle(self):
        points = np.zeros(shape=(10, 2))
        a_pts = 2
        b_pts = 3
        radius = 1

        # Since all points is at [0, 0], they will all be able to fit inside the same circle.
        self.assertFalse(c.cond_8(points, a_pts, b_pts, radius))

    #LIC 9 requires at least five points.
    def test_lic9_less_than_five_points(self):
        points = [(1,1),(1,1)]
        self.assertFalse(c.cond_9(points, 1, 1, 1))
    
    #LIC 9 is met if angle is larger than PI + EPSILON, and the three data points are separated by exactly C PTS and D PTS.
    def test_lic9_angle_larger(self):
        points = [(0,0), (1,0), (2,0), (0,5), (0,10)]
        self.assertTrue(c.cond_9(points, 1, 1, 1))
    
    #LIC 9 is met if angle is smaller than PI - EPSILON, and the three data points are separated by exactly C PTS and D PTS.
    def test_lic9_angle_smaller(self):
        points = [(0,0), (1,0), (2,0), (0,5), (0,-10)]

        self.assertTrue(c.cond_9(points, 1, 1, 1))

    #LIC 9 is not met if either the first or the last pint coincide with the vertex.
    def test_lic9_angle_undefined(self):
        points = [(0,0), (1,0), (2,0), (0,5), (2,0)]
        self.assertFalse(c.cond_9(points, 1, 1, 1))

    """ Tests for LIC10 : There exists at least one set of three data points separated by exactly E PTS and F PTS con-
secutive intervening points, respectively, that are the vertices of a triangle with area greater
than AREA1"""
    def test_lic10(self):
        points = self.reset_points()
        # All points are in the same position
        self.assertFalse(c.cond_10(points, 2, 3, 2))

        # Creation of a triabgle of points that matches the conditions
        points[50]=(0,0)
        points[53]=(3,0)
        points[57]=(0,2)
        self.assertTrue(c.cond_10(points, 2, 3, 2))

        # Creation of a triabgle of points that matches the condition for the area but not the right amount of points in between
        points[53]=(1,1)
        points[54]=(3,0)
        self.assertFalse(c.cond_10(points, 2, 3, 2))

    """Tests for LIC11 : There exists at least one set of two data points separated by exactly K PTS consecutive in-
tervening points that are a distance greater than the length, LENGTH1, apart."""
    def test_lic11(self): 
        points = [[3, 0], [1, 0], [1, 0], [2,0]]
        g_pts = 2
        self.assertFalse(c.cond_11(points, g_pts))

        points = [[2, 0], [1, 0], [1, 0], [3,0]]
        self.assertTrue(c.cond_11(points, g_pts))

        points = [[2, 0], [1, 0], [3, 0], [1,0]]
        self.assertFalse(c.cond_11(points, g_pts))

        points = [[2, 0], [1, 0]]
        g_pts = 0
        self.assertFalse(c.cond_11(points, g_pts))
    
    #LIC 12 requires more than three points
    def test_lic12_less_than_three_points(self):
        points = [(1,2), (2,3)]
        self.assertFalse(c.cond_12(points, 1,1,1))

    #LIC 12 requires two points to be further apart than length1 and closer than length2 with K PTS between them, can also be the same or different points.
    def test_lic12_positive(self):
        points = [(1,1),(0,0),(0,0),(3,3)]
        self.assertTrue(c.cond_12(points, 2, 2, 4))

    #LIC 12 does should be false if the distance is 0.
    def test_lic12_negative(self):
        d.PARAMETERS.k_pts = 2
        d.PARAMETERS.length1 = 2
        d.PARAMETERS.length2 = 4
        points = [(1,1),(1,1),(1,1),(1,1)]
        self.assertFalse(c.cond_12(points, 2,2,4))

    # LIC 13 is met if the same set of three points lie both inside and outside of circles with dirrenent radii.
    def test_lic13_same_points_both_inside_outside(self):
        radius1 = 1
        radius2 = 3
        a_pts = 2
        b_pts = 3

        middle_radius = 2

        points = [[-middle_radius,0], [0,0], [0,0], [middle_radius, 0], [0,0], [0,0], [0,0], [0, middle_radius]]

        # There is only one set of three points possible to check,
        # and they all lie outside the first circle and inside the second circle.
        # This means this condition should be met.
        self.assertTrue(c.cond_13(points, a_pts, b_pts, radius1, radius2))

    # LIC 13 is met if different set of points is inside and outside the circles.
    def test_lic13_different_points_inside_outside(self):
        radius1 = 2
        radius2 = 3
        a_pts = 2
        b_pts = 3

        radius_inside = 1
        radius_outside = 4

        points = [[-radius_inside,0], [-radius_outside,10], [0,0], [radius_inside, 0], [radius_outside,10], [0,0], [0,0], [0, radius_inside], [0, 10 + radius_outside]]

        # The fist set of points will be inside both circles and the second set of points will be outside both circles,
        # which means that LIC 13 will be met using both sets of points.
        self.assertTrue(c.cond_13(points, a_pts, b_pts, radius1, radius2))

    # LIC 13 is not met if all sets of points is inside both circles.
    def test_lic13_all_points_inside(self):
        points = np.zeros(shape=(10,2))
        radius1 = 2
        radius2 = 3
        a_pts = 2
        b_pts = 3

        self.assertFalse(c.cond_13(points, a_pts, b_pts, radius1, radius2))

    # LIC 14 is not met if there are less than 5 points.
    def test_lic14_not_enough_points(self):
        points = np.zeros(shape=(4, 2))
        e_pts = 1
        f_pts = 1
        area1 = 1
        area2 = 2

        self.assertFalse(c.cond_14(points, e_pts, f_pts, area1, area2))

    # LIC 14 is met if the same set of points form an area both larger and smaller than the given areas.
    def test_lic14_same_points_both_larger_smaller(self):
        e_pts = 2
        f_pts = 3
        area1 = 1
        area2 = 4

        points = [[0, 0], [0,0], [0,0], [2, 0], [0,0], [0,0], [0,0], [0, 2]]

        self.assertTrue(c.cond_14(points, e_pts, f_pts, area1, area2))

    # LIC 14 is met if different sets of points are both larger and smaller than the areas.
    def test_lic14_different_points_larger_smaller(self):
        e_pts = 2
        f_pts = 3
        area1 = 2
        area2 = 3

        points = [[0,0], [0, 0], [0,0], [1, 0], [3, 0], [0,0], [0,0], [0, 1], [0, 3]]

        self.assertTrue(c.cond_14(points, e_pts, f_pts, area1, area2))

    # LIC 14 is not met if all triangles are smaller than the given areas.
    def test_lic14_all_triangles_smaller(self):
        points = np.zeros(shape=(10, 2))
        e_pts = 2
        f_pts = 3
        area1 = 2
        area2 = 3

        # Since all points are (0,0), all triangles will have an area of 0,
        # which is smaller than the given areas.
        self.assertFalse(c.cond_14(points, e_pts, f_pts, area1, area2))

class IntegrationTests(unittest.TestCase):
    # With the default config, DECIDE should return False.
    def test_default_config(self):
        self.assertFalse(decide.decide())

if __name__ == '__main__':
    unittest.main()