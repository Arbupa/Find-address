from unittest.case import expectedFailure
from .address import Address
from .distance import find_distance
import unittest
#import pytest


class TestFindDistance(unittest.TestCase):

    # normal tests of the function.
    def test_find_distance(self):
        real = find_distance("-53.373061", "-8.626851")
        expected = 10855.406521690002
        self.assertEqual(real, expected)

        real = find_distance("10.551701", "51.228764")
        expected = 1851.6036849750005
        self.assertEqual(real, expected)

        real = find_distance("-102.277714", "23.530679")
        expected = 10442.31747647962
        self.assertEqual(real, expected)

        real = find_distance("-105.983713", "54.164145")
        expected = 7380.151552184582
        self.assertEqual(real, expected)

        real = find_distance("1.943388", "46.790884")
        expected = 2644.487200861031
        self.assertEqual(real, expected)

        real = find_distance("1.544599", "42.528762")
        expected = 2965.776166830954
        self.assertEqual(real, expected)

        real = find_distance("22.302411", "39.267074")
        expected = 2150.9981760625674
        self.assertEqual(real, expected)

        real = find_distance("139.268181", "36.72451")
        expected = 7384.976334019954
        self.assertEqual(real, expected)

        real = find_distance("139.268181", "36.72451")
        expected = 7384.976334019954
        self.assertEqual(real, expected)

        real = find_distance("170.455747", "-44.069583")
        expected = 16469.206744135572
        self.assertEqual(real, expected)

        real = find_distance("-8.448826", "39.489874")
        expected = 3811.095736133726
        self.assertEqual(real, expected)

        real = find_distance("99.505405", "61.698657")
        expected = 3507.135228763138
        self.assertEqual(real, expected)

        real = find_distance("-61.283356", "10.685546")
        expected = 9584.409742422167
        self.assertEqual(real, expected)

        real = find_distance("-65.441092", "6.494347")
        expected = 10223.841956245451
        self.assertEqual(real, expected)

        real = find_distance("26.308349", "-13.243134")
        expected = 7713.839238904956
        self.assertEqual(real, expected)

    # testing function with no parameters.
    def test_find_distance_no_params(self):
        try:
            find_distance()
        except:
            assert AssertionError(
                "Must send 2 parameters (lat, lon) to function.")

    # testing if the parameters are an address string or coordinates
    def test_parameters_type(self):
        first_param = 1
        second_param = 1
        if (str != type(first_param) and (str != type(second_param))):
            assert AssertionError(
                "The parameters must be numbers or an address.")

    # testing with booleans
    def test_parameters_type2(self):
        a = True
        b = False
        try:
            find_distance(a, b)
        except:
            assert AssertionError(
                "Must send 2 parameters from type float (lat, lon) to function.")

    # testing with empty strings
    def test_parameters_type3(self):
        a = ""
        b = ""
        try:
            find_distance(a, b)
        except:
            assert AssertionError(
                "Must send 2 parameters from type float (lat, lon) to function.")

    # testing with empty lists
    def test_parameters_type4(self):
        a = []
        b = []
        try:
            find_distance(a, b)
        except:
            assert AssertionError(
                "Must send 2 parameters from type float (lat, lon) to function.")

    # testing with empty tuples
    def test_parameters_type5(self):
        a = ()
        b = ()
        try:
            find_distance(a, b)
        except:
            assert AssertionError(
                "Must send 2 parameters from type float (lat, lon) to function.")

    # testing with empty dictionaries.
    def test_parameters_type6(self):
        a = {}
        b = {}
        try:
            find_distance(a, b)
        except:
            assert AssertionError(
                "Must send 2 parameters from type float (lat, lon) to function.")
