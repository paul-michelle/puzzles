import unittest
from reverse_a_number import reverse_digits_rec as rev


class TestNumbersReverse(unittest.TestCase):

    def test_digits_reversed_correctly(self):
        self.assertEqual(rev(-123), -321)
        self.assertEqual(rev(-12300), -321)
        self.assertEqual(rev(-10**27), -1)
        self.assertEqual(rev(10**27), 1)
        self.assertEqual(rev(505), 505)
        self.assertEqual(rev(0), 0)
        self.assertEqual(rev(1), 1)
        self.assertEqual(rev(12345), 54321)
        self.assertEqual(rev(111), 111)


