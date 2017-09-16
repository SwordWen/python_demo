import unittest
import sys
import math

sys.path.append("../src")

from math_demo import distance

class TestMathDemo(unittest.TestCase):

    def test_distance_1(self):
        #print "distance(1,1,0,0) = " + str(distance(1,1,0,0))
        self.assertEqual(distance(1,1,0,0), math.sqrt(2))
        self.assertEqual(distance(2,2,0,0), math.sqrt(8))
        self.assertEqual(distance(3,4,0,0), 5)


if __name__ == '__main__':
    unittest.main()