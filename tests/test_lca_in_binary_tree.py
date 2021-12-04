import unittest
from lca_in_binary_tree import *


class TestBinaryTreeOperator(unittest.TestCase):

    def test_finding_lowest_common_ancestor(self):

        operator = BinaryTreeOperator()

        result1 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 7, 4
        )
        result2 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 2, 4
        )
        result3 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 7, 2
        )
        self.assertTrue(result1 == result2 == result3 == 2)

        result1 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 6, 2
        )
        result2 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 6, 7
        )
        result3 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 6, 4
        )
        self.assertTrue(result1 == result2 == result3 == 5)

        result1 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 5, 0
        )
        result2 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 5, 8
        )
        result3 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 5, 1
        )
        self.assertTrue(result1 == result2 == result3 == 3)

        result1 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 4, 13
        )
        result2 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 4, 14
        )
        result3 = operator.find_lowest_common_ancestor(
            [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, 13, 14], 7, 3
        )
        self.assertTrue(result1 == result2 == result3 == 3)
