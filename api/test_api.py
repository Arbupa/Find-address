from .address import Address
from .api import search_address
import unittest


class TestApi(unittest.TestCase):

    # testing type of response with different values.
    def test_search_address(self):
        locations = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia',
                     'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan']
        for country in locations:
            self.assertEqual(list, type(search_address(country)))

    # testing with no parameters
    def test_no_parameters(self):
        try:
            search_address()
        except:
            assert AssertionError(
                "Must send 1 string parameter to function.")

    # testing type passing numbers as parameters
    def test_testing_numbers(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for num in numbers:
            self.assertEqual(list, type(search_address(num)))

    # testing type with float numbers as parameters
    def test_testing_float_parameters(self):
        numbers = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.7, 9.7, 10.10]
        for num in numbers:
            self.assertEqual(list, type(search_address(num)))

    # testing type with boolean as parameters
    def test_testing_boolean_parameters(self):
        booleans = [True, False, False, False,
                    True, True, False, True, True, False]
        for elem in booleans:
            self.assertEqual(list, type(search_address(elem)))

    # testing type with special characters as parameters
    def test_sending_special_chars(self):
        special_characters = ['#', '&', '!', '~', '@', '$',
                              '*', '+', '{', ']', ':', '<', '?', '.']
        for elem in special_characters:
            self.assertEqual(list, type(search_address(elem)))

    # testing with special characters if is instance of the Address class.
    def test_search_address_is_instance(self):
        special_characters = ['#', '&', '!', '~', '@', '$',
                              '*',  ':', '<', '?', '.', '%']
        for elem in special_characters:
            result = search_address(elem)
            assert(isinstance(result[0], Address))

    # testing with special characters if is instance of the Address class.
    def test_address_with_special_chars(self):
        expected = []
        special_characters = [']', '-', '[', ';']
        for elem in special_characters:
            result = search_address(elem)
            self.assertEqual(expected, result)
