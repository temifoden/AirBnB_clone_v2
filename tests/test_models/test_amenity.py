#!/usr/bin/python3
"""
Unit test for the Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""
    def test_attributes(self):
        """Test that the Amenity class has the correct attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
