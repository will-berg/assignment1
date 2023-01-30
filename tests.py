import unittest

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

    def test_lic1(self):
        """There exists at least one set of three consecutive data points that cannot all be contained within or on a circle of radius RADIUS1."""
        # Positive instance
        points = self.reset_points()
        points[50] = (2*d.PARAMETERS.radius1,2*d.PARAMETERS.radius1)
        points[51] = (4*d.PARAMETERS.radius1,4*d.PARAMETERS.radius1)
        points[52] = (6*d.PARAMETERS.radius1,6*d.PARAMETERS.radius1)
        self.assertTrue(c.cond_1())
        
        # Negative instance
        #Within radius
        points[50] = (1,1)
        points[51] = (1,1)
        points[52] = (1,1)
        self.assertFalse(c.cond_1())
        
        #On radius
        points[50] = (d.PARAMETERS.radius1, 0)
        points[51] = (0,d.PARAMETERS.radius1)
        points[52] = (0,-d.PARAMETERS.radius1)
        self.assertFalse(c.cond_1())

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

if __name__ == '__main__':
    unittest.main()
