import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 10), 13)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 9), 18)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(45, 5), 9)

    def test_substact(self):
        self.assertEqual(self.calculator.substract(2, 9), -7)


if __name__ == '__main__':
    unittest.main()
