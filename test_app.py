""" Module for importing TestCase """
from unittest import TestCase
from app import summ, minus,multiply

class TestApp(TestCase):
    """Class representing the test """
    #test de l'addition
    def test_sum_true(self):
        """ function testing sum if it's true """
        self.assertEqual(summ(1, 2), 3)

    def test_sum_wrong(self):
        """ function testing sum if it's wrong """
        self.assertNotEqual(summ(1, 2), 4)

    #test du soustraction
    def test_minus_true(self):
        """ function testing minus if it's true """
        self.assertEqual(minus(2, 1), 1)

    def test_minus_wrong(self):
        """ function testing minus if it's wrong """
        self.assertNotEqual(minus(2, 1), 2)

    #test de multiplication
    def test_multiply_true(self):
        """ function testing multiply if it's true """
        self.assertEqual(multiply(2, 2), 4)

    def test_multiply_wrong(self):
        """ function testing multiply if it's wrong """
        self.assertNotEqual(multiply(2, 2), 5)
