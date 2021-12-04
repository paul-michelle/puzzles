import unittest
from max_area_of_island import *

grid_8_13 = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
]

grid_4_4 = [
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0]
]


class TestAreaCalculation(unittest.TestCase):

    def test_max_area_is_defined_correctly(self):
        archipelago = Archipelago()
        self.assertEqual(archipelago.get_largest_land_area(grid_4_4), 3)
        self.assertEqual(archipelago.get_largest_land_area(grid_8_13), 6)
