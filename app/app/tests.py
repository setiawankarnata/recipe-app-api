"""
Tests for the calculator app
"""

from django.test import SimpleTestCase

from . import calc


class TestCalc(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding two numbers together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting two numbers"""
        res = calc.subtract(12, 5)
        self.assertEqual(res, 7)
