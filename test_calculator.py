# https://github.com/ArturoAlizo/lab10-AA.git
# Partner 1: Arturo Alizo


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 100), 2.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(1, 10)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-2, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5.0)

if __name__ == "__main__":
    unittest.main()