from django.test import SimpleTestCase

from app import calc

class CalcSimpleTests(SimpleTestCase):
    """ Test the calc module. """

    def test_add_number(self):
        "test adding two numbers together"
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """ test subtracting two numbers together """
        res = calc.subtract(10, 6)
        self.assertEqual(res, 4)