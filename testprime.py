"""Test cases that checks the prime number generator"""
import unittest
from prime import prime_num

class TestPrime(unittest.TestCase):
    """A class that contains test cases of primenumbers"""
    def test_if_it_accepts_string_datatype(self):
        """This will test that the  string datatype is not accepted"""
        with self.assertRaises(TypeError):
            prime_num("string")

    def test_if_it_accepts_dictionary(self):
        """Test if dictionary is accepted"""
        with self.assertRaises(TypeError):
            prime_num({})

    def test_if_it_accepts_lists(self):
        """Test if list are accepted"""
        with self.assertRaises(TypeError):
            prime_num([])

    def test_if_it_accepts_lists(self):
        """Test if list datatype is accepted"""
        with self.assertRaises(TypeError):
            prime_num(56.58)
    def test_if_input_is_negative(self):
    	"""Tests if it accepts negative numbers"""
    	self.assertEquals(prime_num(-5), "Numbers less than or equal to zero are not allowed!")
    def test_if_input_is_one(self):
    	"""Tests if one is a prime number"""
    	self.assertEquals(prime_num(1), "One is not a prime number")
    def test_if_input_is_zero(self):
    	"""Tests if zero is a prime number"""
    	self.assertEquals(prime_num(0), "Numbers less than or equal to zero are not allowed!")
    def test_if_it_outputs_correct_output(self):
    	"""Tests if it outputs correct result"""
    	self.assertEquals(prime_num(5), [2, 3, 5])
    def test_if_it_outputs_correct_output_for_numbers_greater_than_50(self):
    	"""Tests if it outputs correct result"""
    	self.assertEquals(len(prime_num(55)), 16)
    def test_if_it_includes_a_number_i(self):
    	"""Tests if a number is prime is included in the list"""
    	self.assertIn(5, prime_num(5))
    def test_if_it_includes_a_number_if_the_number_is(self):
    	"""Tests the input number is prime is included in the list"""
    	self.assertNotIn(16, prime_num(16))
""""team asgard thanks millie great help"""
