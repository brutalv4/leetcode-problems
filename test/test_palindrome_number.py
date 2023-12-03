import unittest

from solutions import PalindromeNumber


class TestPalindromeNumber(unittest.TestCase):
    def setUp(self):
        self.solution = PalindromeNumber()

    def test_case1(self):
        expected = True
        self.assertEqual(self.solution.is_palindrome_v1(121), expected)
        self.assertEqual(self.solution.is_palindrome_v2(121), expected)

    def test_case2(self):
        expected = False
        self.assertEqual(self.solution.is_palindrome_v1(-121), expected)
        self.assertEqual(self.solution.is_palindrome_v2(-121), expected)

    def test_case3(self):
        expected = False
        self.assertEqual(self.solution.is_palindrome_v1(10), expected)
        self.assertEqual(self.solution.is_palindrome_v2(10), expected)

    def test_case4(self):
        expected = True
        self.assertEqual(self.solution.is_palindrome_v1(123321), expected)
        self.assertEqual(self.solution.is_palindrome_v2(123321), expected)

    def test_case5(self):
        expected = True
        self.assertEqual(self.solution.is_palindrome_v1(42924), expected)
        self.assertEqual(self.solution.is_palindrome_v2(42924), expected)

    def test_case6(self):
        expected = True
        self.assertEqual(self.solution.is_palindrome_v1(0), expected)
        self.assertEqual(self.solution.is_palindrome_v2(0), expected)
