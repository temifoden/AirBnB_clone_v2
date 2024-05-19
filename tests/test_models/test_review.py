#!/usr/bin/python3
"""
Unit test for the Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_attributes(self):
        """Test that the Review class has the correct attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
