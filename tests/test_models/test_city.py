#!/usr/bin/python3
"""
Unit test for the City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_attributes(self):
        """Test that the city class has the correct attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
