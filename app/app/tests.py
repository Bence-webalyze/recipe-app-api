"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        res = calc.add(5, 4)

        self.assertEqual(res, 9)

    def test_subract_numbers(self):
        """Substracting numbers"""

        res = calc.substract(10, 15)

        self.assertEqual(res, 5)
