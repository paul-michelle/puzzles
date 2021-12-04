import unittest
from k_closest_points_to_origin import *


class TestEuclidianDistCalc(unittest.TestCase):

    def test_closest_points_are_defined_correctly(self):
        plane = XYPlane()
        self.assertTrue(
            len(plane.get_closest_to_origin([[1, 3], [-2, 2]], 1)) == 1
        )
        self.assertEqual(
            plane.get_closest_to_origin([[1, 3], [-2, 2]], 1),
            [[-2, 2]]
        )
        self.assertTrue(
            len(plane.get_closest_to_origin([[1, 3], [-2, 2]], 2)) == 2
        )
        self.assertEqual(
            sorted(plane.get_closest_to_origin([[1, 3], [-2, 2]], 2)),
            sorted([[-2, 2], [1, 3]])
        )
        self.assertTrue(
            len(plane.get_closest_to_origin([[1, 3], [-2, 2], [0, 0], [1, 1], [2, 4]], 3)) == 3
        )
        self.assertEqual(
            sorted(plane.get_closest_to_origin([[1, 3], [-2, 2], [0, 0], [1, 1], [2, 4]], 3)),
            sorted([[-2, 2], [0, 0], [1, 1]])
        )
