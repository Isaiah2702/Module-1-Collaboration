import unittest
from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)  # This will fail

if __name__ == "__main__":
    unittest.main()

# When running the test.py script using the unittest framework, one test passed and one test failed.
# The test_list_int function correctly validated that the sum of the list [1, 2, 3] is 6.
# However, the test_list_fraction function failed because it expected the sum of the fractions [1/4, 1/4, 2/5] to equal 1, but the actual result was 9/10. 