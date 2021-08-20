from .address import Address
import unittest


class TestAddressClass(unittest.TestCase):

    # testing if is instance of main object class
    def test_is_instance(self):
        my_address = Address("", "", "")
        assert isinstance(my_address, Address)

    # testing if is instance of another class
    def test_is_instance2(self):
        class Fake():
            def __init__(self) -> None:
                pass

        my_class = Fake()
        if not isinstance(my_class, Address):
            assert AssertionError(
                "The object comparised is from another class")
        else:
            return True
