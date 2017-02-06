"""A collection of tests that checks if the program is working """
import unittest
from prime import primenum
class TestPrime(unittest.TestCase):
    """A class that contains testcases for the prime test"""
    def test_input_is_a_number(self):
         with self.assert_Raises(TypeError):
             primenum("string")
    def test_input_is_a_number(self):
        with self.assert_Raises(TypeError):
            primenum([])
    def test_input_is_a_number(self):
        with self.assert_Raises(TypeError):
            primenum({})
    def test_if_input_is_zero(self):
        with self.assert_Raises(TypeError):
            primenum=0

