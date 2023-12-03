import unittest

from solutions import AddTwoIntegers


class TestPalindromeNumber(unittest.TestCase):
    def setUp(self):
        self.solution = AddTwoIntegers()

    def test_case1(self):
        expected = 17
        actual = self.solution.sum(12, 5)
        self.assertEqual(actual, expected)

    def test_case2(self):
        expected = -6
        actual = self.solution.sum(-10, 4)
        self.assertEqual(actual, expected)
