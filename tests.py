import unittest

import decide
import conditions as c
import declarations as d

x = d.X
y = d.Y
points = []
for i in range(d.NUMPOINTS):
    points.append((x[i], y[i]))

class testDecide(unittest.TestCase):
    def test_lic0(self):
        """There exists at least one set of two consecutive data points that are a distance greater than the length, LENGTH1, apart."""
        # Positive instance
        points[50] = (4,4)
        
        self.assertTrue(c.cond_0())

        points[50] = (1,1)

        # Negative instance
        self.assertFalse(c.cond_0())

    def test_lic1(self):
        """There exists at least one set of three consecutive data points that cannot all be contained within or on a circle of radius RADIUS1."""
        # Positive instance
        points[50] = (2*d.radius1,2*d.radius1)
        points[51] = (4*d.radius1,4*d.radius1)
        points[52] = (6*d.radius1,6*d.radius1)
        self.assertTrue(c.cond_1())
        
        # Negative instance
        #Within radius
        points[50] = (1,1)
        points[51] = (1,1)
        points[52] = (1,1)
        self.assertFalse(c.cond_1())
        
        #On radius
        points[50] = (d.radius1, 0)
        points[51] = (0,d.radius1)
        points[52] = (0,-d.radius1)
        self.assertFalse(c.cond_1())
    
    def test_lic2(self):
        # Positive instance

        # Negative instance
    
    def test_lic3(self):
        # Positive instance

        # Negative instance

    def test_lic4(self):
        # Positive instance

        # Negative instance

    def test_lic5(self):
        # Positive instance

        # Negative instance

    def test_lic6(self):
        # Positive instance

        # Negative instance

    def test_lic7(self):
        # Positive instance

        # Negative instance

    def test_lic8(self):
        # Positive instance

        # Negative instance

    def test_lic9(self):
        # Positive instance

        # Negative instance

    def test_lic10(self):
        # Positive instance

        # Negative instance

    def test_lic11(self):
        # Positive instance

        # Negative instance

    def test_lic12(self):
        # Positive instance

        # Negative instance

    def test_lic12(self):
        # Positive instance

        # Negative instance
    
    def test_lic13(self):
        # Positive instance

        # Negative instance
    
    def test_lic14(self):
        # Positive instance

        # Negative instance