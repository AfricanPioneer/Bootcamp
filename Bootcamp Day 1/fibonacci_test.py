import unittest
from fibonacci import fibonacci
class FibonacciNumbersTest(unittest.TestCase):
    """Test fibonacci_numbers function"""
    def test_for_zero(self):
        """Test that zero returns an empty list"""
        self.assertEqual(fibonacci(0), 0, msg="Zero should return an empty list")
    def test_first_three_fibonacci_numbers(self):
        """Test first three fibonacci numbers"""
        self.assertEqual(fibonacci(
            3), [0, 1, 1], msg="First three fibonacci numbers should be [0, 1, 1]")
    def test_first_five_fibonacci_numbers(self):
        """Test first five fibonacci numbers"""
        self.assertEqual(fibonacci(
            5), [0, 1, 1, 2, 3], msg="First three fibonacci numbers should be [0, 1, 1, 2, 3]")
    def test_for_negative_numbers(self):
        """Raise value error if the input is negative"""
        with self.assertRaises(ValueError):
            fibonacci(-1)
    def test_for_non_integers(self):
        """Raise error if the input is not an integer"""
        with self.assertRaises(TypeError):
            fibonacci('str')
if __name__ == '__main__':
    unittest.main()