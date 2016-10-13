import unittest
from prime import prime

class PrimeNumbersTest(unittest.TestCase):
    """Test prime_numbers function"""
    def test_for_zero(self):
        """Test that zero returns an empty list"""
        self.assertEqual(prime(0), [], msg="Zero should return an empty list")
    def test_first_three_primes(self):
        """Test first three prime numbers"""
        self.assertEqual(prime(
            3), [2, 3, 5], msg="First three primes should be [2, 3, 5]")
    def test_first_five_primes(self):
        """Test first five prime numbers"""
        self.assertEqual(prime(
            5), [2, 3, 5, 7, 11], msg="First three primes should be [2, 3, 5, 7, 11]")
    def test_for_negative_numbers(self):
        """Raise value error if the input is negative"""
        with self.assertRaises(ValueError):
            prime(-3)
    def test_for_non_integers(self):
        """Raise error if the input is not an integer"""
        with self.assertRaises(TypeError):
            prime('str')
if __name__ == '__main__':
    unittest.main()