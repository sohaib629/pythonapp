"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase): # Define class. Base class (SimpleTestCase). Derived class (CalcTests)
    """Test the calc module."""

    def test_add_numbers(self):  # Create method test_add_numbers
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
        
    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)

# Self represents the instance of the class. By using the “self” we can access the attributes and methods of the class
# in Python. It binds the attributes with the given arguments. The reason you need to use self. is because Python does
# not use the @ syntax to refer to instance attributes