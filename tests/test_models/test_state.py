#!/usr/bin/python3
"""
Unit test for the State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases fir the State class"""

    def test_attributes(self):
        """Test that the State class has the correct attribute"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
