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
        points[50] = (4,4)
        self.assertTrue(c.cond_0(points, d.PARAMETERS))

    def test_lic0_less(self):
        points = self.reset_points()
        points[50] = (1,1)
        self.assertFalse(c.cond_0(points, d.PARAMETERS))

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

    def test_lic2_angle_smaller(self):
        points = self.reset_points()
        points[50] = (0,0)
        points[51] = (2,0)
        points[52] = (0,-10)
        self.assertTrue(c.cond_2(points, d.PARAMETERS))

    def test_lic2_angle_larger(self):
        points = self.reset_points()
        points[50] = (0,0)
        points[51] = (2,0)
        points[52] = (0,10)
        print(c.angle(points[50], points[51], points[52]))
        self.assertTrue(c.cond_2(points, d.PARAMETERS))

    def test_lic2_angle_undefined(self):
        points = self.reset_points()
        self.assertFalse(c.cond_2(points, d.PARAMETERS))

    

if __name__ == '__main__':
    unittest.main()
