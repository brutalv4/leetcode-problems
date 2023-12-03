import unittest

from solutions import TwoSum


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = TwoSum()

    def test_case1(self):
        expected = [0, 1]
        actual = self.solution.two_sum([2, 7, 11, 15], 9)
        self.assertEqual(actual, expected)

    def test_case2(self):
        expected = [1, 2]
        actual = self.solution.two_sum([3, 2, 4], 6)
        self.assertEqual(actual, expected)

    def test_case3(self):
        expected = [0, 1]
        actual = self.solution.two_sum([3, 3], 6)
        self.assertEqual(actual, expected)
